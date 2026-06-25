'''
调用本地whisper模型，生成完整的录音转文字，并存入成txt文档
'''
import os
from pathlib import Path
from typing import Callable

import numpy as np
import soundfile as sf
import soxr
from pywhispercpp.model import Model

from src.config.paths import TRANSCRIPT_DIR, ensure_output_dirs
from src.utils.logger import get_logger

log = get_logger(__name__)

# whisper 模型要求 16kHz 单声道
WHISPER_SAMPLE_RATE = 16000

# 转录时预留给界面/系统的线程数，避免吃满 CPU 导致 GUI 卡死
RESERVED_THREADS = 2


def _resolve_n_threads() -> int:
    """返回可用于转录的线程数：逻辑核数减去预留量，至少 1 个。"""
    cpu_count = os.cpu_count() or 1
    return max(1, cpu_count - RESERVED_THREADS)


def _load_audio_16k_mono(audio_file_path: str) -> np.ndarray:
    """读取 wav / mp3 等音频，统一转为 16kHz 单声道 float32 波形。

    使用 soundfile(libsndfile) 解码，soxr 重采样，二者的 wheel 均自带原生库，
    分发时无需用户额外安装 FFmpeg。
    """
    # always_2d=True 保证 data 形状为 (帧数, 声道数)，便于统一处理单/多声道
    data, sample_rate = sf.read(audio_file_path, dtype="float32", always_2d=True)

    # 多声道按均值混成单声道
    mono = data.mean(axis=1)

    # 采样率不是 16kHz 时重采样
    if sample_rate != WHISPER_SAMPLE_RATE:
        mono = soxr.resample(mono, sample_rate, WHISPER_SAMPLE_RATE)

    return mono.astype(np.float32)

# 返回路径的str格式，在一次性生成底稿和会议纪要时，需要路径寻找文件
def whisper_generate_transcript(
    model_file_path: str,
    audio_file_path: str,
    console_output: Callable[[str], None] = print,
) -> str | None:
    # 校验模型与音频文件是否存在
    if not Path(model_file_path).is_file():
        return _report_error(f"未找到 whisper 模型文件：{model_file_path}", console_output)
    if not Path(audio_file_path).is_file():
        return _report_error(f"未找到音频文件：{audio_file_path}", console_output)

    try:
        console_output("正在读取并解码音频...")
        # 自行解码为 16kHz 单声道数组后再喂给模型，避免依赖系统 FFmpeg
        audio = _load_audio_16k_mono(audio_file_path)

        n_threads = _resolve_n_threads()
        console_output(f"正在加载本地 whisper 模型（使用 {n_threads} 线程）...")
        model = Model(model_file_path, n_threads=n_threads)

        console_output("正在转录音频，请稍候...")
        segments = model.transcribe(audio, language="zh")
    except Exception as e:
        return _report_error(f"音频转录失败：{e}", console_output)

    # transcribe 返回 Segment 列表，需拼接各段文本得到完整底稿
    text = "".join(seg.text for seg in segments).strip()
    if not text:
        return _report_error("转录结果为空，请检查音频内容是否有效。", console_output)

    # 写入 txt 底稿，文件名沿用音频名
    ensure_output_dirs()
    out_path = TRANSCRIPT_DIR / f"{Path(audio_file_path).stem}.txt"
    out_path.write_text(text, encoding="utf-8")
    console_output(f"转录完成，底稿已保存到：{out_path}")

    return str(out_path)


# 统一的错误上报：同时写入日志和控制台（QTextEdit）
def _report_error(message: str, console_output: Callable[[str], None]) -> None:
    log.error(message)
    console_output(message)
    return None

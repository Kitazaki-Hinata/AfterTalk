'''
麦克风录音模块：采集系统默认输入设备的声音，停止时写成 wav 文件。

录音采用 16kHz 单声道，与 whisper 的输入要求一致，避免后续重采样。
采集在 PortAudio 的独立线程中通过回调进行，不阻塞 GUI。
'''

from datetime import datetime
from pathlib import Path
from typing import Callable

import numpy as np
import sounddevice as sd
import soundfile as sf

from src.config.paths import RECORDINGS_DIR, ensure_output_dirs
from src.utils.logger import get_logger

log = get_logger(__name__)

# whisper 要求 16kHz 单声道，录音直接对齐该规格
SAMPLE_RATE = 16000
CHANNELS = 1

# 录音文件名允许用户省略后缀，这里识别并剥离常见音频后缀，避免出现 name.wav.wav
_AUDIO_SUFFIXES = (".wav", ".mp3", ".m4a", ".flac", ".ogg")


class AudioRecorder:
    '''麦克风录音器：start() 开始采集，stop(filename) 停止并落盘，返回 wav 路径。'''

    def __init__(self):
        self._stream: sd.InputStream | None = None
        self._frames: list[np.ndarray] = []
        self._recording = False

    @property
    def is_recording(self) -> bool:
        return self._recording

    def start(self, console_output: Callable[[str], None] = print) -> None:
        '''开启输入流开始录音。重复调用在已录音时直接忽略。'''
        if self._recording:
            console_output("已经在录音中，无需重复开始。")
            return
        self._frames = []
        self._stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32",
            callback=self._callback,
        )
        self._stream.start()
        self._recording = True
        console_output(f"麦克风已就绪（{SAMPLE_RATE} Hz 单声道），开始录音...")

    def _callback(self, indata, frames, time_info, status) -> None:
        # 该回调运行在 PortAudio 线程，仅做拷贝入列，保持轻量
        if status:
            log.warning(f"录音状态异常：{status}")
        self._frames.append(indata.copy())

    def stop(self, filename: str = "", console_output: Callable[[str], None] = print) -> str:
        '''停止录音并把缓存的音频写入 RECORDINGS_DIR，返回保存路径。

        filename 不含后缀；为空时以「日期_时间」命名。
        '''
        if self._stream is not None:
            self._stream.stop()
            self._stream.close()
            self._stream = None
        self._recording = False

        name = self._resolve_filename(filename)
        ensure_output_dirs()
        out_path = RECORDINGS_DIR / f"{name}.wav"

        if self._frames:
            audio = np.concatenate(self._frames, axis=0)
        else:
            # 没有采集到任何数据时写入空音频，避免后续读取报错
            audio = np.empty((0, CHANNELS), dtype=np.float32)
            log.warning("未采集到任何音频数据，将写入空文件。")
            console_output("警告：未采集到任何音频数据，请检查麦克风设备。")

        console_output("录音已停止，正在保存音频文件...")
        sf.write(str(out_path), audio, SAMPLE_RATE)
        self._frames = []
        return str(out_path)

    @staticmethod
    def _resolve_filename(filename: str) -> str:
        '''规整用户输入的文件名：去空白、剥离音频后缀；为空则用日期时间。'''
        name = (filename or "").strip()
        if not name:
            return datetime.now().strftime("%Y%m%d_%H%M%S")
        p = Path(name)
        if p.suffix.lower() in _AUDIO_SUFFIXES:
            name = p.stem
        return name

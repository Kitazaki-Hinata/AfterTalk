'''
路径文件，内存有全部文件的路径

用法示例：
from src.config.paths import MODEL_DIR, RECORDINGS_DIR, ensure_output_dirs

ensure_output_dirs()
audio_out = RECORDINGS_DIR / "meeting_20260623.wav"

'''


from pathlib import Path

# ── 根目录 ──────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[2]   # AfterTalk/

# ── resource/ ───────────────────────────────────────────────────────────────
RESOURCE_DIR   = ROOT / "resource"
MODEL_DIR      = RESOURCE_DIR / "model"      # 本地 ASR 模型权重
SKILL_DIR      = RESOURCE_DIR / "skill"      # Deepseek system-prompt 模板 (*.md)
PICTURES_DIR   = RESOURCE_DIR / "pictures"

# ── output/ ─────────────────────────────────────────────────────────────────
OUTPUT_DIR        = ROOT / "output"
RECORDINGS_DIR    = OUTPUT_DIR / "recordings"   # 原始音频
TRANSCRIPT_DIR    = OUTPUT_DIR / "transcript"   # ASR 底稿
MINUTES_DIR       = OUTPUT_DIR / "minutes"      # 最终会议纪要

# ── logs/ ────────────────────────────────────────────────────────────────────
LOGS_DIR = ROOT / "logs"

# ── 项目根目录散文件 ─────────────────────────────────────────────────────────
ENV_FILE = ROOT / ".env"


def ensure_output_dirs() -> None:
    """确保所有 output/ 子目录及 logs/ 存在（首次运行时自动创建）。"""
    for d in (RECORDINGS_DIR, TRANSCRIPT_DIR, MINUTES_DIR, LOGS_DIR):
        d.mkdir(parents=True, exist_ok=True)
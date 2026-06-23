'''
统一日志模块。

用法示例：
    from src.utils.logger import get_logger
    log = get_logger(__name__)
    log.info("录音已保存")
    log.error("转写失败", exc_info=True)

日志同时输出到控制台和 logs/aftertalk_<日期>.log。
'''

import logging
import sys
from datetime import date
from src.config.paths import LOGS_DIR


# 对外接口：调用直接返回getLogger，name是模块名称
def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


def _setup_root_logger() -> None:
    root = logging.getLogger()
    if root.handlers:
        return

    root.setLevel(logging.DEBUG)
    fmt = logging.Formatter(
        fmt="%(asctime)s  %(levelname)-8s  %(name)s  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # 控制台：INFO 及以上
    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    console.setFormatter(fmt)

    # 文件：DEBUG 及以上，按天滚动（每次启动追加当天文件）
    log_file = LOGS_DIR / f"aftertalk_{date.today():%Y%m%d}.log"
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(fmt)

    root.addHandler(console)
    root.addHandler(file_handler)


# 模块被调用加载时即配置日志系统
_setup_root_logger()
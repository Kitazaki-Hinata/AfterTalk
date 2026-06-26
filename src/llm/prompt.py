'''读取skill.md，可以自行添加其他prompt然后修改这个模块'''

from typing import Callable
from src.config.paths import SKILL_DIR
from src.utils.logger import get_logger

log = get_logger(__name__)

def load_skill_prompt(skill_name: str = "skill", console_output: Callable[[str], None] = print) -> str:
    skill_file = SKILL_DIR / f"{skill_name}.md"
    if not skill_file.exists():
        log.error(f"Skill 文件不存在: {skill_file}")
        console_output(f"Skill 文件不存在: {skill_file}")
    return skill_file.read_text(encoding="utf-8")


def load_glossary(console_output: Callable[[str], None] = print) -> str:
    """读取专业术语纠错表 glossary.md；文件缺失时返回空串，不阻断生成流程。"""
    glossary_file = SKILL_DIR / "glossary.md"
    if not glossary_file.exists():
        log.warning(f"纠错文档不存在，将跳过术语纠错: {glossary_file}")
        console_output(f"纠错文档不存在，将跳过术语纠错: {glossary_file}")
        return ""
    return glossary_file.read_text(encoding="utf-8")

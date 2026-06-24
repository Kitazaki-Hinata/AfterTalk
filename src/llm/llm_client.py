'''
封装deepseek API的调用
选择deepseek模型，接受deepseek返回的内容
'''

from pathlib import Path
from typing import Callable
from openai import (
    OpenAI,
    APIStatusError,
    APIConnectionError,
    APITimeoutError,
    AuthenticationError,
    RateLimitError,
)

from src.utils.logger import get_logger

log = get_logger(__name__)


# 常量：展示可用模型，需要随着ds更新而更新列表，否则后面使用模型的时候会找不到模型
AVAILABLE_MODELS = [
    "deepseek-v4-flash",
    "deepseek-v4-pro",
]

_DEEPSEEK_BASE_URL = "https://api.deepseek.com"


# 创建ds 请求客户端，ui_function中调用
def create_client(api_key: str) -> OpenAI:
    client = OpenAI(
        api_key=api_key,
        base_url=_DEEPSEEK_BASE_URL
    )
    return client


# 向ds发送生成请求
def ds_requests(
    txt_file_path: str,
    skill_name: str | None = None,
    model: str = "deepseek-v4-flash",
    client: OpenAI = None,
    console_output: Callable[[str], None] = print,
) -> str | None:
    from src.llm.prompt import load_skill_prompt

    transcript = Path(txt_file_path).read_text(encoding="utf-8")

    # 通过前面传过来的checkbox状态来决定是否调用skill.md
    if skill_name is not None:
        system_prompt = load_skill_prompt(skill_name, console_output=console_output)
    else:
        system_prompt = ""

    console_output("正在请求Deepseek...")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": transcript},
            ],
            stream=False,
            reasoning_effort="high",
            extra_body={"thinking": {"type": "enabled"}}
        )
    except AuthenticationError:
        return _report_error("API Key 无效或已失效，请检查 Deepseek API Key 是否正确。", console_output)
    except RateLimitError:
        return _report_error("请求过于频繁，已触发 Deepseek 限流，请稍后再试。", console_output)
    except APIStatusError as e:
        # 根据 HTTP 状态码给出更具体的中文提示
        if e.status_code == 402:
            return _report_error("Deepseek 账户余额不足，请前往 Deepseek 开放平台充值后再试。", console_output)
        if e.status_code in (401, 403):
            return _report_error("API Key 无权访问，请检查 Deepseek API Key 是否正确。", console_output)
        if e.status_code >= 500:
            return _report_error(f"Deepseek 服务器异常（状态码 {e.status_code}），请稍后再试。", console_output)
        return _report_error(f"Deepseek 请求失败（状态码 {e.status_code}），请稍后再试。", console_output)
    except APITimeoutError:
        return _report_error("请求 Deepseek 超时，请检查网络后重试。", console_output)
    except APIConnectionError:
        return _report_error("无法连接到 Deepseek 服务器，请检查网络连接。", console_output)
    except Exception as e:
        return _report_error(f"生成会议纪要时发生未知错误：{e}", console_output)

    return response.choices[0].message.content


# 统一的错误上报：同时写入日志和控制台（QTextEdit）
def _report_error(message: str, console_output: Callable[[str], None]) -> None:
    log.error(message)
    console_output(message)
    return None
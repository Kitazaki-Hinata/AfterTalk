'''
封装deepseek API的调用
选择deepseek模型，接受deepseek返回的内容
'''

from pathlib import Path
from typing import Callable
from openai import OpenAI


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
    # response = client.chat.completions.create(
    #     model=model,
    #     messages=[
    #         {"role": "system", "content": system_prompt},
    #         {"role": "user", "content": transcript},
    #     ],
    #     stream=False,
    #     reasoning_effort="high",
    #     extra_body={"thinking": {"type": "enabled"}}
    # )
    # return response.choices[0].message.content
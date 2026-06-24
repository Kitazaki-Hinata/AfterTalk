<p align="center">
</p>
<h2 align="center">AfterTalk：AI + minutes</h2>
  <h5 align="center">基于本地模型 + Deepseek SDK 的会议纪要工具</h5>

----


### 一、项目目标
使用whisper cpp模型将会议录音转换为会议底稿（transcript），再通过 Deepseek SDK 对 transcript 进行整理与生成结构化会议纪要。音频输入支持：实时录音或上传已有音频文件（wav/mp3 等）。

### 二、主要功能
- 本地录音并保存为标准音频文件（wav/mp3）。
- 使用本地whisper模型将音频转写为文本（transcript）。
- 将 transcript 传给 Deepseek SDK，生成结构化会议纪要并回传给 GUI 展示或导出。

### 三、环境与依赖安装（推荐流程）
1. 使用 Python 3.12 解释器：[点击跳转到download页面](https://www.python.org/downloads/release/python-3120/)
2. 在终端中运行 `uv` 来下载并安装项目依赖（项目已配置 `uv` 安装脚本）。

   - 示例（在项目根目录的终端中，**逐条输入运行**）：

   ```powershell
   pip install uv
   ```
   ```powershell
   uv sync
   ```

3. 按 Deepseek 官方文档安装，充值token并配置 Deepseek SDK（包含 API Key/认证信息）[点击跳转到deepseek页面](https://platform.deepseek.com/usage。)   

![示例图片](resource/pictures/deepseek.png "示例图片")

4. 在根目录创建一个文件，命名为```.env```，然后使用文本文档的方式打开文件，将引号内字符替换为第三步中deepseek提供的API key：
    ```env
    DEEPSEEK_API = "sk-Enter-The-API-Key-Here"
    ```
![示例图片](resource/pictures/envfile_screenshot.png "示例图片")

5. 下载本地whisper语音识别模型，然后将模型放在```resource/model```文件夹当中。 
- [夸克网盘链接，提取码：sT8v](https://pan.quark.cn/s/7a425a06541b)
- [百度网盘链接，提取码：hjpw](https://pan.baidu.com/s/1b-unetzLQpe1Qspj_bg9_A)

6. 可以选择自定义Deepseek提示词模板，请修改```resource/skill/skill.md```文件。注意不要删除特殊符号，比如“#”等。

7. 运行```main.py```,
   - 在项目根目录的终端中：
    ```powershell
    python main.py
    ```

### 四、项目架构
<details>
  <summary>点击查看详情</summary>

```
meeting-minutes-ai/
├── main.py                       # 程序入口：启动 GUI
├── pyproject.toml
├── uv.lock
├── .env                          # DEEPSEEK_API 等密钥存储文件
├── logs
├── src/
│   │
│   ├── config/                   # ── 配置层 ──
│   │   ├── settings.py           # 加载 .env、全局配置（模型路径、采样率等）
│   │   └── paths.py              # 集中管理路径常量
│   │
│   ├── audio/                    # ── 音频模块 ──
│   │   ├── recorder.py           # 实时录音
│   │   ├── loader.py             # 加载/校验已有 wav/mp3 文件
│   │   └── converter.py          # 格式转换、重采样(给 ASR 喂标准输入)
│   │
│   ├── whisper/                      # ASR 模型
│   │   └── whisper.py          # 本地模型实现(读取 resource/model/)
│   │
│   ├── llm/                      # ── Deepseek 接入层 ──
│   │   ├── llm_client.py         # Deepseek SDK 客户端封装(重试、超时、错误处理)
│   │   └── prompt.py             # 读取 resource/skill/*.md 构建 system prompt
│   │
│   ├── gui/     
│   │   ├── ui_main.py                  
│   │   ├── ui_function.py               
│   │   └── ui_mainwindow.py        # 主窗口
│   │
│   └── utils/                    # ── 通用工具 ──
│       ├── logger.py             # 统一日志(写到 output/ 或 logs/)
│       └── file_utils.py         # 时间戳文件名、文件清理等
│
├── resource/
│   ├── model/                    # 本地 ASR 模型权重
│   ├── skill/                    # 给 Deepseek 的提示词模板(md)
│   │   └── skill.md
│   └── pictures/
│
└── output/
    ├── recordings/               # 原始音频
    ├── transcript/               # ASR 生成的底稿
    └── minutes/                  # 最终会议纪要
```

</details>
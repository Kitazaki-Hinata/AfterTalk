<p align="center">
</p>
<h2 align="center">AfterTalk：AI + minutes</h2>
  <h5 align="center">基于本地模型 + Deepseek SDK 的会议纪要工具</p>

----


### 一、项目目标
使用本地语音识别（ASR）模型将会议录音转换为会议底稿（transcript），再通过 Deepseek SDK 对 transcript 进行整理与生成结构化会议纪要。音频输入支持：实时录音或上传已有音频文件（wav/mp3 等）。

### 二、主要功能
- 本地录音并保存为标准音频文件（wav/mp3）。
- 使用本地 ASR 模型将音频转写为文本（transcript）。
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

5. [！！！等待添加！！！点击跳转到网盘链接]()，下载本地语音识别模型，然后将模型放在```resource/model```文件夹当中。

6. 可以在```resource/skill```文件夹当中存放传送给Deepseek的有关会议纪要的写法与注意事项。推荐使用Markdown格式。

7. 运行```main.py```,
   - 在项目根目录的终端中：
    ```powershell
    python main.py
    ```

### 四、项目架构
```
meeting-minutes-ai/
├── main.py                       # 程序入口：启动 GUI
├── pyproject.toml
├── uv.lock
├── .env                          # DEEPSEEK_API 等密钥存储文件
├── src/
│   │
│   ├── config/                   # ── 配置层 ──
│   │   ├── settings.py           # 加载 .env、全局配置（模型路径、采样率等）
│   │   └── paths.py              # 集中管理 resource/、output/ 等路径常量
│   │
│   ├── core/                     # ── 业务编排层 ──
│   │   ├── pipeline.py           # 串联：音频 → 转写 → 纪要 的主流程
│   │   └── events.py             # 进度/状态事件（供 GUI 订阅，解耦 UI 与逻辑）
│   │
│   ├── audio/                    # ── 音频模块 ──
│   │   ├── recorder.py           # 实时录音（如 sounddevice / pyaudio）
│   │   ├── loader.py             # 加载/校验已有 wav/mp3 文件
│   │   └── converter.py          # 格式转换、重采样(给 ASR 喂标准输入)
│   │
│   ├── asr/                      # ── 语音识别层 ──
│   │   ├── base.py               # ASRBase 抽象类：transcribe(audio_path) -> str
│   │   └── local_asr.py          # 本地模型实现(读取 resource/model/)
│   │
│   ├── llm/                      # ── Deepseek 接入层 ──
│   │   ├── llm_client.py         # Deepseek SDK 客户端封装(重试、超时、错误处理)
│   │   ├── prompt.py             # 读取 resource/skill/*.md 构建 system prompt
│   │   └── schema.py             # pydantic，将AI可能传回不同格式的回答统一成同一个格式
│   │
│   ├── minutes/                  # ── 会议纪要业务 ──
│   │   ├── generator.py          # 调用 llm 生成纪要、做后处理
│   │   └── exporter.py           # 导出 .md / .docx / .txt
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
│   │   └── example.md
│   └── pictures/
│
└── output/
    ├── recordings/               # 原始音频
    ├── transcript/               # ASR 生成的底稿
    └── minutes/                  # 最终会议纪要
```
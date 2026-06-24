# 👽️ AI Chat – AI 聊天助手

一个基于 **Streamlit** 和 **Ollama** 本地大模型的轻量级聊天应用，模拟温柔贴心的闺蜜好友，提供自然、亲切的对话体验。

## ✨ 功能特点
- 💬 **闺蜜人设对话** – 内置系统提示，AI 以温柔贴心的闺蜜身份与用户聊天，风格自然、情绪同步。
- 🧠 **本地模型支持** – 通过 Ollama 调用 `qwen2.5:1.5b` 等本地模型，无需联网，隐私安全（可自行查阅资料进行配置其他模型）。
- 📚 **会话管理** – 自动保存/加载聊天记录，支持**新建会话**、**删除会话**、**历史会话列表**。
- 🎨 **个性化设置** – 侧边栏可自定义 AI 的**名字**和**性格描述**，即刻生效。
- 🌊 **流式输出** – 实时显示 AI 逐字回复，交互反馈更流畅。
- 🌈 **美观界面** – 渐变色标题、欢迎页、清新配色，提升使用愉悦感。

## 🛠️ 技术栈
- **前端/UI**：Streamlit
- **大模型接口**：OpenAI SDK（兼容 Ollama 的 API）
- **本地推理引擎**：Ollama
- **语言**：Python 3.9+
- **数据存储**：JSON 文件（`sessions/` 目录）

## 📁 文件结构project
- `app.py` – 主程序（UI布局、交互逻辑）
- `session_utils.py` – 会话管理（创建、保存、加载、删除）
- `config.py` – 系统提示模板（system_prompt）
- `logo.png` – 应用 Logo（可选）
- `sessions/` – 自动生成，存放会话 JSON 文件

🚀 安装与运行
1. 克隆仓库
bash
git clone https://github.com/your-username/ai-chat.git
cd ai-chat
2. 安装依赖
bash
pip install streamlit openai
3. 安装并启动 Ollama
下载 Ollama 并安装。

拉取模型（示例使用 qwen2.5:1.5b）：

bash
ollama pull qwen2.5:1.5b
确保 Ollama 服务运行中（默认 http://localhost:11434）。

4. 运行应用
bash
streamlit run app.py
浏览器将自动打开 http://localhost:8501。

---

## 🖥️ 使用说明

- **首次启动**：页面展示欢迎界面，直接在底部输入框发送消息即可开始对话。
- **修改 AI 人设**：在左侧边栏的 **Set Messages** 区域，可修改 AI 的昵称和性格描述（如“活泼开朗”、“温柔细腻”等），AI 会立即按新设定回复。
- **会话管理**：
  - 点击 **New Session** 清空当前聊天并创建新会话（旧会话自动保存）。
  - 左侧 **Session History** 列出所有历史会话，点击即可加载。
  - 点击会话旁的 ❌ 按钮可删除该会话。
- **数据存储**：所有会话以 JSON 格式保存在 `sessions/` 文件夹中，便于备份或迁移。


## ⚙️ 自定义与扩展

- **更换模型**：在 `app.py` 中修改 `model="qwen2.5:1.5b"` 为其他已下载的 Ollama 模型名称。
- **调整系统提示**：编辑 `config.py` 中的 `system_prompt`，改变 AI 人设或对话规则。
- **更换 Logo**：将 `logo.png` 替换为自己的图片，或注释掉 `st.logo()` 行。

⚠️ 注意事项

- **必须使用 `streamlit run` 启动**，不要直接用 `python app.py`，否则会因缺少 Streamlit 上下文而报错。
- 确保 Ollama 服务在运行，且 `base_url` 地址正确（默认 `http://localhost:11434/v1`）。
- 若会话加载出现错误，可能是旧版本遗留的 `nick_name` 字段问题，本版本已兼容处理。

## 🤝 贡献
欢迎提交 Issue 或 Pull Request，帮助优化项目，提升为复杂高级大项目！

## 📧 联系
如有问题，请通过 GitHub Issues 联系，或直接 Fork 本项目进行修改。

---

**Enjoy your chat with AI Friend！🌷**

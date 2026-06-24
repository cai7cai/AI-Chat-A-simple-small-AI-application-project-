# 👽️ AI Chat – AI Chat Assistant

A lightweight chat application based on **Streamlit** and **Ollama** local large language models, simulating a warm and caring best friend to provide natural and friendly conversations.
<img width="2858" height="1624" alt="image" src="https://github.com/user-attachments/assets/138bbd02-a98a-4748-aca0-a9289ad3e7b7" />

---

## ✨ Features

- 💬 **Best-friend persona** – Built-in system prompt makes the AI act as a gentle, caring friend, with natural responses that match the user's mood.
- 🧠 **Local model support** – Uses Ollama to run models like `qwen2.5:1.5b` locally, no internet required, privacy guaranteed (you can also configure other models by referring to documentation).
- 📚 **Session management** – Automatically saves and loads chat history; supports creating new sessions, deleting sessions, and viewing a list of past sessions.
- 🎨 **Personalization** – Customize the AI's name and personality description in the sidebar, taking effect immediately.
- 🌊 **Streaming output** – Displays AI responses word by word in real time for a smoother interaction experience.
- 🌈 **Beautiful UI** – Gradient title, welcome page, and fresh color scheme for an enjoyable experience.

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **LLM API**: OpenAI SDK (compatible with Ollama's API)
- **Local inference engine**: Ollama
- **Language**: Python 3.9+
- **Data storage**: JSON files (in `sessions/` directory)

---

## 📁 Project Structure

```
project/
├── app.py                # Main program (UI layout, interaction logic)
├── session_utils.py      # Session management (create, save, load, delete)
├── config.py             # System prompt template (system_prompt)
├── logo.png              # App logo (optional)
└── sessions/             # Auto-generated, stores session JSON files
```

---

## 🚀 Installation & Run

### 1. Clone the repository
```bash
git clone https://github.com/cai7cai/AI-Chat-A-simple-small-AI-application-project-.git
cd AI-Chat-A-simple-small-AI-application-project-
```

### 2. Install dependencies
```bash
pip install streamlit openai
```

### 3. Install and start Ollama
- Download and install [Ollama](https://ollama.com/).
- Pull a model (example uses `qwen2.5:1.5b`):
  ```bash
  ollama pull qwen2.5:1.5b
  ```
- Make sure the Ollama service is running (default `http://localhost:11434`).

### 4. Run the app
```bash
streamlit run app.py
```
Your browser will automatically open `http://localhost:8501`.

---

## 🖥️ Usage Guide

- **First launch**: You'll see a welcome page; simply type a message in the input box at the bottom to start chatting.
- **Modify AI persona**: In the sidebar under **Set Messages**, you can change the AI's name and personality description (e.g., "cheerful", "gentle and thoughtful"). The AI will immediately respond according to the new settings.
- **Session management**:
  - Click **New Session** to clear the current chat and create a new one (the old session is automatically saved).
  - The **Session History** on the left lists all past sessions; click any to load it.
  - Click the ❌ button next to a session to delete it.
- **Data storage**: All sessions are saved as JSON files in the `sessions/` folder, making it easy to back up or migrate.

---

## ⚙️ Customization & Extension

- **Change model**: In `app.py`, modify `model="qwen2.5:1.5b"` to any other Ollama model name you have downloaded.
- **Adjust system prompt**: Edit the `system_prompt` in `config.py` to change the AI's persona or conversation rules.
- **Replace Logo**: Replace `logo.png` with your own image, or comment out the `st.logo()` line.

---

## ⚠️ Notes

- **Must use `streamlit run` to start** – do not run with `python app.py`, otherwise you'll get errors due to missing Streamlit context.
- Ensure Ollama is running and the `base_url` is correct (default `http://localhost:11434/v1`).
- If you encounter session loading errors, it might be due to the legacy `nick_name` field; this version has been made compatible.

---

## 🤝 Contributing

Issues and Pull Requests are welcome to help improve this project and make it more advanced!

---

## 📧 Contact

For questions, please open an issue on GitHub, or feel free to fork and modify the project.

---

**Enjoy your chat with AI Friend！🌷**

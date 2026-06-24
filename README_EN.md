# 👽️ AI Chat – AI Chat Assistant

A lightweight chat application based on **Streamlit** and **Ollama** local large language models, simulating a warm and caring best friend to provide natural and friendly conversations.

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

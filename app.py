import streamlit as st
import json
from openai import OpenAI
from datetime import datetime

# 导入自定义模块
from session_utils import (
    generate_session_name,
    save_session,
    load_sessions,
    load_session,
    delete_session
)
from config import system_prompt

# ---------- 页面配置 ----------
st.set_page_config(
    page_title="AI Chat",
    page_icon="👽️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# ---------- 初始化状态 ----------
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'name' not in st.session_state:
    st.session_state.name = "Alice"
if 'nature' not in st.session_state:
    st.session_state.nature = "a graceful tender soul"
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

# ---------- 标题 ----------
st.markdown("""
<h1 style="
    background: linear-gradient(90deg, #2e86de, #5f27cd, #ff6b6b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 2.5rem;
    font-weight: 700;
    display: inline-block;
">AI Chat</h1>
""", unsafe_allow_html=True)

st.logo("logo.png")   # 请确保 logo.png 存在，或注释此行

# ---------- 侧边栏 ----------
with st.sidebar:
    st.subheader("AI Control Panel")

    # 新建会话
    if st.button("New Session", width="stretch", icon="🗨"):
        save_session()  # 保存当前会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()

    st.text("Session History")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])
        with col1:
            if st.button(
                session,
                width="stretch",
                icon="💩",
                key=f"load_{session}",
                type="primary" if session == st.session_state.current_session else "secondary"
            ):
                load_session(session)
                st.rerun()
        with col2:
            if st.button("", width="stretch", icon="❌", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    st.divider()
    st.subheader("Set Messages")

    name = st.text_input("✏️ name", placeholder="Please set name", value=st.session_state.name)
    if name:
        st.session_state.name = name

    nature = st.text_area("😉 nature", placeholder="Please set nature", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

# ---------- 聊天界面 ----------
if not st.session_state.messages:
    st.markdown("""
    <div style="text-align: center; padding: 60px 20px;">
        <h1 style="font-size: 48px;">👽️</h1>
        <h2 style="
        background: linear-gradient(90deg, #2ecc71, #3498db, #9b59b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 2.2rem;
    ">Welcome to AI Chat！</h2>
        <p style="color: #999;">Start a conversation by typing a message below!</p>
        <p style="color: #ccc; font-size: 14px;">💡 Tip: You can set your name and personality in the sidebar</p>
    </div>
    """, unsafe_allow_html=True)
else:
    for message in st.session_state.messages:
        st.chat_message(message["role"]).write(message["content"])

# ---------- 用户输入 & AI 回复 ----------
prompt = st.chat_input("input your message...")
if prompt:
    # 显示用户消息
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 初始化 OpenAI 客户端（本地 Ollama）
    client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")

    # 构建完整提示（系统 + 历史）
    full_prompt = system_prompt % (st.session_state.name, st.session_state.nature)

    # 调用模型（流式）
    response = client.chat.completions.create(
        model="qwen2.5:1.5b",
        messages=[{"role": "system", "content": full_prompt}, *st.session_state.messages],
        stream=True
    )

    # 流式输出
    response_placeholder = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_placeholder.chat_message("assistant").markdown(full_response + "▌")

    response_placeholder.chat_message("assistant").markdown(full_response)

    # 保存回复
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    save_session()  # 自动保存当前会话
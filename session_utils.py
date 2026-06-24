import os
import json
from datetime import datetime
import streamlit as st

def generate_session_name():
    """生成时间戳格式的会话标识"""
    return datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")

def save_session():
    """保存当前会话到 sessions/ 目录"""
    if not st.session_state.current_session:
        return
    session_data = {
        "name": st.session_state.current_session,
        "nature": st.session_state.nature,
        "current_session": st.session_state.current_session,
        "messages": st.session_state.messages
    }
    os.makedirs("sessions", exist_ok=True)
    with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

def load_sessions():
    """返回所有已保存会话的名称列表（按时间降序）"""
    session_list = []
    if os.path.exists("sessions"):
        for filename in os.listdir("sessions"):
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    session_list.sort(reverse=True)
    return session_list

def load_session(session_name):
    """加载指定会话的内容到 st.session_state"""
    try:
        path = f"sessions/{session_name}.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                st.session_state.messages = data["messages"]
                st.session_state.name = data.get("name", "Alice")      # 兼容旧数据
                st.session_state.nature = data.get("nature", "a graceful tender soul")
                st.session_state.current_session = session_name
    except Exception as e:
        st.error(f"Failed to load session: {e}")

def delete_session(session_name):
    """删除指定会话文件，并重置当前会话（如果删除的是当前会话）"""
    try:
        path = f"sessions/{session_name}.json"
        if os.path.exists(path):
            os.remove(path)
        if session_name == st.session_state.current_session:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
    except Exception as e:
        st.error(f"Failed to delete session: {e}")
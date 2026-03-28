import streamlit as st
import uuid
from datetime import datetime
from langchain_core.messages import HumanMessage
from ui_langgraph_backend import chatbot

# =========================================================
# 1️⃣ SESSION STATE INITIALIZATION (MUST BE AT TOP)
# =========================================================

if "threads" not in st.session_state:
    st.session_state["threads"] = {}

if "current_thread_id" not in st.session_state:
    thread_id = str(uuid.uuid4())
    st.session_state["threads"][thread_id] = {
        "name": f"Chat – {datetime.now().strftime('%b %d, %I:%M %p')}",
        "messages": []
    }
    st.session_state["current_thread_id"] = thread_id


# =========================================================
# 2️⃣ HELPERS
# =========================================================

def create_new_thread():
    thread_id = str(uuid.uuid4())
    st.session_state["threads"][thread_id] = {
        "name": f"Chat – {datetime.now().strftime('%b %d, %I:%M %p')}",
        "messages": []
    }
    st.session_state["current_thread_id"] = thread_id


def auto_rename_thread(thread_id, first_message):
    title = first_message.strip()[:40]
    st.session_state["threads"][thread_id]["name"] = title


# =========================================================
# 3️⃣ SIDEBAR (CHAT LIST)
# =========================================================

st.sidebar.title("🧠 LangGraph Chat")

if st.sidebar.button("➕ New Chat"):
    create_new_thread()
    st.rerun()

st.sidebar.header("My Conversations")

for tid, thread in st.session_state["threads"].items():
    if st.sidebar.button(thread["name"], key=f"thread_{tid}"):
        st.session_state["current_thread_id"] = tid
        st.rerun()


# =========================================================
# 4️⃣ LOAD CURRENT THREAD
# =========================================================

current_thread_id = st.session_state["current_thread_id"]
current_thread = st.session_state["threads"][current_thread_id]


# =========================================================
# 5️⃣ RENDER CHAT HISTORY
# =========================================================

for message in current_thread["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# =========================================================
# 6️⃣ LANGGRAPH CONFIG
# =========================================================

CONFIG = {
    "configurable": {
        "thread_id": current_thread_id
    }
}


# =========================================================
# 7️⃣ USER INPUT
# =========================================================

user_input = st.chat_input("Type your message...")

if user_input:
    # Auto rename thread on first message
    if len(current_thread["messages"]) == 0:
        auto_rename_thread(current_thread_id, user_input)

    # Store user message
    current_thread["messages"].append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # Stream assistant response
    assistant_text = ""

    with st.chat_message("assistant"):
        for message_chunk, metadata in chatbot.stream(
            {"messages": [HumanMessage(content=user_input)]},
            config=CONFIG,
            stream_mode="messages"
        ):
            if message_chunk.content:
                assistant_text += message_chunk.content
                st.write(message_chunk.content)

    # Store assistant message
    current_thread["messages"].append({
        "role": "assistant",
        "content": assistant_text
    })

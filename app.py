import streamlit as st

st.set_page_config(page_title="LangGraph Chat Application")

st.title("Chat Apps")

st.text_input("Hello")

with st.chat_message("user"):
    st.write("Hello 👋")
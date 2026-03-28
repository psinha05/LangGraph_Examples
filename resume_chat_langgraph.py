from langchain_core.messages import HumanMessage
import streamlit as st
from langgraph_backend_database import chatbot, retrieve_unique_threads 
import uuid
from datetime import datetime

# to generate thread id for each conversation

def generate_thread_id():
    thread_id = uuid.uuid4()
    return thread_id

# for the new Chat conversation 
def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(st.session_state['thread_id'])
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)


def load_conversation(thread_id):
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    return state.values.get('messages', [])
    
    


if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']= generate_thread_id()

# before db, chat_threads be [](blank), changed now after connected with Sqlite db

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_unique_threads()

add_thread(st.session_state['thread_id'])

#************************************ Side bar ****************************************

st.sidebar.title('LangGraph Chat')

if st.sidebar.button("➕ New Chat"):
    reset_chat()

st.sidebar.header('My Conversation')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id']= thread_id
        messages = load_conversation(thread_id)

        temp_messages = []

        for msg in messages:
            if isinstance(msg, HumanMessage):
                role='user'
            else:
                role='assistant'
            temp_messages.append({'role': role, 'content': msg.content})

        st.session_state['message_history'] = temp_messages


# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}

user_input = st.chat_input('Type here')

if user_input:

    # first add the message to message_history
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)



    # first add the message to message_history
    with st.chat_message("assistant"):

        ai_message = st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config= CONFIG,
                stream_mode= "messages"
            )
        )

# set the value in st.session_state for maintaining the chat history 
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})

   
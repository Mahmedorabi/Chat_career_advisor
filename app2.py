import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from utils.functions import *

# app config
st.set_page_config(page_title="Streamlit Chatbot", page_icon="🤖")
st.title("Chatbot career advisor")

# session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# conversation
for message in st.session_state.chat_history:
    if isinstance(message, AIMessage):
        with st.chat_message("AI"):
            st.write(message.content)
    elif isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.write(message.content)

upload_pdf = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])
user_query = st.chat_input("Type your message here...")
user_query2 = user_query

if upload_pdf is not None:
    text = extract_pdf_text(upload_pdf)
    if user_query:
        user_query += text

if user_query:  

    with st.chat_message("Human"):
        st.markdown(user_query2)

    # Get response and append to chat history
    response = get_response(user_query, st.session_state.chat_history)

    with st.chat_message("AI"):
        response_placeholder = st.empty()
        full_response = ""

        for response in get_response(user_query, st.session_state.chat_history):
            response_placeholder.markdown(response)
            full_response += response
            response_placeholder.markdown(full_response)

    st.session_state.chat_history.append(HumanMessage(content=user_query2))
    st.session_state.chat_history.append(AIMessage(content=response))

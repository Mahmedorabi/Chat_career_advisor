import streamlit as st
from utils.function import extract_pdf_text, read_system_prompt, get_response_from_llm

# Initialize session state for memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar for PDF upload
with st.sidebar:
    st.title("Career Advisor Chatbot")
    uploaded_file = st.file_uploader("Upload your PDF resume", type=["pdf"])
    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open("temp_resume.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("PDF uploaded successfully!")
        # Extract text from PDF
        resume_text = extract_pdf_text("temp_resume.pdf")
        st.session_state.resume_text = resume_text

# Main chat interface
st.title("Chat with Career Advisor")

# Display chat history
for interaction in st.session_state.chat_history:
    with st.chat_message("user"):
        st.write(interaction['user'])
    with st.chat_message("assistant"):
        st.write(interaction['bot'])

# User input
user_input = st.chat_input("Ask your question:")

if user_input:
    # Get system prompt
    system_prompt = read_system_prompt("utils/system_prompt.txt")
    
    # Add resume text to system prompt if available
    if "resume_text" in st.session_state:
        system_prompt += f"\n\nResume Context:\n{st.session_state.resume_text}"

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get response from LLM with streaming
    api_key = ""  # Replace with your API key
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""
        for chunk in get_response_from_llm(
            user_question=user_input,
            chat_history=st.session_state.chat_history,
            system_prompt=system_prompt,
            api_key=api_key,
            session_id="default_session",  # Unique session ID for memory
        ):
            full_response += chunk
            response_container.markdown(full_response)

    # Update chat history
    st.session_state.chat_history.append({"user": user_input, "bot": full_response})
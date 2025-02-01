from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import PyPDF2
from typing import Optional


def extract_pdf_text(file_object):
    reader = PyPDF2.PdfReader(file_object)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return str(text)

def read_system_prompt(directory):
    with open(directory, "r") as file:
        return file.read()

def get_response(user_query, chat_history):
    system_prompt = read_system_prompt("system_prompt.txt")

    template = """

    Chat history: {chat_history}

    System prompt: {system_prompt}

    User question: {user_question}

    """

    # Ensure that the PDF text is included in the prompt
    prompt = ChatPromptTemplate.from_template(template).partial(
        system_prompt=system_prompt
    )

    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    chain = prompt | llm | StrOutputParser()

    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query
    })


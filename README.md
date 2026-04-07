# Career Advisor Chatbot

An AI-powered career advisor chatbot that analyzes your CV/resume and provides personalized job recommendations. Built with **Streamlit** and **LangChain**, powered by **Meta LLaMA 3 70B** via Together AI.

---

## Features

- **PDF Resume Upload** — Upload your CV in PDF format; the app extracts and analyzes the text automatically
- **Intelligent CV Analysis** — Extracts education, work experience, skills, projects, awards, languages, and more
- **Personalized Job Recommendations** — Recommends up to 3 relevant job opportunities with clear reasoning tailored to your profile
- **Real-time Streaming** — Responses are streamed token-by-token for a smooth, interactive experience
- **Persistent Chat History** — Full multi-turn conversation memory within a session using LangChain's `RunnableWithMessageHistory`
- **Structured Output** — Consistent response format: User Profile summary + Job Recommendations with explanations

---

## Tech Stack

| Component | Technology |
|---|---|
| Frontend | [Streamlit](https://streamlit.io/) |
| LLM | Meta LLaMA 3 70B (via [Together AI](https://www.together.ai/)) |
| LLM Framework | [LangChain](https://www.langchain.com/) |
| PDF Parsing | [PyPDF2](https://pypdf2.readthedocs.io/) |
| Memory | LangChain `ChatMessageHistory` + `RunnableWithMessageHistory` |

---

## Project Structure

```
Chat_career_advisor/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── utils/
    ├── function.py         # Core logic: PDF extraction, LLM chain, streaming
    └── system_prompt.txt   # System prompt defining the AI advisor behavior
```

---

## Getting Started

### Prerequisites

- Python 3.9+
- A [Together AI](https://www.together.ai/) API key

### Installation

```bash
git clone https://github.com/Mahmedorabi/Chat_career_advisor.git
cd Chat_career_advisor

# (Optional) create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### Configuration

Open `app.py` and replace the empty `api_key` string with your Together AI API key:

```python
api_key = "your_together_ai_api_key_here"
```

### Run the App

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## How It Works

```
                        ┌──────────────────────────┐
  User uploads PDF  ──▶ │  PyPDF2 Text Extraction  │
                        └────────────┬─────────────┘
                                     │ resume text
                                     ▼
                        ┌──────────────────────────┐
  User asks question ──▶│   ChatPromptTemplate     │
                        │ (system + history + user) │
                        └────────────┬─────────────┘
                                     │
                                     ▼
                        ┌──────────────────────────┐
                        │  ChatTogether LLaMA 3 70B│
                        │     (streaming=True)      │
                        └────────────┬─────────────┘
                                     │ streamed chunks
                                     ▼
                        ┌──────────────────────────┐
                        │  RunnableWithMessageHistory│
                        │   (session memory)        │
                        └────────────┬─────────────┘
                                     │
                                     ▼
                           Streamlit Chat UI
```

1. **Upload Resume** — Sidebar accepts PDF files; text is extracted and stored in session state.
2. **Context Injection** — Extracted resume text is appended to the system prompt before each call.
3. **Chat** — User messages are routed through a LangChain chain with full conversation history.
4. **Streaming** — Responses are yielded chunk-by-chunk and rendered incrementally in the UI.

---

## Example Interaction

```
User:  [Uploads resume PDF]
       What jobs are suitable for me?

AI:    Based on your resume, here is your profile:
       - Name: Ahmed Mohamed
       - Education: B.Sc. Computer Science, Cairo University
       - Experience: 2 years as a Python Developer at XYZ Corp
       - Skills: Python, Machine Learning, SQL, TensorFlow

       Recommended Jobs:
       1. Data Scientist
          Reason: Your ML experience and Python skills directly align with this role.
       2. ML Engineer
          Reason: TensorFlow proficiency and project history make you a strong candidate.
       3. AI Research Analyst
          Reason: Your academic background positions you well for research-oriented roles.
```

---

## Dependencies

```
langchain
langchain-community
langchain-core
langchain-together
PyPDF2
streamlit
```

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or suggestions, open an issue or reach out via [GitHub](https://github.com/Mahmedorabi).

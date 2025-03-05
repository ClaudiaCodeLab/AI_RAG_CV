# CV RAG Assistant

A conversational AI assistant built with LangChain and Streamlit that answers questions about Claudia's professional experience, technical skills, and personal interests using RAG (Retrieval Augmented Generation).

## 🚀 Features

- Interactive chat interface
- Context-aware responses based on CV content
- Conversation memory
- Support for various question types:
  - Professional experience
  - Technical skills
  - Personal interests
  - GitHub projects
  - Technical knowledge
  - Behavioral aspects

## 🛠️ Technology Stack

- **LangChain**: For RAG pipeline implementation
- **OpenAI**: GPT-4-turbo and text-embedding-3-small models
- **FAISS**: Vector store for efficient similarity search
- **Streamlit**: Web interface
- **Python**: Core programming language

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- Git (for cloning the repository)

## 🔧 Installation

1. Clone the repository:
```bash
git clone https://github.com/claudiacodelab/ai_rag_cv.git
cd cv-rag-assistant
```bash

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

## 🚀 Usage

1. Run the Streamlit app:
```bash
streamlit run cv_rap.py
```

2. Open your browser and navigate to the provided URL (typically http://localhost:8501)

3. Start chatting with the assistant about Claudia's professional experience!

## 📁 Project Structure

```
.
├── cv_rap.py           # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables (not in repo)
├── .gitignore         # Git ignore file
├── README.md          # Project documentation
└── cvs/               # CV content in markdown format
    ├── BehavioralQuestions.md
    ├── GitHub_Projects.md
    ├── PersonalInterests.md
    ├── Professional Profile_Work Experience.md
    └── TechnicalQA.md
```
## Additional Information
 
 If you want to personalize the chatbot with your own CV, you can do it by changing the content of the cvs folder.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for bugs or feature requests.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👩‍💻 Author

- **Claudia Jara Herrera**
  - [GitHub](https://github.com/ClaudiaCodeLab)
  - [LinkedIn](https://linkedin.com/in/claudia4jh/)
  - [Website](https://www.claudia.land/)

## 🙏 Acknowledgments

- OpenAI for providing the language models
- LangChain community for the excellent RAG tools
- Streamlit team for the amazing web framework
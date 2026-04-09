# LangChain Learning & Development Repository

A comprehensive collection of tutorials, examples, and applications demonstrating **LangChain** capabilities for building AI-powered applications. This repository covers chatbots, retrieval-augmented generation (RAG), vector databases, and API development using modern language models.

## 📚 Project Overview

This project is a hands-on learning resource that includes:

- **Chatbot Development**: Building conversational AI with memory and context awareness
- **Retrieval-Augmented Generation (RAG)**: Implementing semantic search and document-based question answering
- **Vector Databases**: Working with Chroma and FAISS for efficient similarity search
- **API Development**: Creating FastAPI servers with LangServe for deploying LLM chains
- **Multiple LLM Providers**: Integration with OpenAI, Groq, Ollama, and HuggingFace models
- **Text Processing**: Document ingestion, splitting, and embedding techniques

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- API keys for your chosen LLM providers (optional for local models like Ollama)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/langchain-learning.git
   cd langchain-learning
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

## 📁 Project Structure

```
langchain-learning/
├── notebooks/              # Jupyter notebooks with tutorials and experiments
│   ├── 1-chatbots.ipynb
│   ├── Chatbot_with_history.ipynb
│   ├── Vector_retriever.ipynb
│   ├── ChromaDB.ipynb
│   ├── Fais.ipynb
│   └── ...
├── src/                    # Production-ready Python applications
│   ├── serve.py           # FastAPI server with LangServe
│   ├── ollama_app.py      # Streamlit app with Ollama integration
│   └── openai_ollama_app.py  # Structured output with Pydantic
├── docs/                   # Documentation and reference materials
│   ├── Attention.pdf      # Research paper on attention mechanisms
│   └── knowledge.txt      # Knowledge base snippets
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🛠️ Running Applications

### Jupyter Notebooks

Explore interactive tutorials and experiments:

```bash
jupyter notebook notebooks/
```

Start with `1-chatbots.ipynb` for foundational concepts or `Chatbot_with_history.ipynb` for advanced conversation management.

### Streamlit Apps

Run interactive web applications:

```bash
# Ollama-based chatbot
streamlit run src/ollama_app.py

# OpenAI/Ollama with structured output
streamlit run src/openai_ollama_app.py
```

### FastAPI Server

Deploy LangChain chains as REST APIs:

```bash
python src/serve.py
```

The server will start at `http://localhost:8000`. Access the interactive API documentation at `http://localhost:8000/docs`.

## 📖 Key Concepts

### Chatbots with Memory

Learn how to build stateful chatbots that remember conversation history:
- Message history management
- Context preservation across turns
- Integration with various LLM providers

### Retrieval-Augmented Generation (RAG)

Implement semantic search and document-based QA:
- Document ingestion and chunking
- Embedding generation
- Vector similarity search
- Context-aware response generation

### Vector Databases

Work with modern vector storage solutions:
- **Chroma**: In-memory and persistent vector storage
- **FAISS**: Facebook's efficient similarity search library
- Embedding models from HuggingFace and OpenAI

### API Development

Create scalable LLM applications:
- FastAPI for high-performance web services
- LangServe for automatic API generation from chains
- Async support for concurrent requests

## 🔑 Environment Variables

Create a `.env` file based on `.env.example`:

```env
# Required for OpenAI models
OPENAI_API_KEY=sk-...

# Required for Groq models
GROQ_API_KEY=gsk_...

# Required for HuggingFace embeddings
HUGGINGFACEHUB_API_TOKEN=hf_...

# Optional: LangChain API for tracing
LANGCHAIN_API_KEY=lsv2_...
LANGCHAIN_TRACING_V2=true

# For local Ollama models
OLLAMA_BASE_URL=http://localhost:11434
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new notebook tutorials
- Improve existing applications
- Fix bugs or enhance documentation
- Share your LangChain experiments

## 📝 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangServe](https://github.com/langchain-ai/langserve)
- [Ollama](https://ollama.ai/)
- [Chroma](https://www.trychroma.com/)
- [FAISS](https://github.com/facebookresearch/faiss)

## ⚠️ Security Notes

- **Never commit `.env` files** with real API keys to version control
- Always use `.env.example` as a template for configuration
- Rotate API keys regularly if they are exposed
- Use environment variables for sensitive credentials in production

## 📧 Support

For questions or issues, please open a GitHub issue or contact the maintainers.

---

Happy learning! 🚀

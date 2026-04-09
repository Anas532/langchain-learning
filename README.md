# 🚀 LangChain Learning & AI Development Repository

A hands-on repository showcasing my exploration of **Large Language Models (LLMs)**, **Retrieval-Augmented Generation (RAG)**, and **AI application development** using modern tools like LangChain, FastAPI, and vector databases.

This project focuses on building real-world, end-to-end AI systems — from data ingestion to deployment — with an emphasis on practical implementation and structured workflows.

---

## 🧠 Key Concepts Explored

- **LLM Applications** – Building conversational AI systems using local and API-based models (OpenAI, Groq, Ollama, HuggingFace)
- **Retrieval-Augmented Generation (RAG)** – Semantic search with FAISS and ChromaDB for document-based question answering
- **Embeddings & Vector Databases** – Efficient similarity search, document retrieval, and embedding techniques
- **Prompt Engineering** – Controlling model behavior and response structure
- **Structured Output (Pydantic)** – Ensuring consistent and reliable LLM responses with type validation
- **API Development** – Deploying AI systems using FastAPI and LangServe for scalable web services
- **Text Processing Pipelines** – Document ingestion, chunking, cleaning, and transforming unstructured data
- **Chatbots with Memory** – Context-aware conversational AI with message history management

---

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

---

## ⚙️ Quick Start

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- API keys for your chosen LLM providers (optional for local models like Ollama)

### Installation

### 1. Clone the repository

```bash
git clone https://github.com/Anas532/langchain-learning.git
cd langchain-learning
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Add your API keys if needed (OpenAI, Groq, etc.)

---

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

---

## 📌 Highlights

- Built end-to-end RAG pipelines using FAISS and ChromaDB for semantic search
- Developed LLM-powered applications with structured JSON outputs using Pydantic
- Implemented data ingestion pipelines for unstructured documents with intelligent chunking
- Experimented with local LLMs (Ollama) and API-based models (OpenAI, Groq, HuggingFace)
- Designed modular, production-ready workflows for scalable AI applications
- Created FastAPI servers with automatic API documentation generation via LangServe

---

## 🎯 Purpose

This repository serves as:

- A **learning journal** documenting my progress in applied AI and LLM engineering
- A **portfolio** of projects demonstrating practical, production-ready LLM use cases
- A **foundation** for building scalable, enterprise-grade AI systems
- A **reference** for implementing RAG, chatbots, and vector search applications

---

## 🛠 Tech Stack

| Category | Tools & Technologies |
|----------|---------------------|
| **Languages** | Python 3.8+ |
| **Frameworks** | LangChain, FastAPI, LangServe, Streamlit |
| **Vector Databases** | Chroma, FAISS |
| **LLM Providers** | OpenAI, Groq, Ollama, HuggingFace |
| **Libraries** | Pydantic, Jupyter, NumPy, Pandas |
| **Tools** | Git, Jupyter Notebook, VS Code |
| **Concepts** | RAG, NLP, Embeddings, Vector Search, Prompt Engineering, Async Processing |

---

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

---

## ⚠️ Security Notes

- **Never commit `.env` files** with real API keys to version control
- Always use `.env.example` as a template for configuration
- Rotate API keys regularly if they are exposed
- Use environment variables for sensitive credentials in production

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add new notebook tutorials
- Improve existing applications
- Fix bugs or enhance documentation
- Share your LangChain experiments

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🔗 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [LangServe](https://github.com/langchain-ai/langserve)
- [Ollama](https://ollama.ai/)
- [Chroma](https://www.trychroma.com/)
- [FAISS](https://github.com/facebookresearch/faiss)

---

## 👤 Author

**Mohammad Anas**

- GitHub: [https://github.com/Anas532](https://github.com/Anas532)
---

Happy learning! 🚀

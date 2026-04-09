from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="langchain-learning",
    version="1.0.0",
    author="LangChain Learning Contributors",
    description="A comprehensive learning repository for LangChain with tutorials, examples, and applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/langchain-learning",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "langchain>=0.1.0",
        "langchain-core>=0.1.0",
        "langchain-community>=0.0.1",
        "langchain-groq>=0.0.1",
        "langchain-openai>=0.0.1",
        "langchain-ollama>=0.0.1",
        "langchain-chroma>=0.1.0",
        "langchain-huggingface>=0.0.1",
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "langserve>=0.0.1",
        "sse-starlette>=1.6.0",
        "python-dotenv>=1.0.0",
        "pydantic>=2.0.0",
    ],
    extras_require={
        "dev": [
            "jupyter>=1.0.0",
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
)

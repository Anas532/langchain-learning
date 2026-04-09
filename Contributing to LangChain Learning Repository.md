# Contributing to LangChain Learning Repository

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/langchain-learning.git
   cd langchain-learning
   ```
3. **Create a new branch** for your contribution:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Add your API keys to .env
   ```

## Contribution Types

### 1. Adding New Notebooks

- Place Jupyter notebooks in the `notebooks/` directory
- Use descriptive filenames (e.g., `RAG_with_custom_embeddings.ipynb`)
- Include markdown cells explaining concepts and code
- Add comments to complex code sections
- Test the notebook end-to-end before submitting

### 2. Improving Applications

- Place Python applications in the `src/` directory
- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Include error handling and validation
- Test thoroughly with different configurations

### 3. Documentation

- Update `README.md` for major changes
- Add API documentation in docstrings
- Include usage examples
- Keep documentation up-to-date with code changes

### 4. Bug Fixes

- Clearly describe the bug in your PR
- Include steps to reproduce
- Provide before/after behavior
- Add tests if applicable

## Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code
- Use meaningful variable and function names
- Keep functions focused and modular
- Add comments for non-obvious logic
- Use type hints where applicable

## Commit Messages

Write clear, descriptive commit messages:

```
[Type] Brief description

Detailed explanation of changes (if needed)

Fixes #issue_number (if applicable)
```

**Types**: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

Example:
```
feat: Add RAG pipeline with custom embeddings

Implements a new RAG example using sentence-transformers
for custom embeddings and Chroma for vector storage.

Fixes #42
```

## Pull Request Process

1. **Update your branch** with the latest main:
   ```bash
   git fetch origin
   git rebase origin/main
   ```

2. **Push your changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub with:
   - Clear title and description
   - Reference to related issues
   - Summary of changes
   - Any breaking changes or dependencies

4. **Respond to feedback** and make requested changes

## Testing

- Test your code locally before submitting
- Verify notebooks run without errors
- Check that applications handle edge cases
- Test with different LLM providers if applicable

## Security

- **Never commit API keys or secrets**
- Use `.env.example` for configuration templates
- Sanitize any sensitive data in examples
- Report security issues privately to maintainers

## Questions?

- Open an issue for questions or discussions
- Check existing issues and PRs first
- Be respectful and constructive in all interactions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉

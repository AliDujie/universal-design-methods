# Contributing to Universal Design Methods

Thank you for your interest in contributing! This skill provides a comprehensive toolkit for 100 design research methods.

## How to Contribute

### 📚 Content Contributions

- **Add new research methods**: Follow the existing method template in `references/`
- **Improve method descriptions**: Clarify usage scenarios, prerequisites, or outputs
- **Add real-world examples**: Practical case studies for each method
- **Translate content**: Help make this skill accessible in more languages

### 🔧 Code Contributions

- **Fix bugs**: Report and fix issues in the `udm/` module
- **Add features**: New query capabilities, method comparison tools
- **Improve performance**: Optimize method search and filtering
- **Add tests**: Ensure reliability of the toolkit

### 📝 Documentation

- **Improve README**: Clearer instructions, better examples
- **Add tutorials**: Step-by-step guides for specific research scenarios
- **Update references**: Keep the 100 methods current and accurate

## Development Setup

```bash
# Clone the repository
git clone https://github.com/AliDujie/universal-design-methods.git
cd universal-design-methods

# Install in development mode
pip install -e ".[dev]"

# Run tests
pytest

# Lint code
ruff check .
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit with descriptive messages
6. Push to your fork and submit a PR

## Code Style

- Follow PEP 8 guidelines
- Use type hints for new code
- Add docstrings for all public functions
- Keep line length under 100 characters

## Questions?

Open an issue or reach out to the maintainers. We welcome all contributions!

---

*By contributing, you agree that your contributions will be licensed under the MIT License.*

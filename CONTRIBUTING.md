# Contributing to Telegram File Manager Bot

First off, thank you for considering contributing to Telegram File Manager Bot! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Coding Standards](#coding-standards)
- [Testing](#testing)

## 📜 Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code:

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what is best for the community
- Show empathy towards other community members

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected behavior**
- **Actual behavior**
- **Screenshots** (if applicable)
- **Environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** - why this would be useful
- **Possible implementation** (if you have ideas)
- **Alternative solutions** considered

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Make your changes
3. Test thoroughly
4. Update documentation if needed
5. Create a pull request

## 🛠 Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Telegram account

### Setup Steps

1. **Fork and clone the repository:**

```bash
git clone https://github.com/yourusername/telegram-file-manager.git
cd telegram-file-manager
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up configuration:**

```bash
cp config.example.py config.py
# Edit config.py with your credentials
```

5. **Run the bot:**

```bash
python bot.py
```

## 🔄 Pull Request Process

1. **Update documentation** - If you add new features, update the README
2. **Follow coding standards** - See below
3. **Test your changes** - Make sure everything works
4. **Commit messages** - Use clear, descriptive commit messages
5. **Pull request description** - Explain what and why

### Commit Message Format

```
type: brief description

Detailed explanation (optional)

Fixes #issue_number (if applicable)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:
```
feat: add file search functionality
fix: resolve pagination bug on large directories
docs: update installation instructions
```

## 📝 Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and small
- Use type hints where appropriate

### Code Example

```python
def calculate_file_size(file_path: str) -> int:
    """
    Calculate the size of a file in bytes.
    
    Args:
        file_path: Path to the file
        
    Returns:
        File size in bytes
        
    Raises:
        FileNotFoundError: If file doesn't exist
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return os.path.getsize(file_path)
```

### Documentation

- Add comments for complex logic
- Update README.md for new features
- Include usage examples
- Document configuration options

## 🧪 Testing

### Manual Testing Checklist

Before submitting a PR, test:

- [ ] Bot starts without errors
- [ ] `/start` command works
- [ ] `/browse` command works
- [ ] Folder navigation works
- [ ] File download works
- [ ] Pagination works
- [ ] Progress bar displays correctly
- [ ] Error handling works
- [ ] Works on target OS (if OS-specific change)

### Test on Different Scenarios

- Empty folders
- Large folders (100+ items)
- Files with special characters
- Large files (close to 2GB)
- Permission-denied folders
- Non-existent paths

## 🎨 Feature Development Guidelines

### Adding New Features

1. **Discuss first** - Open an issue to discuss major changes
2. **Keep it simple** - Follow the KISS principle
3. **Maintain backwards compatibility** - Don't break existing functionality
4. **Add configuration options** - Make features customizable
5. **Document thoroughly** - Update README and code comments

### Feature Ideas Welcome

- File/folder deletion
- File search
- Multiple file selection
- Upload from Telegram
- File preview
- And more!

## 🐛 Bug Fix Guidelines

1. **Reproduce the bug** - Make sure you can reproduce it
2. **Identify the cause** - Debug and find the root cause
3. **Fix minimally** - Make the smallest change needed
4. **Test thoroughly** - Ensure the fix works and doesn't break anything
5. **Add comments** - Explain why the fix works

## 📚 Documentation

Help improve documentation:

- Fix typos and grammar
- Add examples
- Clarify confusing sections
- Add translations
- Create tutorials

## 🌍 Translations

Want to translate the bot to your language? Great!

1. Create a new file: `lang/your_language.py`
2. Translate all strings
3. Add language selection option
4. Update README

## ❓ Questions?

- **General questions:** Open a [Discussion](https://github.com/yourusername/telegram-file-manager/discussions)
- **Bug reports:** Open an [Issue](https://github.com/yourusername/telegram-file-manager/issues)
- **Security issues:** Email directly (see README for contact)

## 🙏 Recognition

Contributors will be:
- Listed in README.md
- Mentioned in release notes
- Given credit in code comments (for major contributions)

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🎉

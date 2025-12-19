# 🤝 Contributing to Loom

Welcome to **Loom**! We're thrilled you're interested in contributing to this educational static site generator. Whether you're a first-time open-source contributor or a seasoned developer, there's a place for you here.

---

## 🎉 Welcome, Contributors!

Whether you're a seasoned developer or just getting started, we're excited to have you here. Loom is growing, and with the right contributions, it has the potential to become a production-grade tool.

We welcome contributors of all backgrounds:

- **Students** exploring parsers and data structures
- **Bootcamp graduates** seeking real-world project experience
- **Self-taught developers** looking to build their open-source portfolio
- **Experienced engineers** who want to help shape a zero-dependency SSG

**Every contribution matters** — from fixing typos to implementing major features.

---

## 🛠️ Environment Setup

### Prerequisites

| Requirement | Version | Check Command |
|-------------|---------|---------------|
| Python | 3.12+ | `python3 --version` |
| Git | Any recent | `git --version` |

### Platform Support

- ✅ **Linux** — Native support
- ✅ **macOS** — Native support  
- ✅ **Windows** — Use WSL (Windows Subsystem for Linux)

### Getting Started

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR-USERNAME/loom.git
cd loom

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Verify your setup
./test.sh
```

> **No dependencies required!** Loom is zero-dependency by design.

---

## 🧪 Testing Strategy

### Running Tests

```bash
# Run all tests
./test.sh

# Or use unittest directly
python3 -m unittest discover -s src

# Run a specific test file
python3 -m unittest src.test_inline

# Run a specific test case
python3 -m unittest src.test_inline.TestInline.test_split_nodes_delimiter
```

### Understanding Test Results

Tests live alongside the source code in `src/`:
- `test_block.py` — Block parsing tests
- `test_inline.py` — Inline parsing tests
- `test_htmlnode.py` — HTML node tests
- `test_leafnode.py` — Leaf node tests
- `test_parentnode.py` — Parent node tests
- `test_textnode.py` — Text node tests

> [!IMPORTANT]
> **Some existing tests may be broken or have incorrect assertions!**
> 
> Fixing these tests is a **valid and valuable contribution**. If you find a failing test:
> 1. Determine if the **test** is wrong, or if the **code** is wrong
> 2. Fix whichever is incorrect
> 3. Document your reasoning in the PR

### Test Requirements

| Contribution Type | Test Expectation |
|-------------------|------------------|
| **New feature** | Must include new tests covering the feature |
| **Bug fix** | Should add a test that catches the bug |
| **Refactoring** | Existing tests should still pass |
| **Modifying tests** | Only allowed if the test is **incorrect** — not to make your code pass |

> [!CAUTION]
> **Do not modify existing tests just to make your code pass.** Tests should only be changed if they have incorrect assertions or don't align with the expected behavior. If you believe a test is wrong, explain your reasoning in the PR.

---

## 📝 Style Guide

### Python Conventions

We follow [PEP 8](https://peps.python.org/pep-0008/) with a few emphases:

```python
# ✅ Good: Pure functions when possible
def markdown_to_blocks(markdown: str) -> List[str]:
    blocks = markdown.split("\n\n")
    return [block.strip() for block in blocks if block.strip()]

# ✅ Good: Type hints
def extract_title(markdown: str) -> str:
    ...

# ✅ Good: Descriptive names
def block_to_block_type(markdown: str) -> BlockType:
    ...

# ❌ Avoid: Side effects in parsing functions
# ❌ Avoid: Global state
```

### Key Principles

1. **Keep functions pure** — Given the same input, return the same output
2. **Use type hints** — Help others understand your code
3. **Write docstrings** — Explain *why*, not just *what*
4. **Keep it simple** — This is an educational project; clarity > cleverness

### Code Formatting

```bash
# We recommend using a formatter (not required, but helpful)
# Example with black (if you have it installed):
python3 -m black src/
```

---

## 🔄 Pull Request Process

### Before Submitting

Use this checklist:

- [ ] **Tested locally** — Run `./test.sh` and ensure tests pass
- [ ] **Added tests** — New features/bug fixes must include corresponding tests
- [ ] **No new warnings** — Check for any Python warnings
- [ ] **Code formatted** — Follow PEP 8 conventions
- [ ] **Descriptive commits** — Write meaningful commit messages

### PR Template

When opening a PR, please include:

```markdown
## Description
[What does this PR do?]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Test fix/improvement
- [ ] Documentation update

## Testing
[How did you test this change?]

## Related Issues
Closes #[issue number]
```

### Review Process

1. Submit your PR with a clear description
2. A maintainer will review within a few days
3. Address any feedback (we're friendly, we promise!)
4. Once approved, your PR will be merged 🎉

---

## 💡 Finding Issues to Work On

### Good First Issues

Check out our GitHub Issues for beginner-friendly tasks:

| Issue | Difficulty | Skills |
|-------|------------|--------|
| Fix Nested Inline Parsing | 🟡 Medium | Regex, Recursion |
| Relax Block Parsing | 🟢 Easy-Medium | Regex |
| Implement Table Support | 🟡 Medium | Parsing, Classes |
| Audit Unit Tests | 🟢 Easy | Testing, Debugging |

### Creating Your Own Issues

Found a bug or have an idea? Open an issue with:
- Clear title
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Any relevant code snippets

### How to Claim an Issue

1. **Comment on the GitHub issue** — Let others know you're working on it
2. **Fork the repository** — Create your own copy
3. **Create a branch** — `git checkout -b fix/issue-name`
4. **Make your changes** — Follow the hints and resources
5. **Test thoroughly** — Run `./test.sh`
6. **Submit a PR** — Reference the issue number

---

## ❓ Getting Help

Stuck? Here's how to get support:

1. **Check existing issues** — Your question may already be answered
2. **Open a discussion** — Ask questions in GitHub Discussions
3. **Join our Discord** — Reach out to the maintainer directly on our Discord server
4. **Read the code** — Loom is small; diving in is encouraged!

---

## 🙏 Code of Conduct

Be kind, be respectful, be inclusive. We're all here to learn.

- Welcome newcomers warmly
- Provide constructive feedback
- Assume good intentions
- Celebrate contributions of all sizes

---

<div align="center">

**Thank you for contributing to Loom! 🧵**

*Every PR makes this project better for learners everywhere.*

</div>

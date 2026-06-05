# Auto-PR-Reviewer Agent 🤖

An AI-powered GitHub bot that automatically reviews Pull Requests for bugs, security vulnerabilities, and code quality issues.

## 🚀 How it works
1. Triggered on Pull Requests.
2. Uses Groq/LLM to analyze the "diff" of the changes.
3. Posts a detailed code review directly back to the GitHub PR.

## 🛠 Tech Stack
- **Python**
- **LangChain** (AI Framework)
- **Groq API** (Llama 3.3 Model)
- **GitHub API** (via GitHubKit)

## 📋 Installation
1. Clone the repo.
2. Setup your `.env` with `GITHUB_TOKEN` and `GROQ_API_KEY`.
3. Run `python auto_review.py`.
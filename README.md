# 🤖 Commit Genie: The CLI That Writes Your Commits

> **Stop writing "wip", "fix", or "updates" today.** Let AI analyze your code and write the perfect commit message while you sip your coffee.

![PyPI - Downloads](https://img.shields.io/pypi/dm/commit-genie) ![PyPI - Version](https://img.shields.io/pypi/v/commit-genie) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![AI](https://img.shields.io/badge/Powered%20By-Gemini%20Flash-orange) ![License](https://img.shields.io/badge/License-MIT-green)


---

## ⚡ Why Use This?

You just spent 3 hours debugging a race condition. The last thing you want to do is summarize 15 files of changes into a string of text. 

**AI Commit** reads your staged changes, understands the context, and generates a structured, meaningful commit message instantly.

* **✨ Intelligent:** Distinguishes between a `feat`, `fix`, and `chore`.
* **🎭 Chameleon Mode:** Switch tones from **"Hardcore Developer"** (technical jargon) to **"Project Manager"** (business value) instantly.
* **📏 Strict or Casual:** Enforce **Conventional Commits** for your repo, or use natural language for personal projects.

---

## 📦 Installation

### Prerequisites
* Python 3.8+
* Git
* A [Google Gemini API Key](https://aistudio.google.com/app/apikey) (**It's free!**)

### Get Started

1.  **Install:**
    ```bash
    pip install commit-genie
    ```
    > Or use pipx.  Use pip3 if you are on Mac/Linux

    >💡 Tip: To update to the latest version later, just run: 

    ```pip install --upgrade commit-genie ```


2.  **Configure your Key:**
    ```bash
    commit-genie config --key "YOUR_GEMINI_API_KEY"
    ```
    > **💡 Tip:** If you skip step 3, don't worry! The first time you run `commit-genie commit`, the tool will detect the missing key and ask you to paste it securely.

---

## 🚀 Usage

### The "I'm Feeling Lucky" Workflow
Stage your files and let the AI do the rest.

```bash
git add .
commit-genie commit
```
The tool will generate a message, show you a preview, and ask for confirmation before committing.

---

## 🎛️ Power User Controls
Don't like the default output? Override everything on the fly.

| Flag      | Description                       | Example                    | Available Options                         |
|-----------|-----------------------------------|----------------------------|-------------------------------------------|
| `--type`  | Force a specific commit type      | `--type fix`               | `feat`, `fix`, `docs`, `chore`, `refactor`, etc. |
| `--tone`  | Change the AI persona             | `--tone manager`           | `developer` (default), `manager`          |
| `--style` | Change the message format         | `--style natural`          | `conventional` (default), `natural`       |
| `--model` | Use a smarter/different model     | `--model gemini-2.5-pro`   | `gemini-2.5-flash`,  `gemini-2.5-pro`      |
| `--auto`  | YOLO Mode: Commit without asking  | `--auto`                   | —                                         |


## 🎭 The "Persona" Feature

This is where the magic happens. You can configure **commit-genie** to sound exactly how you need it to.


### 👨‍💻 Tone: Developer (Default)
Focuses on technical implementation details, function names, and logic.

**Message:**  ``` feat(auth): implement JWT validation in middleware ```

### 👔 Tone: Manager
Focuses on user impact, business value, and high-level summaries.

**Message:** ``` feat(auth): enable secure user login to improve system safety ```

<br>

**Try it:**

    
    commit-genie commit --tone manager
    

---

## ⚙️ Configuration
Set it and forget it. Your preferences are saved globally in ~/.commit-genie-config.json.

Set your favorite model: ``` commit-genie config --model gemini-2.5 ```

Set your default style: ``` commit-genie config --style conventional ```


---

## 📂 Project Structure
If you want to hack on the source code, here is how the magic is organized:

```bash
.
├── setup.py             # The installer
└── commit_genie/           # The brains
    ├── cli.py           # Command line interface (Click)
    ├── model.py         # The "Mega Prompt" & Logic
    ├── git_reader.py    # Reads your staged diffs
    └── config.py        # Manages your API keys/settings
```

---

## 🤝 Contributing
Got a better prompt? A new persona?

1. Fork the Project

2. Create your Feature Branch (git checkout -b feature/AmazingFeature)

3. Commit your Changes (commit-genie commit) — See what I did there?

4. Push to the Branch (git push origin feature/AmazingFeature)

5. Open a Pull Request

---

## 🔮 Future Scope

We are just getting started! Here is what we are planning for v2.0:

*   **🧠 Multi-LLM Support:** Add support for OpenAI (GPT-4), Anthropic (Claude), and local Ollama models for privacy-focused users.
*   **📜 Auto-Changelog:** Automatically generate a `CHANGELOG.md` file based on your commit history.
*   **🌍 Multi-Language:** Generate commit messages in languages other than English (Spanish, French, Chinese, etc.).
*   **🖥️ GUI Mode:** A simple desktop app for users who prefer clicking over typing commands.
*   **🔍 pre-commit Hook Integration:** Official support for the [pre-commit](https://pre-commit.com/) framework to run checks automatically.

Have an idea? Open an [Issue](https://github.com/007-shivam/commit-genie/issues) and let's discuss it!

---

Built with ❤️ and ☕.
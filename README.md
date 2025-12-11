# AI_Agent — First AI Agent (Learning Project)

A minimal, beginner-friendly project that demonstrates how to wire a Python program to an LLM provider to build a simple "agent": send a prompt, receive a response, and handle basic errors.

This repository is intended as a learning exercise for someone building their first AI agent: it shows virtual environment setup, dependency management, environment variables for API keys, and how to switch or fallback between providers.

## What this project contains
- `main.py`: Example agent code — constructs an LLM client (Anthropic `ChatAnthropic` by default), invokes the model with a prompt, and prints the response.
- `requirements.txt`: Python dependencies used by the project.
- `README.md`: (this file) setup, run instructions, and troubleshooting tips.

## Design overview (what the agent does)
- The program loads environment variables (via `dotenv` if present).
- It constructs an LLM client object and calls `invoke(...)` with a prompt.
- The response is printed to the console. You can extend `main.py` to add reasoning loops, tools, or memory.

## Prerequisites
- Python 3.11 or newer
- Git (optional, for version control and pushing to remotes)

## Setup (PowerShell)
1. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

If PowerShell blocks activation due to ExecutionPolicy, allow signed scripts for your user and re-run activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Environment variables (API keys)
Set the API keys the session will use. Example (session-only):

```powershell
$env:ANTHROPIC_API_KEY = 'sk-...'
$env:OPENAI_API_KEY = 'sk-...'
$env:GROQ_API_KEY = 'gsk_...'
```

To persist the keys for your Windows user:

```powershell
[System.Environment]::SetEnvironmentVariable('ANTHROPIC_API_KEY','sk-...','User')
[System.Environment]::SetEnvironmentVariable('OPENAI_API_KEY','sk-...','User')
[System.Environment]::SetEnvironmentVariable('GROQ_API_KEY','gsk_...','User')
```

Do not commit API keys into the repository.

## How to run
With the virtual environment active, run:

```powershell
python .\main.py
```

You should see the model's response printed. If you're using Anthropic and receive a 400 error about credits, see Troubleshooting.

## Troubleshooting & common issues
- "Your credit balance is too low" (Anthropic 400 BadRequestError):
  - Sign in to Anthropic Console → Billing to add credits or enable billing: https://console.anthropic.com/billing
  - Alternatively, set `OPENAI_API_KEY` and switch `main.py` to `ChatOpenAI` or add a fallback.

- Activation blocked by PowerShell ExecutionPolicy: use `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.

- To check environment variables in PowerShell:

```powershell
echo $env:ANTHROPIC_API_KEY
echo $env:OPENAI_API_KEY
```

## Switching providers or adding a fallback
- To use OpenAI instead of Anthropic, edit `main.py` to use `ChatOpenAI(model="gpt-4o-mini")` and ensure `OPENAI_API_KEY` is set.
- A recommended development pattern is to catch provider-specific errors (like Anthropic billing errors) and optionally fall back to another provider if its API key is available.

## Git
Add and commit the README (example):

```powershell
git add README.md
git commit -m "Update README: project explanation and setup"
git push
```

## Next steps (learning paths)
- Extend `main.py` to implement a simple agent loop (prompt → action → observation → next prompt).
- Add tools (web search, file I/O) and let the agent call them.
- Add logging and tests for deterministic behavior.

If you want, I can patch `main.py` to add a safe fallback from Anthropic to OpenAI and include example code for that behavior.

---
Edited to include a project overview, setup steps, run instructions, and troubleshooting for a beginner learning their first AI agent.


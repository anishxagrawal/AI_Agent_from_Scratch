# AI Research Assistant

A simple Python tool that researches topics for you using Wikipedia and web search, then summarizes everything with AI.

## What it does

Ask it a question, and it will:
1. Check Wikipedia for background info
2. Search the web for current information
3. Use AI to combine everything into a clear answer
4. Let you save the results to a file

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/anishxagrawal/AI_Agent_from_Scratch.git
cd AI_Agent_from_Scratch
```

**2. Create a virtual environment**
```bash
python -m venv venv
```

**3. Activate it**

Windows (PowerShell):
```bash
.\venv\Scripts\Activate.ps1
```

Mac/Linux:
```bash
source venv/bin/activate
```

**4. Install dependencies**
```bash
pip install -r requirements.txt
```

**5. Get an API key**

Get a free Groq API key from: https://console.groq.com/keys

**6. Set your API key**

Windows (PowerShell):
```bash
$env:GROQ_API_KEY = 'your-api-key-here'
```

Mac/Linux:
```bash
export GROQ_API_KEY='your-api-key-here'
```

To make it permanent (Windows):
```bash
[System.Environment]::SetEnvironmentVariable('GROQ_API_KEY','your-key','User')
```

## How to run
```bash
python main.py
```

Then just type what you want to research:
```
What can I help you research? history of the Eiffel Tower
```

## Example
```
What can I help you research? capital of India

🔍 Step 1: Searching Wikipedia...
✅ Wikipedia found!

🔍 Step 2: Searching the web...
✅ Web search complete!

🤖 Step 3: Generating answer...

📊 RESEARCH RESULTS
================================================================
The capital of India is New Delhi. It serves as the seat of all 
three branches of the Government of India. New Delhi was officially 
declared as the capital in 1911, replacing Calcutta (now Kolkata)...

💾 Would you like to save this research? (y/n):
```

## Files

- `main.py` - Main program that runs the research workflow
- `tools.py` - Search, Wikipedia, and file-saving tools
- `requirements.txt` - Python packages needed

## Troubleshooting

**"ModuleNotFoundError"**
- Make sure your virtual environment is activated
- Run `pip install -r requirements.txt` again

**"API key not found"**
- Check that you set the `GROQ_API_KEY` environment variable
- Try: `echo $env:GROQ_API_KEY` (Windows) or `echo $GROQ_API_KEY` (Mac/Linux)

**PowerShell won't let you activate the venv**
- Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Then try activating again

**Search isn't working**
- DuckDuckGo search sometimes has rate limits
- Wait a minute and try again

## Using different AI models

The code uses Groq (free), but you can switch to:

**OpenAI** (paid but very reliable):
```python
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
```
Set: `$env:OPENAI_API_KEY = 'your-key'`

**Google Gemini** (free):
```python
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
```
Get key from: https://aistudio.google.com/app/apikey
Set: `$env:GOOGLE_API_KEY = 'your-key'`

## How it works

1. **User asks a question** → "What is quantum computing?"
2. **Wikipedia tool** → Gets background information
3. **Web search tool** → Gets current/additional info
4. **AI synthesis** → Combines everything into a clear answer
5. **Optional save** → Writes results to a text file

No complex agent frameworks - just a simple, reliable workflow.

## Tech stack

- **LangChain** - For AI and tool integration
- **Groq** - Fast, free AI inference (using Llama 3.3)
- **DuckDuckGo** - Web search
- **Wikipedia API** - Encyclopedia lookup

## Future improvements

- [ ] Add conversation history
- [ ] Support follow-up questions
- [ ] Add more sources (arXiv, news APIs)
- [ ] Export to markdown/PDF
- [ ] Add citations to sources

## License

MIT - do whatever you want with it

## Contributing

Found a bug? Have an idea? Open an issue or submit a PR!

---

Made while learning about AI agents and LangChain
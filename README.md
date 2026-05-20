# Acme Watercoolers Welcome App

This is a lightweight Dash chatbot app that uses OpenAI to act as Acme Watercoolers' welcome agent.

The app is intentionally simple:
- no database
- no scenario engine
- one editable backend prompt
- one chat interface

## What This App Does

This app is a simple AI chat experience for Acme Watercoolers.

When someone opens the app:
- they see a chatbot in the browser
- they ask questions about Acme Watercoolers
- the chatbot answers as Acme's welcome agent
- the chatbot behavior is guided by a backend prompt that can be edited

## Main Files

- `app.py`
  - the simple top-level launcher
  - run this with `python app.py` on Windows or `python3 app.py` on macOS/Linux

- `scripts/app.py`
  - the Dash web app
  - controls the chat interface shown in the browser

- `scripts/openai_client.py`
  - sends the conversation to OpenAI and returns the response

- `scripts/welcome_prompt.py`
  - the most important behavior file
  - defines what Acme Watercoolers is, who it serves, and how the assistant should respond

- `knowledge/newsletters`
  - optional reference material loaded into the prompt
  - includes a few fake Acme newsletters for demo purposes

## Running The App

Create and activate a virtual environment:

PowerShell on Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your local environment file:

```bash
cp .env.example .env
```

Then put your OpenAI key into `.env`:

```env
OPENAI_API_KEY=your_real_openai_key_here
OPENAI_MODEL=gpt-5.4
```

Start the app:

PowerShell on Windows:

```powershell
python app.py
```

macOS or Linux:

```bash
python3 app.py
```

Then open the local URL shown in Terminal, usually:

```text
http://127.0.0.1:8050/
```

## Editing The Demo

If you want to change the assistant's voice or company positioning, start with:

- `scripts/welcome_prompt.py`

If you want to change the visible page copy, title, or opening message, edit:

- `scripts/app.py`

If you want more fake company knowledge for testing, add or edit files in:

- `knowledge/newsletters`

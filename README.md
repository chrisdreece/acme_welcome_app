# Acme Watercoolers Welcome App

This is a lightweight Dash chatbot app that uses OpenAI to act as Acme Watercoolers' welcome agent.

The app is intentionally simple:
- no database
- one editable backend prompt
- one chat interface

## Start Here

This guide walks through the setup one step at a time. If Terminal, PowerShell, Git, Python, API keys, or Codex are new to you, the explanations below will give you the context you need as you go.

The goal is not to become an expert in every tool immediately. The goal is to get the app running, understand what each major piece does, and then make small changes safely.

This guide is written for both Windows and macOS users. When the commands are different, follow the Windows PowerShell version on Windows and the macOS Terminal version on macOS. When only one command is shown, it works the same way on both systems.

## What This App Does

This app is a simple AI chat experience for Acme Watercoolers.

When someone opens the app:
- they see a chatbot in the browser
- they answer a quick office-size question
- they ask questions about Acme Watercoolers
- the chatbot answers as Acme's welcome agent
- the chatbot behavior is guided by a backend prompt that can be edited

The main goal of your setup is:
- get the app running on your own computer
- confirm it works with your own OpenAI API key
- understand the main files
- then use Codex in plain English to make changes safely

## The Simple Sequence

This is the recommended order:

1. Understand the basic tools: Terminal or PowerShell, Git, cloning, Python, virtual environments, and API keys
2. Install Git if you do not already have it
3. Install Python if you do not already have it
4. Clone or download the repo
5. Set up the app locally and add your OpenAI API key
6. Test the app from the command line so you know it works
7. Install or open Codex
8. Use Codex inside this project and ask for small changes in normal English

Why this order matters:
- first you get the app running without any coding assistant involved
- then you know the local setup works
- then Codex becomes a helper for editing the app, not another mystery in the middle of setup

## Very Helpful Tip

Any time you receive an error after running a command in Terminal or PowerShell, copy the full error message and ask ChatGPT or Codex to explain it.

Try a prompt like this:

```text
I am setting up a Python Dash app. Here is the command I ran and the full error I got. Please explain what it means in beginner-friendly language and tell me what to try next.
```

Most setup errors are fixable once you can see what the error is actually saying.

## Plain-English Definitions

Before the steps, here are a few quick definitions.

### What Terminal Or PowerShell Is

Terminal and PowerShell are apps where you type commands instead of clicking buttons.

On macOS, this app is usually called `Terminal`.

On Windows, this app is often called `PowerShell` or `Windows Terminal`.

Think of it as:
- a text window for talking directly to your computer
- the place where you run setup commands
- the place where you start the app
- the place where you can later start Codex CLI

Important: Terminal or PowerShell is not the Acme app itself. It is the tool you use to launch and manage the app.

### What Git Is

`Git` is a tool for working with code projects.

For this project, the most important thing to know is:
- Git can download a copy of the project from GitHub
- Git can also track changes to files over time

You do not need to learn all of Git right now. For setup, you mainly need it so you can copy the project onto your computer.

### What "Clone The Repo" Means

A `repo` is short for `repository`, which means a project folder stored in a code host such as GitHub.

To `clone the repo` means:
- make a full copy of that project on your own computer
- so you can open it, run it, and edit it locally

After cloning, you will have a normal folder on your computer called something like `acme_welcome_app`.

### What Python Is

`Python` is the programming language this app runs on.

You do not need to write Python from scratch to use this project. You mainly need Python so your computer can run the app.

### What A Virtual Environment Is

A virtual environment is a private Python setup for one project.

This project uses a folder called `.venv` for that private setup.

That helps because:
- this app gets its own Python packages
- those packages do not get mixed with other Python projects
- setup is easier to repeat later

### What The API Key Is

The OpenAI API key is the private key that lets this app make OpenAI requests.

For this app:
- the chatbot sends the conversation to OpenAI
- OpenAI returns the assistant's reply
- the API key tells OpenAI which developer account is making the request
- usage may be billed to the OpenAI account that owns the key

Treat your API key like a password. Do not paste it into public chats, GitHub, screenshots, or shared documents.

### What The `.env` File Is

The `.env` file is a local settings file.

This app uses it for private values like:
- `OPENAI_API_KEY`
- `OPENAI_MODEL`

The `.env` file should stay on your computer. It is listed in `.gitignore`, which means Git should not track it or upload it to GitHub.

The repo includes `.env.example` instead. That file shows which settings are needed, but it uses placeholder values so it is safe to share.

## Step 1: Install Or Check Git

Purpose: make sure you have the tool that can download the project from GitHub.

Open Terminal or PowerShell, then run:

```bash
git --version
```

If Git is already installed, you will see a version number.

If Git is not installed:
- on macOS, running `git --version` may prompt you to install Apple's Command Line Tools
- on Windows, install Git from [git-scm.com](https://git-scm.com/downloads)

After installing, close and reopen Terminal or PowerShell, then run:

```bash
git --version
```

When it works, you should see a Git version number.

## Step 2: Install Or Check Python

Purpose: make sure your computer can run this Python app.

On Windows, run:

```powershell
python --version
```

On macOS, run:

```bash
python3 --version
```

If that prints a Python 3 version number, you can move to the next step.

If Python is not found, install Python 3:
- Windows: [python.org/downloads/windows](https://www.python.org/downloads/windows/)
- macOS: [python.org/downloads/macos](https://www.python.org/downloads/macos/)

After installing, close and reopen Terminal or PowerShell, then check the version again.

## Step 3: Clone Or Open The Repo

Purpose: get your own local copy of this project.

If you already have this project folder on your computer, open Terminal or PowerShell and move into that folder.

For example, on Windows:

```powershell
cd C:\Users\your-name\OneDrive\Projects\acme_welcome_app
```

For example, on macOS:

```bash
cd ~/Desktop/acme_welcome_app
```

If the project is on GitHub and you need to clone it, move to the place where you want the project folder to live.

For example, on macOS:

```bash
cd ~/Desktop
```

For example, on Windows:

```powershell
cd $HOME\Desktop
```

Then clone the repo, replacing the URL below with the real GitHub repo URL:

```bash
git clone https://github.com/example/acme_welcome_app.git
```

Now go into the project folder:

```bash
cd acme_welcome_app
```

You must be inside the project folder before running the rest of the commands in this guide.

## Step 4: Set Up Your Local App Copy

Purpose: create the local Python environment, install the required packages, and add your private API key.

### 4A. Create A Virtual Environment

On Windows, run:

```powershell
python -m venv .venv
```

On macOS, run:

```bash
python3 -m venv .venv
```

What this does:
- creates a folder called `.venv`
- gives this project its own private Python setup
- keeps this app's packages separate from other Python projects

### 4B. Activate The Virtual Environment

On Windows PowerShell, run:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS, run:

```bash
source .venv/bin/activate
```

What this does:
- tells Terminal or PowerShell to use the Python setup for this project
- makes sure install and run commands use the right Python environment

After this, your command line will usually start with `(.venv)`. That is a good sign.

### 4C. Install The Required Python Packages

Run:

```bash
pip install -r requirements.txt
```

What this does:
- reads `requirements.txt`
- installs the Python packages this app needs
- prepares the app to run locally

### 4D. Create Your Local Environment File

On Windows PowerShell, run:

```powershell
Copy-Item .env.example .env
```

On macOS, run:

```bash
cp .env.example .env
```

What this does:
- copies the sample settings file
- creates your private local config file

## Step 5: Add Your OpenAI API Key

Purpose: give the app permission to call OpenAI from your own developer account.

To get your own key:

1. Go to [OpenAI API keys](https://platform.openai.com/settings/organization/api-keys).
2. Sign in or create an OpenAI developer account.
3. Create a new API key.
4. Copy the key.

Now open your local `.env` file in a text editor.

You will see this line:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Delete only the placeholder text after the `=` sign, and paste in your real key.

After you paste it, the line should look like this pattern:

```env
OPENAI_API_KEY=sk-...
```

Do not add extra quotation marks.
Do not add spaces before or after the key.
Do not edit the `OPENAI_API_KEY=` part on the left.

Your `.env` file should look like this:

```env
OPENAI_API_KEY=your_real_openai_key_here
OPENAI_MODEL=gpt-5.4
```

Important:
- you must use your own OpenAI API key
- do not use someone else's key
- do not share your key publicly
- `.env` is ignored by Git on purpose
- `.env.example` is safe to share because it contains placeholders, not secrets

## Step 6: Test The App From The Command Line

Purpose: confirm the app runs correctly before you try making changes.

With your virtual environment still active, run the app.

On Windows:

```powershell
python app.py
```

On macOS:

```bash
python3 app.py
```

What this does:
- starts the Acme Watercoolers Welcome App on your own computer
- prints a local web address in Terminal or PowerShell
- lets you test the chatbot in your browser

You will usually see a local address like this:

```text
http://127.0.0.1:8050/
```

Open that address in your browser.

If the page loads and the chatbot appears, your local setup is working.

To stop the app, go back to Terminal or PowerShell and press:

```text
Control + C
```

This testing step matters because it proves:
- Git worked
- Python worked
- your dependencies installed
- your `.env` file is set up correctly
- the app runs before you try editing it with Codex

## Step 7: Install Or Open Codex

Purpose: use a coding assistant to inspect and edit the project with natural language.

You have two common options:
- use the Codex desktop app
- use the Codex CLI in Terminal or PowerShell

The Codex app is available for macOS and Windows. You can open the app, sign in with your ChatGPT account or an OpenAI API key, select this project folder, and ask Codex for help.

Official OpenAI docs:
- [Codex app getting started](https://developers.openai.com/codex/app#getting-started)
- [Codex CLI setup](https://developers.openai.com/codex/cli#cli-setup)

If you want to use the Codex CLI, first check whether `npm` is installed:

```bash
npm --version
```

If that prints a version number, install Codex CLI with:

```bash
npm i -g @openai/codex
```

If `npm` is not found, install Node.js first, then run the Codex install command again. `npm` comes with Node.js.

After installation, start Codex from inside the project folder:

```bash
codex
```

What this step does:
- installs or opens the coding assistant tool
- lets you sign in with your own account or key
- lets you ask for changes in plain English
- helps you inspect files before editing them

## Step 8: Use Codex Inside This Project

Purpose: ask for changes in simple English, one small change at a time.

Make sure you are inside the project folder:

```bash
cd acme_welcome_app
```

Then start Codex if you are using the CLI:

```bash
codex
```

Now you can type requests in normal language.

Examples:

```text
Please make the assistant sound warmer and more welcoming.
```

```text
Please update the Acme prompt so it asks better follow-up questions about office hydration needs.
```

```text
Please change the opening message so it sounds more polished but still playful.
```

```text
Please look for any leftover old-brand references and remove them.
```

The key idea is:
- Terminal or PowerShell is where you run commands
- Git is how you get the project onto your computer
- the local setup proves the app works
- Codex is the helper you use after that to inspect and change the project

## What The Main Pieces Of The App Are

Here is the app in plain English:

- `app.py`
  - the simple top-level launcher
- this is what you run with `python app.py` on Windows or `python3 app.py` on macOS

- `scripts/app.py`
  - the Dash web app
  - this controls the chat interface people see in the browser
  - this is where the visible title, opening message, buttons, and page styling live

- `scripts/openai_client.py`
  - the code that sends the conversation to OpenAI
  - this is where the app reads `OPENAI_API_KEY` and `OPENAI_MODEL`
  - this is where the app gets the assistant response back

- `scripts/welcome_prompt.py`
  - the most important file for behavior
  - this is where the system prompt lives
  - this is where you describe what Acme Watercoolers is, who it is for, and how the assistant should behave

- `knowledge/newsletters`
  - optional fake company reference material
  - files in this folder are loaded into the prompt
  - useful for demo content and testing how the assistant uses extra context

- `.env`
  - holds your private OpenAI API key and model name
  - this file should exist on your computer
  - this file should not be committed or shared

- `.env.example`
  - a safe example of the settings the app expects
  - this file can be committed because it does not contain a real key

- `requirements.txt`
  - lists the Python packages the app needs

## A Good Beginner Workflow

If you want a safe and simple rhythm, use this:

1. Open Terminal, PowerShell, or Codex
2. Go into the project folder
3. Activate the virtual environment
4. Run the app
5. Test the app in the browser
6. Stop the app with `Control + C`
7. Ask Codex for one small change
8. Read what changed
9. Run the app again and test the result

That pattern helps you stay grounded: run, test, change, test again.

## If Something Goes Wrong

A few common fixes:

- If `git` is not found, Git is not installed yet
- If `python` or `python3` is not found, Python is not installed or not available in Terminal or PowerShell
- If activating `.venv` fails on Windows, make sure you are using PowerShell from the project folder
- If `pip install -r requirements.txt` fails, make sure the virtual environment is active first
- If the app says the OpenAI key is missing, recheck the `.env` file
- If the app returns an authentication error, make sure the API key was copied correctly
- If `npm` is not found, install Node.js before trying to install Codex CLI
- If `codex` is not found, try the install command again after confirming `npm` works

## Summary

The simplest mental model is:

1. Use Terminal or PowerShell to run commands
2. Use Git to download the project
3. Use Python to run the app
4. Add your own OpenAI API key in `.env`
5. Test the app locally
6. Use Codex to help make small changes in plain English

The most important file for changing the assistant's behavior is:

- `scripts/welcome_prompt.py`

The most important command for testing the app locally is:

Windows:

```powershell
python app.py
```

macOS:

```bash
python3 app.py
```

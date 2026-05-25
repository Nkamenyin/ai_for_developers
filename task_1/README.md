# OpenRouter CLI Chat Client

A simple Python command-line tool for sending prompts to the OpenRouter Chat Completions API and printing responses.

This project lets you quickly query large language models from the terminal using the OpenRouter API.

---

## Features

- Send prompts directly from the command line
- Uses OpenRouter Chat Completions API
- Fully configurable via environment variables
- Lightweight and easy to run
- Returns full JSON response (or just the model output if enabled)

---

## Requirements

- Python 3.8 or higher
- OpenRouter API key: https://openrouter.ai

---

## Installation
This project uses the `requests` library to make HTTP calls to the OpenRouter API.

Clone or download this project, then install dependencies:

```bash
pip install -r requirements.txt
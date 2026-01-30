# Conversational Knowledge Bot

LangChain-powered chatbot with memory + web search.

## Features

- Conversational memory
- DuckDuckGo web search
- Contextual follow-up questions
- CLI + Streamlit UI

## Tech Stack

- Python
- LangChain
- OpenAI
- DuckDuckGo Search
- Streamlit

## Setup

```bash
git clone repo
cd conversational-bot
pip install -r requirements.txt

Run CLI

python cli.py

Run UI

streamlit run app.py

Memory Design

ConversationBufferMemory stores chat history and injects into agent.

Tools

DuckDuckGoSearchRun for factual queries.

Example

Who is CEO of OpenAI?
Where did he study?
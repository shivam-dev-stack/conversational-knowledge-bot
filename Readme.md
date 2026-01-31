#  Conversational Knowledge Bot

- External web search (DuckDuckGo)
- Extractive Question Answering (RoBERTa)
- Lightweight conversational memory
- Streamlit chat UI

Built without OpenAI or Ollama — fully CPU-based.

---

##  Features

-  Searches live web data using DuckDuckGo  
-  Extracts factual answers using HuggingFace QA model  
-  Remembers previous entity for follow-up questions (e.g., “Where did he study?”)  
-  Streamlit chat interface  
-  CLI support  
-  No paid APIs required  

---

##  Architecture

```bash
User
 ↓
Streamlit / CLI
 ↓
DuckDuckGo Search (DDGS)
 ↓
RoBERTa Question Answering Model
 ↓
Answer Extraction
 ↓
Entity Memory (for follow-ups)

```

# Tech Stack

Python 3.10+

HuggingFace Transformers

deepset/roberta-base-squad2 (QA Model)

DuckDuckGo Search (ddgs)

Streamlit

# Installation

## Create environment:
```bash
conda create -n kbot python=3.10
conda activate kbot
```


## Install dependencies:
```bash
pip install transformers torch streamlit ddgs
```

Run CLI
```bash
python cli.py
```

Run Streamlit UI
```bash
streamlit run app.py
```

Open in browser:

http://localhost:8501

### Sample Chat
```bash
User: who is ceo of tesla
Bot: Elon Musk

User: where did he study
Bot: University of Pennsylvania

User: where was he born
Bot: Pretoria
```


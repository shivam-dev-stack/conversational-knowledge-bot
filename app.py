import streamlit as st
from agent import KnowledgeBot

st.title("🧠 Conversational Knowledge Bot")

# Initialize bot once
if "bot" not in st.session_state:
    st.session_state.bot = KnowledgeBot()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask something...")

if user_input:
    # Show user
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Bot reply
    reply = st.session_state.bot.ask(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)

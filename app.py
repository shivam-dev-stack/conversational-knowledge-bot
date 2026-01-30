import streamlit as st
from agent import create_agent

st.set_page_config(page_title="Knowledge Bot")

if "agent" not in st.session_state:
    st.session_state.agent = create_agent()

st.title("🧠 Conversational Knowledge Bot")

user_input = st.chat_input("Ask something...")

if user_input:
    with st.spinner("Thinking..."):
        response = st.session_state.agent.run(user_input)

    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)

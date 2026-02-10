import streamlit as st
from groq import Groq

st.set_page_config(page_title="Groq Chat", page_icon="🤖")

st.title("🤖 Groq Chat App")

# Sidebar for API key
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Groq API Key", type="password")

if not api_key:
    st.warning("Please enter your Groq API key in the sidebar.")
    st.stop()

client = client = Groq(api_key=api_key)

# Initialize memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )
    with st.chat_message("user"):
        st.write(prompt)

    # Get response
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"Error: {e}"

    # Show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )
    with st.chat_message("assistant"):
        st.write(reply)

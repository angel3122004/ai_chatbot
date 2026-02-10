import streamlit as st
import os
from groq import Groq

# Page title
st.title("🤖 GROQ Chatbot")

# Load API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ API key not found!")
    st.stop()

client = Groq(api_key=api_key)

# User input
user_prompt = st.text_input("Ask something:")

if st.button("Send"):
    if user_prompt.strip() == "":
        st.warning("Please enter a question")
    else:
        with st.spinner("Thinking..."):
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_prompt}
                ],
                model="llama-3.3-70b-versatile",
            )

        response = chat_completion.choices[0].message.content
        st.success("Response:")
        st.write(response)

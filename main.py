import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

st.set_page_config(
    page_title="D13 new-gen AI",
    page_icon='🧠',
    layout="centered",
)

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel("gemini-2.0-flash")
def map_role(role):
    return "assistant" if role == "model" else role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    
st.title(" 🤯 Know-verge Ai chat🤖 ")


for message in st.session_state.chat_session.history:
    with st.chat_message(map_role(message.role)):
        st.markdown(message.parts[0].text)

user_input= st.chat_input("💭 Ask anything...")

if user_input:
    st.chat_message("user").markdown(user_input)
    response=st.session_state.chat_session.send_message(user_input)

    with st.chat_message("assistant"):
        st.markdown(response.text)

import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage
)

# Initialize the ChatOpenAI object
chat = ChatOpenAI(openai_api_key='0', base_url='http://10.0.1.196:1080/llm/v1', model_name="gpt-3.5-turbo",
                  temperature=0)

st.set_page_config(page_title="Welcome to ASL", layout="wide")

st.title("🤠 Welcome to ASL")

if "messages" not in st.session_state:
    st.session_state["messages"] = []


with st.container():
    st.header("Chat with GPT")

    for message in st.session_state["messages"]:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)
    prompt = st.chat_input("Type something...")
    if prompt:
        st.session_state["messages"].append(HumanMessage(content=prompt))
        with st.chat_message("user"):
            st.markdown(prompt)
        ai_message = chat([HumanMessage(content=prompt)])
        st.session_state["messages"].append(ai_message)
        with st.chat_message("assistant"):
            st.markdown(ai_message.content)

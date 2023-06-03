import streamlit as st
from langchain.llms import OpenAI

st.title('The Oracle.')
openai_api_key = st.sidebar.text_input(("OpenAI API Key"), type="password")

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What is the answer to the question of life, the universe, and everything?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter a valid OpenAI API key'
        
        )
    if (submitted and openai_api_key.startswith('sk-')):
        generate_response(text)



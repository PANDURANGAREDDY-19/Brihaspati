import streamlit as st
from components.locale import load_locale
from components.ui import render_page_header

PROVIDERS = ['Ollama', 'OpenAI', 'Gemini', 'Groq']
LANGS = ['en', 'te']


def render(locale):
    render_page_header(locale['settings']['title'], locale['settings']['subtitle'])

    col1, col2 = st.columns(2, gap='large')
    with col1:
        lang = st.selectbox(locale['settings']['language_label'], ['English','Telugu'])
        provider = st.selectbox(locale['settings']['ai_provider'], PROVIDERS)
        key = st.text_input(locale['settings']['byok'])
    with col2:
        st.markdown("<div class='card'><strong>Theme</strong></div>", unsafe_allow_html=True)

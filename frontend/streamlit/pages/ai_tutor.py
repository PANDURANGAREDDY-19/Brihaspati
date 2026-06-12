import streamlit as st
import time
from components.ui import chat_bubble, render_page_header

SUGGESTED = [
    'Explain recursion.',
    'What is OOP?',
    'How do dictionaries work?'
]
MOCK = {
    'Explain recursion.': 'Recursion solves problems by calling the same function with smaller inputs. Always include a base case.',
    'What is OOP?': 'Object-oriented programming models code with objects and classes for encapsulation.',
    'How do dictionaries work?': 'Dictionaries map keys to values using hashing for fast lookup.'
}

def render(locale):
    render_page_header(locale['ai_tutor']['title'], locale['ai_tutor']['subtitle'])

    if 'chat' not in st.session_state:
        st.session_state.chat = [{'sender': locale['ai_tutor']['ai_label'], 'text': locale['ai_tutor']['welcome'], 'ts': time.time()}]

    cols = st.columns([3,1], gap='large')
    with cols[0]:
        st.markdown("<div class='card chat-container'>", unsafe_allow_html=True)
        for msg in st.session_state.chat:
            chat_bubble(msg['sender'], msg['text'], ai=(msg['sender']==locale['ai_tutor']['ai_label']), ts=time.strftime('%H:%M', time.localtime(msg.get('ts',0))))
        st.markdown("</div>", unsafe_allow_html=True)

        with st.form('chat'):
            choice = st.selectbox(locale['ai_tutor']['language'], ['Python','JavaScript','C'])
            text = st.text_input(locale['ai_tutor']['placeholder'])
            submit = st.form_submit_button(locale['ai_tutor']['send'])
            if submit and text:
                st.session_state.chat.append({'sender': locale['ai_tutor']['user_label'], 'text': text, 'ts': time.time()})
                # mock response
                resp = MOCK.get(text, 'Great question! Here is a helpful mock response to guide your practice.')
                st.session_state.chat.append({'sender': locale['ai_tutor']['ai_label'], 'text': resp, 'ts': time.time()})
                st.experimental_rerun()

    with cols[1]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='section-title'>{locale['ai_tutor']['suggested']}</div>", unsafe_allow_html=True)
        for s in SUGGESTED:
            if st.button(s, key=s):
                st.session_state.chat.append({'sender': locale['ai_tutor']['user_label'], 'text': s, 'ts': time.time()})
                st.session_state.chat.append({'sender': locale['ai_tutor']['ai_label'], 'text': MOCK.get(s,''), 'ts': time.time()})
                st.experimental_rerun()
        st.markdown("</div>", unsafe_allow_html=True)

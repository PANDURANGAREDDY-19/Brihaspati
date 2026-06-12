import time
import streamlit as st

MOCK_REPLIES = [
    {
        'keywords': ['python', 'java', 'cplusplus', 'javascript', 'html', 'css', 'c++', 'c'],
        'text': 'I can help you explore syntax, write sample code, or compare programming topics. What would you like to practice first?',
    },
    {
        'keywords': ['grammar', 'vocabulary', 'speaking', 'writing', 'reading'],
        'text': 'Let’s build your language skills with clear examples and practice questions. Which area should we focus on?',
    },
    {
        'keywords': ['telugu', 'telugu grammar', 'spoken', 'reading'],
        'text': 'Telugu learning is fun with structured exercises. I can help you practice reading, writing, and vocabulary.',
    },
]


def ensure_chat_state(locale):
    if 'chat_open' not in st.session_state:
        st.session_state.chat_open = False
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = [
            {
                'sender': 'bot',
                'text': locale.get('chat', {}).get('welcome', "Hello! I'm CodeMentor AI. How can I help you learn Programming, English, or Telugu today?"),
                'time': time.strftime('%I:%M %p'),
            }
        ]
    if 'chat_input' not in st.session_state:
        st.session_state.chat_input = ''


def get_reply(message: str) -> str:
    lower = message.lower()
    for item in MOCK_REPLIES:
        if any(keyword in lower for keyword in item['keywords']):
            return item['text']
    return 'That sounds great. I can guide you with course recommendations, practice suggestions, and quick concept explanations. What would you like to do next?'


def submit_chat():
    text = st.session_state.chat_input.strip()
    if not text:
        return
    st.session_state.chat_messages.append({'sender': 'user', 'text': text, 'time': time.strftime('%I:%M %p')})
    reply = get_reply(text)
    st.session_state.chat_messages.append({'sender': 'bot', 'text': reply, 'time': time.strftime('%I:%M %p')})
    st.session_state.chat_input = ''


def render(locale):
    ensure_chat_state(locale)

    st.markdown('<div class="chat-shell">', unsafe_allow_html=True)
    if st.button('Chat' if not st.session_state.chat_open else 'Close', key='chat_toggle'):
        st.session_state.chat_open = not st.session_state.chat_open
        st.rerun()

    if st.session_state.chat_open:
        st.markdown(
            """
            <div class='chat-panel'>
                <div style='display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 1rem; margin-bottom: 1rem;'>
                    <div>
                        <p style='font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.24em; color: #6ee7b7; margin: 0; font-family: Inter, sans-serif;'>CodeMentor AI</p>
                        <h3 style='margin-top: 0.25rem; font-size: 1.125rem; font-weight: 600; color: #ffffff; margin-bottom: 0; font-family: Inter, sans-serif;'>AI Learning Assistant</h3>
                    </div>
                    <span style='display: inline-flex; height: 2.5rem; width: 2.5rem; align-items: center; justify-content: center; border-radius: 1rem; background: rgba(255, 255, 255, 0.05); font-size: 1.125rem;'>🤖</span>
                </div>
            """,
            unsafe_allow_html=True,
        )

        messages_html = ""
        for message in st.session_state.chat_messages:
            if message['sender'] == 'bot':
                bubble_style = "background: rgba(15, 23, 42, 0.9); border: 1px solid rgba(255, 255, 255, 0.04); margin-bottom: 0.9rem; padding: 1rem; border-radius: 1.5rem; max-width: 85%;"
                label = 'Mentor'
            else:
                bubble_style = "background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.2); color: #f1f5f9; margin-left: auto; max-width: 85%; margin-bottom: 0.9rem; padding: 1rem; border-radius: 1.5rem;"
                label = 'You'
            messages_html += f"""
            <div style='{bubble_style}'>
                <div style='font-size: 0.72rem; letter-spacing: 0.18em; text-transform: uppercase; color: rgba(148, 163, 184, 0.9); font-weight: 600;'>{label}</div>
                <div style='margin: 0.55rem 0 0; line-height: 1.6; font-size: 0.875rem;'>{message['text']}</div>
            </div>
            """
        
        st.markdown(
            f"""
            <div style='max-height: 300px; overflow-y: auto; display: flex; flex-direction: column; padding-right: 0.25rem; font-family: Inter, sans-serif;'>
                {messages_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form('chat_form'):
            st.text_input('Chat input', key='chat_input', placeholder='Ask a question or start a topic...', label_visibility='collapsed')
            st.form_submit_button('Send', on_click=submit_chat)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


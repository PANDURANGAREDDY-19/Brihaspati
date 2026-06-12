import streamlit as st
import time
import asyncio
from api_client import chat


def render(locale):
    welcome = locale.get("chat", {}).get(
        "welcome", "Hello! I'm Brihaspati, your bilingual coding assistant!"
    )

    if "chatbot_msgs" not in st.session_state:
        st.session_state.chatbot_msgs = [
            {"sender": "bot", "text": welcome, "ts": time.time()}
        ]
    if "chatbot_open" not in st.session_state:
        st.session_state.chatbot_open = False
    if "chatbot_session" not in st.session_state:
        st.session_state.chatbot_session = f"chatbot_{int(time.time())}"
    if "chatbot_input_key" not in st.session_state:
        st.session_state.chatbot_input_key = 0

    btn_label = "✕ Close" if st.session_state.chatbot_open else "💬 Chat"
    if st.button(btn_label, key="chatbot_toggle"):
        st.session_state.chatbot_open = not st.session_state.chatbot_open
        st.rerun()

    if st.session_state.chatbot_open:
        st.markdown(
            """
            <div style='position:fixed; bottom:5rem; right:1.5rem; width:360px; max-height:480px;
                background:rgba(15,23,42,0.95); border:1px solid rgba(255,255,255,0.1);
                border-radius:1rem; padding:1rem; z-index:999; overflow-y:auto;
                box-shadow:0 20px 60px rgba(0,0,0,0.5);'>
            """,
            unsafe_allow_html=True,
        )

        for msg in st.session_state.chatbot_msgs:
            is_bot = msg["sender"] == "bot"
            align = "flex-start" if is_bot else "flex-end"
            bg = "rgba(139,92,246,0.15)" if is_bot else "rgba(16,185,129,0.15)"
            label = "Mentor" if is_bot else "You"
            st.markdown(
                f"""
                <div style='display:flex; justify-content:{align}; margin-bottom:0.5rem;'>
                    <div style='background:{bg}; border-radius:0.75rem; padding:0.5rem 0.75rem; max-width:85%;'>
                        <strong style='font-size:0.7rem; color:#6ee7b7;'>{label}</strong>
                        <div style='margin-top:0.2rem; font-size:0.875rem; color:#e2e8f0;'>{msg['text']}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with st.form("chatbot_input", border=False):
            text = st.text_input(
                "Ask a question",
                placeholder="Ask a question...",
                label_visibility="collapsed",
                key=f"chatbot_input_{st.session_state.chatbot_input_key}",
            )
            if st.form_submit_button("Send", use_container_width=True):
                if text:
                    st.session_state.chatbot_msgs.append(
                        {"sender": "user", "text": text, "ts": time.time()}
                    )
                    lang_code = st.session_state.get("lang", "en")
                    try:
                        result = asyncio.run(
                            chat(text, st.session_state.chatbot_session, lang_code)
                        )
                        reply = result.get("response", "")
                    except Exception as e:
                        reply = f"Error: {e}"
                    st.session_state.chatbot_msgs.append(
                        {"sender": "bot", "text": reply, "ts": time.time()}
                    )
                    st.session_state.chatbot_input_key += 1
                    st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

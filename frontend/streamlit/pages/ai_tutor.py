import streamlit as st
import time
import asyncio
from components.ui import render_page_header
from api_client import chat

SUGGESTED = [
    "Explain recursion in Python",
    "What is object-oriented programming?",
    "How do Python dictionaries work?",
]

SESSION_KEY = "brihaspati_session_id"


def get_session_id():
    if SESSION_KEY not in st.session_state:
        st.session_state[SESSION_KEY] = f"streamlit_{int(time.time())}"
    return st.session_state[SESSION_KEY]


def _send(text: str, locale: dict):
    lang_code = st.session_state.get("lang", "en")
    ai_label = locale["ai_tutor"]["ai_label"]
    user_label = locale["ai_tutor"]["user_label"]
    st.session_state.chat.append(
        {"sender": user_label, "text": text, "ts": time.time()}
    )
    with st.spinner("Thinking…"):
        try:
            result = asyncio.run(chat(text, get_session_id(), lang_code))
            reply = result.get("response", "No response from backend.")
        except Exception as e:
            reply = f"⚠️ Error: {e}"
    st.session_state.chat.append({"sender": ai_label, "text": reply, "ts": time.time()})
    st.rerun()


def render(locale):
    render_page_header(locale["ai_tutor"]["title"], locale["ai_tutor"]["subtitle"])

    if "chat" not in st.session_state:
        st.session_state.chat = [
            {
                "sender": locale["ai_tutor"]["ai_label"],
                "text": locale["ai_tutor"]["welcome"],
                "ts": time.time(),
            }
        ]

    col_chat, col_side = st.columns([3, 1], gap="large")

    with col_chat:
        # Build complete chat history HTML in one block
        msgs_html = ""
        for msg in st.session_state.chat:
            is_ai = msg["sender"] == locale["ai_tutor"]["ai_label"]
            role = "ai" if is_ai else "user"
            avatar = "🤖" if is_ai else "🙂"
            ts = time.strftime("%H:%M", time.localtime(msg.get("ts", 0)))
            msgs_html += f"""
            <div class="msg-row {role}">
                <div class="msg-avatar {role}">{avatar}</div>
                <div class="msg-bubble {role}">
                    <div class="msg-label">{msg["sender"]}</div>
                    <div>{msg["text"]}</div>
                    <div class="msg-time">{ts}</div>
                </div>
            </div>
            """
        st.markdown(
            f"""
            <div class="chat-history">
                {msgs_html}
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("chat_form", clear_on_submit=True, border=False):
            text = st.text_input(
                locale["ai_tutor"]["placeholder"],
                placeholder=locale["ai_tutor"]["placeholder"],
                label_visibility="collapsed",
            )
            submitted = st.form_submit_button(
                locale["ai_tutor"]["send"], use_container_width=True
            )
        if submitted and text.strip():
            _send(text.strip(), locale)

    with col_side:
        st.markdown(
            f"""
            <div class="glass-panel">
                <h4 style="color:#6ee7b7;font-size:0.78rem;text-transform:uppercase;
                            letter-spacing:0.18em;margin:0 0 0.75rem;">
                    {locale["ai_tutor"]["suggested"]}
                </h4>
            </div>
            """,
            unsafe_allow_html=True,
        )
        for s in SUGGESTED:
            if st.button(s, key=f"sug_{s}", use_container_width=True):
                _send(s, locale)

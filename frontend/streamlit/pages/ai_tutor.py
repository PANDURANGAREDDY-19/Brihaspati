import streamlit as st
import time
import asyncio
from components.ui import chat_bubble, render_page_header
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
    if "tutor_input_key" not in st.session_state:
        st.session_state.tutor_input_key = 0

    cols = st.columns([3, 1], gap="large")
    with cols[0]:
        st.markdown(
            "<div class='glass-panel' style='padding:1rem; border-radius:1rem; margin-bottom:1rem;'>",
            unsafe_allow_html=True,
        )
        for msg in st.session_state.chat:
            chat_bubble(
                msg["sender"],
                msg["text"],
                ai=(msg["sender"] == locale["ai_tutor"]["ai_label"]),
                ts=time.strftime("%H:%M", time.localtime(msg.get("ts", 0))),
            )
        st.markdown("</div>", unsafe_allow_html=True)

        with st.form("chat"):
            st.selectbox(
                locale["ai_tutor"]["language"], ["Python", "JavaScript", "Java", "C++"]
            )
            text = st.text_input(
                locale["ai_tutor"]["placeholder"],
                key=f"tutor_input_{st.session_state.tutor_input_key}",
            )
            submit = st.form_submit_button(locale["ai_tutor"]["send"])

            if submit and text:
                lang_code = st.session_state.get("lang", "en")
                st.session_state.chat.append(
                    {
                        "sender": locale["ai_tutor"]["user_label"],
                        "text": text,
                        "ts": time.time(),
                    }
                )
                with st.spinner("Thinking..."):
                    try:
                        result = asyncio.run(chat(text, get_session_id(), lang_code))
                        reply = result.get("response", "No response from backend.")
                    except Exception as e:
                        reply = f"Error: {e}"
                st.session_state.chat.append(
                    {
                        "sender": locale["ai_tutor"]["ai_label"],
                        "text": reply,
                        "ts": time.time(),
                    }
                )
                st.session_state.tutor_input_key += 1
                st.rerun()

    with cols[1]:
        st.markdown(
            "<div class='glass-panel' style='padding:1rem; border-radius:1rem;'>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='font-weight:600; margin-bottom:0.75rem;'>{locale['ai_tutor']['suggested']}</div>",
            unsafe_allow_html=True,
        )
        for s in SUGGESTED:
            if st.button(s, key=s, use_container_width=True):
                lang_code = st.session_state.get("lang", "en")
                st.session_state.chat.append(
                    {
                        "sender": locale["ai_tutor"]["user_label"],
                        "text": s,
                        "ts": time.time(),
                    }
                )
                with st.spinner("Thinking..."):
                    try:
                        result = asyncio.run(chat(s, get_session_id(), lang_code))
                        reply = result.get("response", "No response.")
                    except Exception as e:
                        reply = f"Error: {e}"
                st.session_state.chat.append(
                    {
                        "sender": locale["ai_tutor"]["ai_label"],
                        "text": reply,
                        "ts": time.time(),
                    }
                )
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

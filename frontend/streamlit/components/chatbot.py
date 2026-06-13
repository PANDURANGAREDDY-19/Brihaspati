import streamlit as st
import time
import asyncio
from api_client import chat


def render(locale):
    welcome = locale.get("chat", {}).get(
        "welcome", "Hello! I'm Brihaspati. Ask me anything!"
    )

    if "chatbot_msgs" not in st.session_state:
        st.session_state.chatbot_msgs = [
            {"sender": "bot", "text": welcome, "ts": time.time()}
        ]
    if "chatbot_open" not in st.session_state:
        st.session_state.chatbot_open = False
    if "chatbot_session" not in st.session_state:
        st.session_state.chatbot_session = f"chatbot_{int(time.time())}"

    btn_label = "✕ Close Chat" if st.session_state.chatbot_open else "💬 Chat with AI"
    col, _ = st.columns([1, 4])
    with col:
        st.markdown("<div class='chatbot-toggle'>", unsafe_allow_html=True)
        if st.button(btn_label, key="chatbot_toggle", use_container_width=True):
            st.session_state.chatbot_open = not st.session_state.chatbot_open
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    if not st.session_state.chatbot_open:
        return

    # Build chat messages HTML as a single complete block
    msgs_html = ""
    for msg in st.session_state.chatbot_msgs:
        is_bot = msg["sender"] == "bot"
        role = "ai" if is_bot else "user"
        avatar = "🤖" if is_bot else "🙂"
        label = "Mentor" if is_bot else "You"
        ts = time.strftime("%H:%M", time.localtime(msg.get("ts", 0)))
        msgs_html += f"""
        <div class="msg-row {role}">
            <div class="msg-avatar {role}">{avatar}</div>
            <div class="msg-bubble {role}">
                <div class="msg-label">{label}</div>
                <div>{msg["text"]}</div>
                <div class="msg-time">{ts}</div>
            </div>
        </div>
        """

    st.markdown(
        f"""
        <div class="glass-panel" style="max-height:360px;overflow-y:auto;">
            {msgs_html}
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("chatbot_input", clear_on_submit=True, border=False):
        text = st.text_input(
            "Message",
            placeholder="Ask a coding question…",
            label_visibility="collapsed",
        )
        send = st.form_submit_button("Send", use_container_width=True)

    if send and text.strip():
        st.session_state.chatbot_msgs.append(
            {"sender": "user", "text": text.strip(), "ts": time.time()}
        )
        lang_code = st.session_state.get("lang", "en")
        with st.spinner("Thinking…"):
            try:
                result = asyncio.run(
                    chat(text.strip(), st.session_state.chatbot_session, lang_code)
                )
                reply = result.get("response", "Sorry, no response from backend.")
            except Exception as e:
                reply = f"⚠️ Error: {e}"
        st.session_state.chatbot_msgs.append(
            {"sender": "bot", "text": reply, "ts": time.time()}
        )
        st.rerun()

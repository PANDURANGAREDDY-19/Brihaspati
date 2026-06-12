import streamlit as st
import time
from components.ui import render_section_header

PROMPTS = [
    "Explain recursion.",
    "What is OOP?",
    "Explain Python dictionaries.",
    "Give me tips for interview arrays.",
]

MOCK_RESPONSES = {
    "Explain recursion.": "Recursion occurs when a function calls itself to solve smaller instances; ensure a base case and decreasing input.",
    "What is OOP?": "Object-oriented programming groups data and behavior into classes; key ideas: encapsulation, inheritance, polymorphism.",
    "Explain Python dictionaries.": "Dictionaries store key-value pairs with amortized O(1) lookups using hashing.",
    "Give me tips for interview arrays.": "Practice sliding window, two-pointers, and sorting-based approaches. Focus on edge cases and complexity.",
}


def render(locale):
    st.markdown(f"<h2 style='margin-bottom:0.1rem;'>{locale['ai_coach']['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: var(--muted); margin-bottom:1.0rem;'>{locale['ai_coach']['subtitle']}</div>", unsafe_allow_html=True)

    if "coach_history" not in st.session_state:
        st.session_state.coach_history = [
            {"sender": locale['ai_coach']['ai_label'], "text": locale['ai_coach']['welcome_message'], "ts": time.time()},
        ]

    left, right = st.columns([3, 1], gap="large")
    with left:
        st.markdown("<div class='card chat-container'>", unsafe_allow_html=True)
        for msg in st.session_state.coach_history:
            sender = msg['sender']
            text = msg['text']
            ts = msg.get('ts', time.time())
            timestr = time.strftime('%b %d • %H:%M', time.localtime(ts))
            if sender == locale['ai_coach']['ai_label']:
                st.markdown(
                    f"<div class='message-row'><div class='avatar'>🤖</div><div class='bubble ai'><strong>{sender}</strong><div style='margin-top:6px;'>{text}</div><div class='timestamp'>{timestr}</div></div></div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"<div class='message-row' style='justify-content:flex-end;'><div class='bubble user'><strong>{sender}</strong><div style='margin-top:6px;'>{text}</div><div class='timestamp'>{timestr}</div></div><div class='avatar'>🙂</div></div>",
                    unsafe_allow_html=True,
                )
        st.markdown("</div>", unsafe_allow_html=True)

        # input form with typing animation simulation
        with st.form(key='coach_form'):
            query = st.text_input(locale['ai_coach']['message_placeholder'], key='coach_input')
            submitted = st.form_submit_button(locale['ai_coach']['send_button'])
            if submitted and query:
                st.session_state.coach_history.append({"sender": locale['ai_coach']['user_label'], "text": query, "ts": time.time()})
                placeholder = st.empty()
                # simulate typing
                placeholder.markdown(f"<div class='card bubble ai'><div class='timestamp'>{locale['ai_coach']['typing']}...</div></div>", unsafe_allow_html=True)
                time.sleep(0.8)
                response = MOCK_RESPONSES.get(query, "Here's a helpful mock response to guide your learning and next steps.")
                st.session_state.coach_history.append({"sender": locale['ai_coach']['ai_label'], "text": response, "ts": time.time()})
                placeholder.empty()
                st.experimental_rerun()

    with right:
        st.markdown(f"<div class='card'><div class='section-title'>{locale['ai_coach']['suggested_prompts']}</div>", unsafe_allow_html=True)
        for prompt in PROMPTS:
            if st.button(prompt, key=f"prompt_{prompt}"):
                st.session_state.coach_history.append({"sender": locale['ai_coach']['user_label'], "text": prompt, "ts": time.time()})
                st.session_state.coach_history.append({"sender": locale['ai_coach']['ai_label'], "text": MOCK_RESPONSES.get(prompt, '...'), "ts": time.time()})
                st.experimental_rerun()
        st.markdown("</div>", unsafe_allow_html=True)

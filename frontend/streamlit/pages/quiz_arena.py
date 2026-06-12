import streamlit as st
from components.ui import render_page_header

BANK = [
    {
        "lang": "Python",
        "topic": "Lists",
        "difficulty": "Easy",
        "question": "What is the output of list(range(3))?",
        "options": ["[0,1,2]", "[1,2,3]", "[0,1,2,3]", "Error"],
        "answer": "[0,1,2]",
        "explain": "range(3) gives 0,1,2",
    },
    {
        "lang": "Python",
        "topic": "Functions",
        "difficulty": "Medium",
        "question": "What is a pure function?",
        "options": ["Mutates state", "Depends only on inputs", "Uses globals", "None"],
        "answer": "Depends only on inputs",
        "explain": "Pure functions return same output for same inputs.",
    },
]


def render(locale):
    render_page_header(locale["quiz_arena"]["title"], locale["quiz_arena"]["subtitle"])

    lang = st.selectbox(locale["quiz_arena"]["language"], ["Python", "JavaScript"])
    topic = st.selectbox(
        locale["quiz_arena"]["topic"], ["Lists", "Functions", "Algorithms"]
    )
    diff = st.selectbox(locale["quiz_arena"]["difficulty"], ["Easy", "Medium", "Hard"])

    if st.button(locale["quiz_arena"]["generate"], type="primary"):
        filtered = [
            q
            for q in BANK
            if q["lang"] == lang and q["topic"] == topic and q["difficulty"] == diff
        ]
        if not filtered:
            filtered = [q for q in BANK if q["lang"] == lang][:3]
        st.session_state.quiz = filtered

    if "quiz" in st.session_state:
        for i, q in enumerate(st.session_state.quiz, start=1):
            st.markdown(
                "<div class='glass-panel' style='padding:1rem; border-radius:1rem; margin-bottom:1rem;'>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"<div style='font-weight:700; margin-bottom:0.75rem;'>Q{i}. {q['question']}</div>",
                unsafe_allow_html=True,
            )
            choice = st.radio(f"options_{i}", q["options"], key=f"quiz_opt_{i}")
            if st.button(f"Check Answer {i}", key=f"quiz_check_{i}"):
                if choice == q["answer"]:
                    st.success(locale["quiz_arena"]["correct"])
                else:
                    st.error(locale["quiz_arena"]["incorrect"])
                st.info(q["explain"])
            st.markdown("</div>", unsafe_allow_html=True)

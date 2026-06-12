import streamlit as st
from components.ui import render_section_header

QUIZ_BANK = [
    {
        "topic": "Python",
        "difficulty": "Easy",
        "question": "What does `len(lista)` return in Python?",
        "options": ["Number of elements", "Last item", "Memory size", "Index of last"],
        "answer": "Number of elements",
        "explanation": "`len()` returns how many items are in the list.",
    },
    {
        "topic": "Algorithms",
        "difficulty": "Medium",
        "question": "What is the time complexity of binary search?",
        "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
        "answer": "O(log n)",
        "explanation": "Binary search halves the search space at each step.",
    },
    {
        "topic": "Data Structures",
        "difficulty": "Hard",
        "question": "Which data structure is best for FIFO behavior?",
        "options": ["Stack", "Queue", "Tree", "Graph"],
        "answer": "Queue",
        "explanation": "Queues process items in first-in, first-out order.",
    },
    {
        "topic": "JavaScript",
        "difficulty": "Intermediate",
        "question": "What does `===` compare in JavaScript?",
        "options": ["Value only", "Type only", "Value and type", "Reference only"],
        "answer": "Value and type",
        "explanation": "`===` is a strict equality operator that checks both type and value.",
    },
]


def render(locale):
    st.markdown(f"<h2 style='margin-bottom:0.1rem;'>{locale['quiz_lab']['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: var(--muted); margin-bottom:1.5rem;'>{locale['quiz_lab']['subtitle']}</div>", unsafe_allow_html=True)

    cols = st.columns(3, gap="large")
    topic = cols[0].selectbox(locale['quiz_lab']['topic'], ["Python", "Algorithms", "Data Structures", "JavaScript"])
    difficulty = cols[1].selectbox(locale['quiz_lab']['difficulty'], ["Easy", "Medium", "Hard", "Intermediate"])
    count = cols[2].slider(locale['quiz_lab']['number_of_questions'], 1, 4, 3)

    if st.button(locale['quiz_lab']['generate']):
        filtered = [q for q in QUIZ_BANK if q['topic'] == topic and (q['difficulty'] == difficulty or difficulty == 'Intermediate' or q['difficulty'] == 'Intermediate')]
        selected = (filtered or [q for q in QUIZ_BANK if q['topic'] == topic])[:count]
        # store in session
        st.session_state.quiz = {"items": selected, "answers": {}, "score": 0}

    if 'quiz' in st.session_state:
        quiz = st.session_state.quiz
        for idx, q in enumerate(quiz['items'], start=1):
            st.markdown("<div class='card' style='margin-bottom:1rem;'>", unsafe_allow_html=True)
            st.markdown(f"<div style='display:flex; justify-content:space-between; align-items:center;'><div style='font-size:1.05rem; font-weight:700;'>Q{idx}. {q['question']}</div><div class='small-badge badge-soft'>{q['topic']}</div></div>", unsafe_allow_html=True)
            choice = st.radio(f"choice_{idx}", q['options'], key=f"choice_{idx}")
            if st.button(f"Check Q{idx}", key=f"check_{idx}"):
                correct = choice == q['answer']
                if correct:
                    st.session_state.quiz['score'] += 1
                    st.success(locale['quiz_lab']['correct'])
                else:
                    st.error(locale['quiz_lab']['incorrect'])
                st.markdown(f"<div style='color: var(--muted); margin-top:0.5rem; font-size:0.95rem;'><strong>Explanation:</strong> {q['explanation']}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.quiz.get('items'):
            st.markdown(f"<div style='margin-top:0.8rem;' class='card'><strong>Score:</strong> {st.session_state.quiz.get('score',0)}/{len(st.session_state.quiz['items'])}</div>", unsafe_allow_html=True)

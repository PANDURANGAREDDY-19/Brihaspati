import streamlit as st
from components.ui import hero, stat_card, feature_card
import random

def render(locale):
    hero(locale['home']['title'], locale['home']['subtitle'], locale['home']['start'], locale['home']['explore'])

    stats = [
        (locale['home']['questions_solved'], '1.2k', '+6%', [random.randint(5,50) for _ in range(10)], '❓'),
        (locale['home']['quizzes_completed'], '420', '+3%', [random.randint(1,20) for _ in range(10)], '📝'),
        (locale['home']['problems_attempted'], '2.4k', '+8%', [random.randint(10,80) for _ in range(10)], '🧩'),
        (locale['home']['code_reviews'], '128', '+12%', [random.randint(1,12) for _ in range(10)], '🔍'),
    ]

    cols = st.columns(4, gap='large')
    for col, s in zip(cols, stats):
        with col:
            stat_card(s[0], s[1], s[2], chart_data=s[3], icon=s[4])

    st.markdown("<div style='margin-top:1rem; display:grid; grid-template-columns:repeat(3,1fr); gap:1rem;'>", unsafe_allow_html=True)
    feature_card(locale['home']['feature_tutor'], 'Interactive lessons and explanations', '🎓')
    feature_card(locale['home']['feature_debugger'], 'Instant code debugging assistance', '🐞')
    feature_card(locale['home']['feature_quiz'], 'Generate targeted quizzes', '🧠')
    feature_card(locale['home']['feature_arena'], 'Practice coding problems', '⚔️')
    feature_card(locale['home']['feature_reviewer'], 'Automated code review reports', '🔎')
    st.markdown("</div>", unsafe_allow_html=True)

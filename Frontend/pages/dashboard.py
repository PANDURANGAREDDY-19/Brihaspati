import streamlit as st
from components.ui import metric_card, render_section_header
from components.ui import metric_card_with_chart, hero_section
import random


def render(locale):
    # Hero section
    hero_section(locale['dashboard']['hero_title'], locale['dashboard']['hero_subtitle'], locale['dashboard']['start_learning'], locale['dashboard']['explore_features'])

    # Metrics grid with mini charts
    st.markdown("<div style='margin-top:1rem;'></div>", unsafe_allow_html=True)
    cols = st.columns(5, gap="large")
    metrics = [
        (locale['dashboard']['questions_asked'], "1.2k", "+8%", [random.randint(10, 50) for _ in range(12)], "❓"),
        (locale['dashboard']['quizzes_completed'], "420", "+5%", [random.randint(2, 20) for _ in range(12)], "📝"),
        (locale['dashboard']['challenges_solved'], "86", "+3%", [random.randint(0, 8) for _ in range(12)], "🏆"),
        (locale['dashboard']['code_reviews'], "128", "+12%", [random.randint(1, 12) for _ in range(12)], "🔍"),
        (locale['dashboard']['learning_streak'], "14d", "+2d", [random.randint(0, 1) for _ in range(12)], "🔥"),
    ]
    for col, metric in zip(cols, metrics):
        with col:
            metric_card_with_chart(metric[0], metric[1], metric[2], data=metric[3], icon=metric[4])

    # Learning roadmap
    st.markdown("<div class='card' style='margin-top:1.4rem;'>", unsafe_allow_html=True)
    render_section_header(locale['dashboard']['recommended_path'])
    roadmap = [
        "Python Fundamentals",
        "Functions & OOP",
        "Data Structures",
        "Algorithms",
        "System Design",
        "Interview Preparation",
    ]
    path_html = "".join(
        f"<div style='display:flex; align-items:center; gap:0.6rem; margin-bottom:0.6rem;'><div class='small-badge badge-soft'>{step}</div></div>"
        for step in roadmap
    )
    st.markdown(f"<div>{path_html}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Recent activity timeline
    st.markdown("<div class='card' style='margin-top:1.5rem;'>", unsafe_allow_html=True)
    render_section_header(locale['dashboard']['recent_activity'], locale['dashboard']['activity_desc'])
    timeline = [
        ("Today", "Reviewed Python list comprehensions and optimized a practice problem."),
        ("Yesterday", "Completed an algorithms challenge on recursion."),
        ("2 days ago", "Generated a quiz for hash maps and scored 90%."),
        ("Last week", "Practiced bug fixing with mock code snippets."),
    ]
    for date, note in timeline:
        st.markdown(
            f"<div class='timeline-item'><div class='timeline-date'>{date}</div><div style='font-weight:600;margin-top:0.35rem;'>{note}</div></div>",
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)

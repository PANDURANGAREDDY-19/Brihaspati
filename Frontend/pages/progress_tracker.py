import streamlit as st
import pandas as pd
import altair as alt
from components.ui import render_section_header


def render(locale):
    st.markdown(f"<h2 style='margin-bottom:0.15rem;'>{locale['progress_tracker']['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: var(--muted); margin-bottom:1.5rem;'>{locale['progress_tracker']['subtitle']}</div>", unsafe_allow_html=True)

    weekly = pd.DataFrame(
        {
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Practice Hours": [1.5, 2.0, 2.5, 1.8, 2.3, 3.0, 2.7],
            "Challenges": [1, 1, 2, 1, 1, 2, 1],
        }
    )
    st.markdown("<div class='card' style='margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    render_section_header(locale['progress_tracker']['weekly_progress'])
    chart = alt.Chart(weekly).mark_line(point=True).encode(x='Day', y='Practice Hours').interactive()
    st.altair_chart(chart, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    skill_data = pd.DataFrame(
        {
            "Skill": ["Python", "Algorithms", "Data Structures", "System Design", "Debugging"],
            "Mastery": [78, 64, 72, 50, 68],
        }
    )
    st.markdown("<div class='card' style='margin-bottom:1.5rem;'>", unsafe_allow_html=True)
    render_section_header(locale['progress_tracker']['skill_distribution'])
    bar = alt.Chart(skill_data).mark_bar(cornerRadiusTopLeft=6, cornerRadiusTopRight=6).encode(x='Skill', y='Mastery', color=alt.Color('Mastery', scale=alt.Scale(scheme='blues')))
    st.altair_chart(bar, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    quiz_perf = pd.DataFrame(
        {
            "Quiz": ["Basics", "OOP", "Arrays", "Recursion"],
            "Score": [92, 88, 95, 85],
        }
    )
    completion = pd.DataFrame(
        {
            "Status": ["Completed", "In Progress", "Pending"],
            "Value": [62, 18, 20],
        }
    )
    cols = st.columns(2, gap="large")
    with cols[0]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        render_section_header(locale['progress_tracker']['quiz_performance'])
        st.altair_chart(alt.Chart(quiz_perf).mark_bar().encode(x='Quiz', y='Score', color=alt.Color('Score', scale=alt.Scale(scheme='greens'))), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        render_section_header(locale['progress_tracker']['challenge_completion'])
        st.altair_chart(alt.Chart(completion).mark_arc(innerRadius=50).encode(theta=alt.Theta(field='Value', type='quantitative'), color='Status'), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

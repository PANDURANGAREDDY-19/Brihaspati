import streamlit as st
from components.ui import render_course_card
from data.mock import course_categories


def render(locale):
    st.markdown(
        """
        <div class='glass-panel' style='margin-bottom: 2rem;'>
            <span style='color: #6ee7b7; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.28em;'>Learning Categories</span>
            <h1 style='margin-top: 1rem; font-size: 2.25rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>Explore the courses that power your future.</h1>
            <p style='margin-top: 1rem; max-width: 42rem; color: #cbd5e1; margin-bottom: 0;'>Browse programming, English, and Telugu learning paths created for meaningful progress across every skill level.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3, gap="large")
    for idx, category in enumerate(course_categories):
        with cols[idx]:
            render_course_card(
                category["title"],
                category["description"],
                category["topics"],
                category["accent"],
            )

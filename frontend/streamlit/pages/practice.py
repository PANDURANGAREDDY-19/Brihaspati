import streamlit as st
from components.ui import render_practice_card
from data.mock import practice_cards


def render(locale):
    st.markdown(
        """
        <div class='glass-panel' style='margin-bottom: 2rem;'>
            <span style='color: #6ee7b7; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.28em;'>Practice Lab</span>
            <h1 style='margin-top: 1rem; font-size: 2.25rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>Build confidence with practical exercises.</h1>
            <p style='margin-top: 1rem; max-width: 42rem; color: #cbd5e1; margin-bottom: 0;'>Choose a learning stream and get immediate hands-on practice through mock quizzes and interactive challenges.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3, gap="large")
    for idx, card in enumerate(practice_cards):
        with cols[idx]:
            render_practice_card(
                card["title"], card["description"], card["items"], card["accent"]
            )

import streamlit as st
from components.ui import render_course_card
from data.mock import course_categories


def render(locale):
    cols = st.columns([1.2, 0.8], gap="large")
    with cols[0]:
        st.markdown(
            """
            <div class='glass-panel card' style='padding: 2.5rem; overflow: hidden; margin-bottom: 1.5rem;'>
                <span style='color: #6ee7b7; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.28em;'>Learn Skills That Matter</span>
                <h1 style='margin-top: 1.25rem; font-size: 2.75rem; font-weight: 600; line-height: 1.2; color: #ffffff; margin-bottom: 0;'>Master Programming, English, and Telugu through interactive learning.</h1>
                <p style='margin-top: 1.5rem; max-width: 42rem; font-size: 1rem; color: #cbd5e1; line-height: 1.75;'>CodeMentor AI brings the structure of a modern education platform with the energy of a creative learning studio. Explore courses, track your progress, and build confidence every day.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        btn_cols = st.columns([1.2, 1.4, 4.0], gap="small")
        with btn_cols[0]:
            st.markdown("<div class='hero-primary-btn'>", unsafe_allow_html=True)
            if st.button("Start Learning", key="hero_start"):
                st.session_state.page = "practice"
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        with btn_cols[1]:
            st.markdown("<div class='hero-ghost-btn'>", unsafe_allow_html=True)
            if st.button("Explore Courses", key="hero_explore"):
                st.session_state.page = "courses"
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    with cols[1]:
        st.markdown(
            """
            <div class='glass-panel card p-8' style='margin-bottom: 1.5rem;'>
                <span style='color: #6ee7b7; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.24em;'>Fast track your goals</span>
                <h2 style='margin-top: 1rem; font-size: 1.875rem; font-weight: 600; color: #ffffff;'>From beginner to confident learner.</h2>
                <p style='margin-top: 1rem; color: #cbd5e1; margin-bottom: 0;'>Flexible lessons, guided practice, and progress tracking designed for every learner.</p>
            </div>

            <div class='glass-panel card p-8'>
                <div style='display: flex; justify-content: space-between; align-items: center; gap: 1rem;'>
                    <div>
                        <p style='text-transform: uppercase; letter-spacing: 0.24em; color: #94a3b8; font-size: 0.875rem; margin: 0;'>Latest growth</p>
                        <p style='margin-top: 0.75rem; font-size: 1.875rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>+24%</p>
                    </div>
                    <div style='border-radius: 999px; background: rgba(255, 255, 255, 0.05); padding: 0.75rem 1rem; color: #e2e8f0; font-size: 0.875rem;'>Weekly momentum</div>
                </div>
                <div style='margin-top: 1.75rem; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem;'>
                    <div style='border-radius: 1.5rem; background: rgba(15, 23, 42, 0.6); padding: 1.25rem; border: 1px solid rgba(255, 255, 255, 0.04);'>
                        <p style='font-size: 0.875rem; color: #94a3b8; margin: 0;'>Programming learners</p>
                        <p style='margin-top: 0.75rem; font-size: 1.5rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>1.4k</p>
                    </div>
                    <div style='border-radius: 1.5rem; background: rgba(15, 23, 42, 0.6); padding: 1.25rem; border: 1px solid rgba(255, 255, 255, 0.04);'>
                        <p style='font-size: 0.875rem; color: #94a3b8; margin: 0;'>Language learners</p>
                        <p style='margin-top: 0.75rem; font-size: 1.5rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>980</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style='display: flex; justify-content: space-between; align-items: center; gap: 1rem; margin-top: 4rem; margin-bottom: 2rem;'>
            <div>
                <span style='color: #6ee7b7; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.24em;'>Featured learning tracks</span>
                <h2 style='font-size: 1.875rem; font-weight: 600; margin-top: 0.5rem; color: #ffffff; margin-bottom: 0;'>Courses built for growth</h2>
            </div>
            <span style='font-size: 0.875rem; color: #94a3b8;'>Updated weekly with new topics</span>
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

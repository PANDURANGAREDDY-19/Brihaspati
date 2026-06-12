import streamlit as st
from data.mock import team_members


def render(locale):
    st.markdown(
        """
        <div class='glass-panel card p-10' style='margin-bottom: 2rem;'>
            <span style='color: #6ee7b7; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.28em;'>About CodeMentor AI</span>
            <h1 style='margin-top: 1rem; font-size: 2.25rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>A smarter way to learn programming and languages.</h1>
            <p style='margin-top: 1rem; max-width: 48rem; color: #cbd5e1; margin-bottom: 0;'>Our mission is to deliver a welcoming, modern learning experience for students who want to grow with structured content, useful practice, and clear progress tracking.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    cols = st.columns(3, gap='large')
    with cols[0]:
        st.markdown(
            """
            <div class='glass-panel card p-8' style='height: 100%;'>
                <h2 style='font-size: 1.5rem; font-weight: 600; color: #ffffff; margin: 0;'>Mission</h2>
                <p style='margin-top: 1rem; color: #cbd5e1; margin-bottom: 0;'>Empower learners with scalable, easy-to-follow lessons that bridge coding and language learning in one polished platform.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.markdown(
            """
            <div class='glass-panel card p-8' style='height: 100%;'>
                <h2 style='font-size: 1.5rem; font-weight: 600; color: #ffffff; margin: 0;'>Vision</h2>
                <p style='margin-top: 1rem; color: #cbd5e1; margin-bottom: 0;'>Create a trusted digital campus where every student gains skills for school, career, and everyday communication.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[2]:
        st.markdown(
            """
            <div class='glass-panel card p-8' style='height: 100%;'>
                <h2 style='font-size: 1.5rem; font-weight: 600; color: #ffffff; margin: 0;'>Benefits</h2>
                <ul style='margin-top: 1rem; padding-left: 1.25rem; color: #cbd5e1; display: flex; flex-direction: column; gap: 0.75rem; margin-bottom: 0;'>
                    <li>Personalized learning paths</li>
                    <li>Practice-driven mastery</li>
                    <li>Progress tracking and motivation</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    team_grid_html = ""
    for member in team_members:
        team_grid_html += f"""
        <div style='border-radius: 1.5rem; border: 1px solid rgba(255, 255, 255, 0.05); background: rgba(2, 6, 23, 0.5); padding: 1.5rem;'>
            <p style='font-size: 1.125rem; font-weight: 600; color: #ffffff; margin: 0;'>{member['name']}</p>
            <p style='margin-top: 0.5rem; color: #94a3b8; margin-bottom: 0;'>{member['role']}</p>
        </div>
        """

    st.markdown(
        f"""
        <div class='glass-panel card p-10' style='margin-top: 2rem; margin-bottom: 2rem;'>
            <div style='display: flex; flex-direction: column; gap: 1rem; justify-content: space-between; align-items: flex-start;'>
                <div>
                    <h2 style='font-size: 1.875rem; font-weight: 600; color: #ffffff; margin: 0;'>Meet your learning team</h2>
                    <p style='margin-top: 0.75rem; color: #cbd5e1; margin-bottom: 0;'>A small team building big learning experiences with clarity and care.</p>
                </div>
            </div>
            
            <div style='margin-top: 2rem; display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1rem;'>
                {team_grid_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='glass-panel card p-10'>
            <h2 style='font-size: 1.875rem; font-weight: 600; color: #ffffff; margin: 0;'>Contact</h2>
            <p style='margin-top: 1rem; color: #cbd5e1;'>Get in touch with the CodeMentor AI team for course guidance or feedback.</p>
            <div style='margin-top: 2rem;'>
                <div style='border-radius: 1.5rem; background: rgba(2, 6, 23, 0.6); padding: 1.5rem;'>
                    <p style='font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.24em; color: #64748b; margin: 0;'>Email</p>
                    <p style='margin-top: 0.75rem; font-size: 1.125rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>munindrasripathi@gmail.com</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


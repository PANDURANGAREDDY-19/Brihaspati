import streamlit as st
from components.ui import render_stat_card
from data.mock import dashboard_stats, course_detail_modules


def render(locale):
    st.markdown(
        """
        <div class='glass-panel card p-10' style='margin-bottom: 2rem;'>
            <span style='color: #6ee7b7; font-size: 0.875rem; text-transform: uppercase; letter-spacing: 0.28em;'>Learning Dashboard</span>
            <h1 style='margin-top: 1rem; font-size: 2.25rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>Your progress at a glance.</h1>
            <p style='margin-top: 1rem; max-width: 42rem; color: #cbd5e1; margin-bottom: 0;'>Monitor enrolled courses, completed lessons, streaks, and overall progress from one premium dashboard.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stat_cols = st.columns(4, gap='large')
    for idx, stat in enumerate(dashboard_stats):
        with stat_cols[idx]:
            render_stat_card(stat['label'], stat['value'], stat['detail'], stat['accent'])

    cols = st.columns([1.2, 0.8], gap='large')
    with cols[0]:
        modules_html = ""
        for module in course_detail_modules:
            modules_html += f"""
            <div style='border-radius: 1.5rem; border: 1px solid rgba(255, 255, 255, 0.05); background: rgba(2, 6, 23, 0.5); padding: 1.25rem; margin-bottom: 1rem;'>
                <div style='display: flex; align-items: center; justify-content: space-between; gap: 0.75rem;'>
                    <div>
                        <h3 style='font-weight: 600; color: #ffffff; margin: 0; font-size: 1rem;'>{module['title']}</h3>
                        <p style='font-size: 0.875rem; color: #94a3b8; margin: 0.25rem 0 0;'>{module['duration']}</p>
                    </div>
                    <span style='border-radius: 999px; background: rgba(255, 255, 255, 0.05); padding: 0.25rem 0.75rem; font-size: 0.875rem; color: #cbd5e1;'>{module['status']}</span>
                </div>
            </div>
            """
        
        st.markdown(
            f"""
            <div class='glass-panel card p-10'>
                <div style='display: flex; align-items: center; justify-content: space-between; gap: 1rem;'>
                    <div>
                        <span style='font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.28em; color: #94a3b8;'>Active course</span>
                        <h2 style='margin-top: 0.75rem; font-size: 1.875rem; font-weight: 600; color: #ffffff; margin-bottom: 0;'>Python Programming</h2>
                    </div>
                    <span style='border-radius: 999px; background: rgba(255, 255, 255, 0.05); padding: 0.5rem 1rem; font-size: 0.875rem; color: #cbd5e1;'>Intermediate</span>
                </div>
                <p style='margin-top: 1.5rem; color: #cbd5e1;'>A hands-on course for developers who want to build real applications with Python. Learn key concepts, best practices, and apply them in practical exercises.</p>
                
                <div style='margin-top: 2rem;'>
                    {modules_html}
                </div>
                
                <div style='margin-top: 2rem;'>
                    <div style='display: flex; align-items: center; justify-content: space-between; gap: 1rem;'>
                        <p style='font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.24em; color: #94a3b8; margin: 0;'>Course progress</p>
                        <p style='font-size: 0.875rem; font-weight: 600; color: #ffffff; margin: 0;'>72%</p>
                    </div>
                    <div class='progress-bar' style='margin-top: 0.75rem; height: 0.5rem; background: rgba(255, 255, 255, 0.08); border-radius: 999px; overflow: hidden;'>
                        <span style='display: block; height: 100%; width: 72%; background: linear-gradient(135deg, #7c3aed, #22c55e); border-radius: 999px;'></span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with cols[1]:
        st.markdown(
            """
            <div class='glass-panel card p-10'>
                <p style='font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.24em; color: #64748b;'>Learning habits</p>
                <div style='margin-top: 2rem; display: flex; flex-direction: column; gap: 1.25rem;'>
                    <div style='border-radius: 1.5rem; border: 1px solid rgba(255, 255, 255, 0.05); background: rgba(2, 6, 23, 0.5); padding: 1.5rem;'>
                        <h3 style='font-size: 1.25rem; font-weight: 600; color: #ffffff; margin: 0;'>Weekly streak</h3>
                        <p style='margin-top: 0.75rem; color: #cbd5e1; margin-bottom: 0;'>You've learned every day for 16 days. Keep the streak alive with short lessons and practice.</p>
                    </div>
                    <div style='border-radius: 1.5rem; border: 1px solid rgba(255, 255, 255, 0.05); background: rgba(2, 6, 23, 0.5); padding: 1.5rem;'>
                        <h3 style='font-size: 1.25rem; font-weight: 600; color: #ffffff; margin: 0;'>Upcoming session</h3>
                        <p style='margin-top: 0.75rem; color: #cbd5e1; margin-bottom: 0;'>Tomorrow: English conversation practice and Telugu alphabet review.</p>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


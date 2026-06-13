import streamlit as st
from components.ui import render_stat_card
from data.mock import dashboard_stats, course_detail_modules


def render(locale):
    st.markdown(
        """
        <div class="page-hero">
            <span class="overline">Learning Dashboard</span>
            <h1>Your progress at a glance.</h1>
            <p>Monitor enrolled courses, completed lessons, streaks, and progress from one dashboard.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    stat_cols = st.columns(4, gap="large")
    for idx, stat in enumerate(dashboard_stats):
        with stat_cols[idx]:
            render_stat_card(
                stat["label"], stat["value"], stat["detail"], stat["accent"]
            )

    col_main, col_side = st.columns([1.2, 0.8], gap="large")

    with col_main:
        modules_html = "".join(
            f"""
            <div class="module-row">
                <div>
                    <h4>{m["title"]}</h4>
                    <p>{m["duration"]}</p>
                </div>
                <span class="status-pill">{m["status"]}</span>
            </div>
            """
            for m in course_detail_modules
        )
        st.markdown(
            f"""
            <div class="glass-panel">
                <div style="display:flex;align-items:center;justify-content:space-between;gap:1rem;">
                    <div>
                        <span style="font-size:0.72rem;text-transform:uppercase;
                                     letter-spacing:0.24em;color:#64748b;">Active Course</span>
                        <h2 style="font-size:1.6rem;font-weight:600;color:#fff;margin:0.5rem 0 0;">
                            Python Programming
                        </h2>
                    </div>
                    <span class="status-pill">Intermediate</span>
                </div>
                <p style="color:#94a3b8;margin-top:1rem;font-size:0.9rem;line-height:1.6;">
                    A hands-on course for developers who want to build real applications with Python.
                </p>
                <div style="margin-top:1.25rem;">{modules_html}</div>
                <div class="progress-wrap">
                    <div class="progress-label">
                        <span>Course Progress</span><span>72%</span>
                    </div>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width:72%;"></div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_side:
        st.markdown(
            """
            <div class="glass-panel">
                <span style="font-size:0.72rem;text-transform:uppercase;
                             letter-spacing:0.2em;color:#64748b;">Learning Habits</span>
                <div class="module-row" style="margin-top:1rem;flex-direction:column;
                                               align-items:flex-start;">
                    <h4>🔥 Weekly Streak</h4>
                    <p style="margin-top:0.4rem;color:#94a3b8;font-size:0.87rem;line-height:1.5;">
                        You've learned every day for 16 days. Keep the streak alive!
                    </p>
                </div>
                <div class="module-row" style="flex-direction:column;align-items:flex-start;">
                    <h4>📅 Upcoming Session</h4>
                    <p style="margin-top:0.4rem;color:#94a3b8;font-size:0.87rem;line-height:1.5;">
                        Tomorrow: English conversation practice and Telugu alphabet review.
                    </p>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

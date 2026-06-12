import streamlit as st
from pathlib import Path
import pandas as pd
import altair as alt


def inject_css():
    css_path = Path(__file__).resolve().parent.parent / 'assets' / 'styles.css'
    if css_path.exists():
        with open(css_path, 'r', encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def hero(title, subtitle, primary, secondary):
    st.markdown(
        f"""
        <div class='hero card'>
            <div class='hero-copy'>
                <h1>{title}</h1>
                <p>{subtitle}</p>
            </div>
            <div class='hero-actions'>
                <button class='btn-primary'>{primary}</button>
                <button class='btn-ghost'>{secondary}</button>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_page_header(title, subtitle=None):
    subtitle_html = f"<div class='page-subtitle'>{subtitle}</div>" if subtitle else ""
    st.markdown(
        f"""
        <div class='page-header'>
            <div class='page-title-group'>
                <div class='page-badge'>CodeMentor AI</div>
                <h1>{title}</h1>
                {subtitle_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(title, subtitle=None):
    subtitle_html = f"<div class='section-subtitle'>{subtitle}</div>" if subtitle else ""
    st.markdown(
        f"""
        <div class='section-header'>
            <div>
                <h3>{title}</h3>
                {subtitle_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def stat_card(title, value, trend, chart_data=None, icon=''):
    st.markdown("<div class='card card-metric'>", unsafe_allow_html=True)
    cols = st.columns([1, 3], gap='small')
    with cols[0]:
        st.markdown(f"<div class='metric-icon'>{icon}</div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"<div class='metric-label'>{title}</div>")
        st.markdown(f"<div class='metric-value'>{value} <span>{trend}</span></div>")
        if chart_data:
            try:
                df = pd.DataFrame({'x': list(range(len(chart_data))), 'y': chart_data})
                chart = alt.Chart(df).mark_area(opacity=0.18, color='#8b5cf6').encode(x='x', y='y')
                st.altair_chart(chart, use_container_width=True)
            except Exception:
                pass
    st.markdown("</div>", unsafe_allow_html=True)


def feature_card(title, desc, icon=''):
    st.markdown(
        f"""
        <div class='card card-feature'>
            <div class='feature-top'>
                <div>
                    <strong>{title}</strong>
                    <div>{desc}</div>
                </div>
                <div class='feature-icon'>{icon}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def chat_bubble(sender, text, ai=True, ts=None):
    time_html = f"<div class='timestamp'>{ts}</div>" if ts else ""
    if ai:
        st.markdown(
            f"""
            <div class='message-row'>
                <div class='avatar'>🤖</div>
                <div class='bubble ai'>
                    <strong>{sender}</strong>
                    <div>{text}</div>
                    {time_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class='message-row message-user'>
                <div class='bubble user'>
                    <strong>{sender}</strong>
                    <div>{text}</div>
                    {time_html}
                </div>
                <div class='avatar'>🙂</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

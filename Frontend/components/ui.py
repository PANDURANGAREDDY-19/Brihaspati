import streamlit as st
import pandas as pd
import altair as alt


from pathlib import Path


def inject_css(theme: str):
    light_swatches = {
        "bg": "#f5f7ff",
        "card": "rgba(255,255,255,0.88)",
        "text": "#101827",
        "muted": "#5c6b8a",
        "surface": "rgba(255,255,255,0.75)",
        "border": "rgba(16,24,40,0.08)",
        "shadow": "0 24px 48px rgba(15,23,42,0.08)",
    }
    dark_swatches = {
        "bg": "#071523",
        "card": "rgba(10,25,50,0.86)",
        "text": "#f8fafc",
        "muted": "#94a3b8",
        "surface": "rgba(15,23,42,0.75)",
        "border": "rgba(148,163,184,0.12)",
        "shadow": "0 24px 48px rgba(15,23,42,0.35)",
    }
    swatches = dark_swatches if theme == "Dark" else light_swatches
    base_styles = Path(__file__).resolve().parent.parent / "assets" / "styles.css"
    css_text = base_styles.read_text() if base_styles.exists() else ""
    st.markdown(
        f"""
        <style>
            :root {{
                --bg: {swatches['bg']};
                --card: {swatches['card']};
                --text: {swatches['text']};
                --muted: {swatches['muted']};
                --surface: {swatches['surface']};
                --border: {swatches['border']};
                --shadow: {swatches['shadow']};
            }}
            {css_text}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(title: str, subtitle: str = ""):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)
    if subtitle:
        st.markdown(f"<div style='color: var(--muted); margin-bottom:1.2rem;'>{subtitle}</div>", unsafe_allow_html=True)


def metric_card(label: str, value: str, highlight: str = ""):
    st.markdown(
        f"""
        <div class='card'>
            <div class='metric-label'>{label}</div>
            <div class='metric-value'>{value}</div>
            <div style='color: var(--muted); margin-top: 0.5rem;'>{highlight}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card_with_chart(label: str, value: str, trend: str, data=None, icon: str = ""):
    # data: list or pandas Series for mini chart
    st.markdown("<div class='card' style='padding:1rem;'>", unsafe_allow_html=True)
    cols = st.columns([1, 2], gap="small")
    with cols[0]:
        st.markdown(f"<div style='font-size:1.05rem; font-weight:700;'>{icon}</div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"<div class='metric-label'>{label}</div>")
        st.markdown(f"<div class='metric-value'>{value} <span style='font-size:0.9rem; color:var(--muted); margin-left:0.6rem;'>{trend}</span></div>")
        if data is not None:
            try:
                series = pd.DataFrame({"x": list(range(len(data))), "y": list(data)})
                chart = alt.Chart(series).mark_area(opacity=0.18, color="#6366F1").encode(x="x:Q", y="y:Q")
                st.altair_chart(chart, use_container_width=True)
            except Exception:
                pass
    st.markdown("</div>", unsafe_allow_html=True)


def hero_section(title: str, subtitle: str, primary_label: str, secondary_label: str):
    st.markdown("<div style='margin-bottom:1rem;'>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style='padding:1.6rem; border-radius:18px; background: linear-gradient(90deg, rgba(99,102,241,0.12), rgba(14,165,233,0.08));'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <h1 style='margin:0; font-size:1.6rem;'>{title}</h1>
                    <div style='color:var(--muted); margin-top:0.45rem;'>{subtitle}</div>
                </div>
                <div style='display:flex; gap:0.6rem;'>
                    <button style='background:linear-gradient(90deg,#6366F1,#22C1C3); color:white; border:none; padding:0.6rem 1rem; border-radius:10px; font-weight:700;'>{primary_label}</button>
                    <button style='background:transparent; border:1px solid rgba(16,24,40,0.06); padding:0.5rem 0.9rem; border-radius:10px;'>{secondary_label}</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

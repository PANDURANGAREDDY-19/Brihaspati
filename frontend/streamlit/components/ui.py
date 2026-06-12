import streamlit as st
from pathlib import Path


def inject_css():
    css_path = Path(__file__).resolve().parent.parent / "assets" / "styles.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_page_header(title, subtitle=None):
    subtitle_html = f"<p class='hero-text'>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f"""
        <div class='glass-panel hero-card'>
            <span class='text-sm uppercase tracking-[0.28em] text-emerald-300/80'>CodeMentor AI</span>
            <h1 class='hero-title'>{title}</h1>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(title, subtitle=None):
    subtitle_html = (
        f"<p style='color:#94a3b8; font-size:0.875rem; margin:0;'>{subtitle}</p>"
        if subtitle
        else ""
    )
    st.markdown(
        f"""
        <div class='section-header' style='margin-bottom:1rem;'>
            <h3 style='margin:0; color:#f8fafc;'>{title}</h3>
            {subtitle_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def chat_bubble(sender, text, ai=True, ts=None):
    time_html = (
        f"<div style='font-size:0.7rem;color:#64748b;margin-top:0.25rem;'>{ts}</div>"
        if ts
        else ""
    )
    if ai:
        st.markdown(
            f"""
            <div style='display:flex; gap:0.75rem; margin-bottom:1rem; align-items:flex-start;'>
                <div style='width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#8b5cf6,#10b981);display:grid;place-items:center;font-size:1rem;flex-shrink:0;'>🤖</div>
                <div style='background:rgba(15,23,42,0.8); border-radius:1rem 1rem 1rem 0; padding:0.75rem 1rem; max-width:80%;'>
                    <strong style='font-size:0.75rem;color:#6ee7b7;'>{sender}</strong>
                    <div style='margin-top:0.25rem;color:#e2e8f0;'>{text}</div>
                    {time_html}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style='display:flex; gap:0.75rem; margin-bottom:1rem; align-items:flex-start; justify-content:flex-end;'>
                <div style='background:rgba(16,185,129,0.1); border-radius:1rem 1rem 0 1rem; padding:0.75rem 1rem; max-width:80%;'>
                    <strong style='font-size:0.75rem;color:#10b981;'>{sender}</strong>
                    <div style='margin-top:0.25rem;color:#f1f5f9;'>{text}</div>
                    {time_html}
                </div>
                <div style='width:36px;height:36px;border-radius:50%;background:rgba(255,255,255,0.1);display:grid;place-items:center;font-size:1rem;flex-shrink:0;'>🙂</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_stat_card(label, value, detail, accent=""):
    accent_style = f"background: linear-gradient(135deg, {accent});" if accent else ""
    st.markdown(
        f"""
        <div class='glass-panel card p-6 shadow-lg' style='margin-bottom: 1.5rem;'>
            <span style='display: inline-flex; border-radius: 999px; {accent_style} padding: 0.25rem 0.75rem; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.2em; color: rgba(255, 255, 255, 0.9);'>
                {label}
            </span>
            <p style='margin-top: 1.5rem; font-size: 2.25rem; font-weight: 600; letter-spacing: -0.025em; color: #ffffff; margin-bottom: 0;'>{value}</p>
            <p style='margin-top: 0.5rem; font-size: 0.875rem; color: #94a3b8; margin-bottom: 0;'>{detail}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_course_card(title, description, topics, accent=""):
    gradient_style = (
        f"background: linear-gradient(to right, {accent}); -webkit-background-clip: text; -webkit-text-fill-color: transparent;"
        if accent
        else ""
    )
    topic_html = "".join(
        [
            f"<span style='display: inline-flex; border-radius: 999px; background: rgba(255, 255, 255, 0.05); padding: 0.5rem 0.75rem;'>{topic}</span>"
            for topic in topics
        ]
    )
    st.markdown(
        f"""
        <article class='glass-panel card p-8' style='height: 100%; display: flex; flex-direction: column; margin-bottom: 1.5rem;'>
            <div style='margin-bottom: 1rem; display: inline-flex; border-radius: 999px; padding: 0.5rem 0.75rem; font-size: 0.875rem; font-weight: 600; {gradient_style}'>{title}</div>
            <h2 style='font-size: 1.5rem; font-weight: 600; letter-spacing: -0.025em; color: #ffffff; margin: 0;'>{title} Essentials</h2>
            <p style='margin-top: 0.75rem; color: #cbd5e1; flex-grow: 1;'>{description}</p>
            <div style='margin-top: 1.5rem; display: flex; flex-wrap: wrap; gap: 0.5rem; font-size: 0.875rem; color: #e2e8f0;'>{topic_html}</div>
            <div style='margin-top: 2rem; display: flex; align-items: center; justify-content: space-between;'>
                <span style='font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.2em; color: #64748b;'>Designed for learners</span>
                <span style='border-radius: 999px; background: rgba(255, 255, 255, 0.05); padding: 0.25rem 0.75rem; font-size: 0.75rem; color: #cbd5e1;'>Explore</span>
            </div>
        </article>
        """,
        unsafe_allow_html=True,
    )


def render_practice_card(title, description, items, accent=""):
    gradient_style = f"background: linear-gradient(135deg, {accent});" if accent else ""
    items_html = "".join(
        [
            f"""
        <li style='display: flex; align-items: center; gap: 0.75rem; border-radius: 1rem; background: rgba(255, 255, 255, 0.05); padding: 0.75rem 1rem; margin-bottom: 0.75rem;'>
            <span style='color: #6ee7b7;'>•</span>
            <span>{item}</span>
        </li>
        """
            for item in items
        ]
    )
    st.markdown(
        f"""
        <article class='glass-panel card p-8' style='height: 100%; display: flex; flex-direction: column; margin-bottom: 1.5rem;'>
            <div style='display: inline-flex; border-radius: 999px; {gradient_style} padding: 0.5rem 0.75rem; font-size: 0.875rem; font-weight: 600; color: #ffffff; align-self: flex-start;'>{title}</div>
            <h2 style='margin-top: 1.5rem; font-size: 1.5rem; font-weight: 600; color: #ffffff; margin: 0;'>{title}</h2>
            <p style='margin-top: 0.75rem; color: #cbd5e1; flex-grow: 1;'>{description}</p>
            <ul style='margin-top: 1.5rem; padding: 0; list-style: none; color: #e2e8f0; margin-bottom: 0;'>{items_html}</ul>
        </article>
        """,
        unsafe_allow_html=True,
    )


def render_content_card(title, body):
    st.markdown(
        f"""
        <div class='glass-panel card content-card'>
            <h3>{title}</h3>
            <p>{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_team_member(name, role):
    st.markdown(
        f"""
        <div class='glass-panel card team-card'>
            <p class='team-name'>{name}</p>
            <p class='team-role'>{role}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_module_card(title, duration, status):
    st.markdown(
        f"""
        <div class='glass-panel card module-card'>
            <div class='module-card-header'>
                <div>
                    <h4>{title}</h4>
                    <p>{duration}</p>
                </div>
                <span class='module-status'>{status}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown(
        """
        <div class='custom-footer'>
            <div class='custom-footer-inner'>
                <div>
                    <p style='font-weight: 600; color: #f8fafc; margin: 0;'>CodeMentor AI</p>
                    <p style='margin-top: 0.5rem; font-size: 0.875rem; color: #64748b; margin-bottom: 0;'>An intelligent learning experience for programming, English, and Telugu.</p>
                </div>
                <div style='display: flex; flex-wrap: wrap; gap: 1rem; font-size: 0.875rem; color: #94a3b8;'>
                    <span>Terms</span>
                    <span>Privacy</span>
                    <span>Contact</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

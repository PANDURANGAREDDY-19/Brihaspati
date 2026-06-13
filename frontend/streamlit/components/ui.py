import streamlit as st
from pathlib import Path


def inject_css():
    css_path = Path(__file__).resolve().parent.parent / "assets" / "styles.css"
    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def render_page_header(title: str, subtitle: str = ""):
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f"""
        <div class="page-hero">
            <span class="overline">Brihaspati</span>
            <h1>{title}</h1>
            {sub}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_section_header(title: str, subtitle: str = ""):
    sub = (
        f"<p style='color:#64748b;font-size:0.82rem;margin:0.2rem 0 0;'>{subtitle}</p>"
        if subtitle
        else ""
    )
    st.markdown(
        f"""
        <div style="margin-bottom:0.75rem;">
            <h4 style="color:#6ee7b7;font-size:0.78rem;text-transform:uppercase;
                       letter-spacing:0.18em;margin:0;">{title}</h4>
            {sub}
        </div>
        """,
        unsafe_allow_html=True,
    )


def chat_bubble(sender: str, text: str, ai: bool = True, ts: str = ""):
    ts_html = f"<div class='msg-time'>{ts}</div>" if ts else ""
    role = "ai" if ai else "user"
    avatar = "🤖" if ai else "🙂"
    st.markdown(
        f"""
        <div class="msg-row {role}">
            <div class="msg-avatar {role}">{avatar}</div>
            <div class="msg-bubble {role}">
                <div class="msg-label">{sender}</div>
                <div>{text}</div>
                {ts_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_stat_card(label: str, value: str, detail: str, accent: str = ""):
    bg = (
        f"background: linear-gradient(135deg, {accent});"
        if accent
        else "background: rgba(139,92,246,0.3);"
    )
    st.markdown(
        f"""
        <div class="stat-card">
            <span class="stat-badge" style="{bg}">{label}</span>
            <p class="stat-value">{value}</p>
            <p class="stat-detail">{detail}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_course_card(title: str, description: str, topics: list, accent: str = ""):
    pills = "".join(
        f"<span style='background:rgba(255,255,255,0.05);border-radius:999px;"
        f"padding:0.35rem 0.75rem;font-size:0.8rem;color:#e2e8f0;'>{t}</span>"
        for t in topics
    )
    st.markdown(
        f"""
        <div class="glass-panel" style="height:100%;">
            <h3 style="color:#fff;font-size:1.15rem;margin:0 0 0.5rem;">{title}</h3>
            <p style="color:#94a3b8;font-size:0.88rem;margin:0 0 1rem;line-height:1.6;">{description}</p>
            <div style="display:flex;flex-wrap:wrap;gap:0.4rem;">{pills}</div>
            <div style="margin-top:1.25rem;font-size:0.75rem;text-transform:uppercase;
                        letter-spacing:0.2em;color:#475569;">Designed for learners</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_practice_card(title: str, description: str, items: list, accent: str = ""):
    bg = (
        f"background: linear-gradient(135deg, {accent});"
        if accent
        else "background: rgba(139,92,246,0.4);"
    )
    rows = "".join(
        f"<li style='padding:0.6rem 0.9rem;border-radius:12px;"
        f"background:rgba(255,255,255,0.04);margin-bottom:0.5rem;"
        f"font-size:0.875rem;color:#e2e8f0;'>"
        f"<span style='color:#6ee7b7;margin-right:0.5rem;'>•</span>{item}</li>"
        for item in items
    )
    st.markdown(
        f"""
        <div class="glass-panel" style="height:100%;">
            <span style="{bg} border-radius:999px;padding:0.3rem 0.8rem;
                          font-size:0.75rem;font-weight:600;color:#fff;">{title}</span>
            <p style="color:#94a3b8;font-size:0.88rem;margin:0.75rem 0 0.75rem;line-height:1.6;">{description}</p>
            <ul style="list-style:none;padding:0;margin:0;">{rows}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_content_card(title: str, body: str):
    st.markdown(
        f"""
        <div class="glass-panel">
            <h3 style="color:#f8fafc;margin:0 0 0.5rem;">{title}</h3>
            <p style="color:#94a3b8;margin:0;font-size:0.9rem;line-height:1.6;">{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_team_member(name: str, role: str):
    st.markdown(
        f"""
        <div class="glass-panel" style="text-align:center;padding:1.5rem;">
            <div style="width:48px;height:48px;border-radius:50%;
                        background:linear-gradient(135deg,#8b5cf6,#10b981);
                        display:grid;place-items:center;font-size:1.3rem;
                        margin:0 auto 0.75rem;">👤</div>
            <p style="color:#f8fafc;font-weight:600;margin:0;">{name}</p>
            <p style="color:#64748b;font-size:0.82rem;margin:0.3rem 0 0;">{role}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_module_card(title: str, duration: str, status: str):
    st.markdown(
        f"""
        <div class="module-row">
            <div>
                <h4>{title}</h4>
                <p>{duration}</p>
            </div>
            <span class="status-pill">{status}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown(
        """
        <div class="app-footer">
            <div>
                <span class="name">Brihaspati</span>
                <span style="margin-left:0.5rem;">— Bilingual Coding Assistant</span>
            </div>
            <div style="display:flex;gap:1.5rem;">
                <span>Terms</span><span>Privacy</span><span>Contact</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

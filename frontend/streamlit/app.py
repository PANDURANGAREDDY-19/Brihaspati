import streamlit as st
from components.locale import load_locale
from components.ui import inject_css, render_footer
from components.chatbot import render as render_chatbot

PAGES = {
    "home": "pages.home",
    "courses": "pages.courses",
    "dashboard": "pages.dashboard",
    "practice": "pages.practice",
    "about": "pages.about",
    "ai_tutor": "pages.ai_tutor",
    "code_review": "pages.code_review",
    "challenges": "pages.challenges",
    "debugger": "pages.debugger",
    "quiz_arena": "pages.quiz_arena",
    "settings": "pages.settings",
}

NAV_ORDER = [
    "home",
    "courses",
    "dashboard",
    "practice",
    "about",
    "ai_tutor",
    "code_review",
    "challenges",
    "debugger",
    "quiz_arena",
    "settings",
]


def ensure_state():
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "lang" not in st.session_state:
        st.session_state.lang = "en"
    if "search_query" not in st.session_state:
        st.session_state.search_query = ""


def render_header(locale):
    cols = st.columns([0.65, 0.35], gap="large", vertical_alignment="center")
    with cols[0]:
        st.markdown(
            """
            <div class='top-brand' style='display: flex; align-items: center; gap: 1rem;'>
                <div class='brand-mark' style='background: linear-gradient(135deg, #8b5cf6, #10b981); width: 48px; height: 48px; border-radius: 24px; display: grid; place-items: center; color: #ffffff; font-weight: 700; font-size: 1.25rem; box-shadow: 0 10px 20px rgba(139, 92, 246, 0.2);'>CM</div>
                <div>
                    <p class='brand-overline' style='margin: 0; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.3em; color: #6ee7b7;'>CodeMentor AI</p>
                    <h1 class='brand-title' style='margin: 0.25rem 0 0; font-size: 1.75rem; font-weight: 600; color: #ffffff;'>Learn. Practice. Build. Grow.</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with cols[1]:
        st.text_input(
            "Search",
            key="search_query",
            placeholder="Search courses, topics, lessons",
            label_visibility="collapsed",
        )

    st.markdown(
        "<div style='border-bottom: 1px solid rgba(255, 255, 255, 0.1); margin: 1.5rem 0;'></div>",
        unsafe_allow_html=True,
    )

    nav_labels = locale.get("nav", {})
    nav_cols = st.columns(len(NAV_ORDER), gap="small")
    for idx, page_key in enumerate(NAV_ORDER):
        label = nav_labels.get(page_key, page_key.replace("_", " ").title())
        active = st.session_state.page == page_key
        if nav_cols[idx].button(
            label, key=f"nav_{page_key}", disabled=active, use_container_width=True
        ):
            st.session_state.page = page_key
            st.rerun()


def main():
    st.set_page_config(
        page_title="CodeMentor AI",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    ensure_state()
    inject_css()
    locale = load_locale(st.session_state.lang)
    render_header(locale)

    page_module = __import__(
        PAGES.get(st.session_state.page, "pages.home"), fromlist=["*"]
    )
    page_module.render(locale)

    render_footer()
    render_chatbot(locale)


if __name__ == "__main__":
    main()

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
    col_brand, col_search = st.columns(
        [0.65, 0.35], gap="large", vertical_alignment="center"
    )
    with col_brand:
        st.markdown(
            """
            <div class="brand-bar">
                <div class="brand-mark">CM</div>
                <div>
                    <p class="brand-overline">CodeMentor AI · Brihaspati</p>
                    <h1 class="brand-title">Learn. Practice. Build. Grow.</h1>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_search:
        st.text_input(
            "Search",
            key="search_query",
            placeholder="Search courses, topics, lessons…",
            label_visibility="collapsed",
        )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

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
        page_title="Brihaspati · CodeMentor AI",
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

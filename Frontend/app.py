import streamlit as st
from components.locale import load_locale
from components.ui import inject_css
from components.sidebar import render_sidebar
from pages import ai_coach, bug_finder, challenges, dashboard, learn_concepts, progress_tracker, quiz_lab, settings

# Navigation order (professional SaaS order)
NAV_ITEMS = [
    "dashboard",
    "ai_coach",
    "bug_finder",
    "quiz_lab",
    "challenges",
    "learn_concepts",
    "progress_tracker",
    "settings",
]

LANGUAGE_CODES = {"English": "en", "Telugu": "te", "Hindi": "hi"}


def ensure_state():
    if "navigation" not in st.session_state:
        st.session_state.navigation = "dashboard"
    if "theme" not in st.session_state:
        st.session_state.theme = "Light"
    if "language" not in st.session_state:
        st.session_state.language = "English"
    if "provider" not in st.session_state:
        st.session_state.provider = "OpenAI"
    if "ai_key" not in st.session_state:
        st.session_state.ai_key = ""


def main():
    st.set_page_config(page_title="CodeGuru AI", page_icon="🚀", layout="wide")
    ensure_state()
    locale = load_locale(LANGUAGE_CODES.get(st.session_state.language, "en"))
    inject_css(st.session_state.theme)

    # Render the redesigned collapsible sidebar
    with st.sidebar:
        new_page = render_sidebar(locale, NAV_ITEMS, st.session_state.get("navigation", "dashboard"))
        if new_page:
            st.session_state.navigation = new_page

    page = st.session_state.navigation

    if page == "dashboard":
        dashboard.render(locale)
    elif page == "learn_concepts":
        learn_concepts.render(locale)
    elif page == "ai_coach":
        ai_coach.render(locale)
    elif page == "bug_finder":
        bug_finder.render(locale)
    elif page == "quiz_lab":
        quiz_lab.render(locale)
    elif page == "challenges":
        challenges.render(locale)
    elif page == "progress_tracker":
        progress_tracker.render(locale)
    elif page == "settings":
        settings.render(locale, st.session_state)


if __name__ == "__main__":
    main()

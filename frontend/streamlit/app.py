import streamlit as st
from components.locale import load_locale
from components.sidebar import render as render_sidebar
from components.ui import inject_css

PAGES = {
    'home': 'pages.dashboard',
    'ai_tutor': 'pages.ai_tutor',
    'debugger': 'pages.debugger',
    'quiz_arena': 'pages.quiz_arena',
    'challenges': 'pages.challenges',
    'code_review': 'pages.code_review',
    'settings': 'pages.settings',
}


def ensure_state():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'lang' not in st.session_state:
        st.session_state.lang = 'en'
    if 'collapsed' not in st.session_state:
        st.session_state.collapsed = False


def main():
    st.set_page_config(
        page_title='CodeMentor AI',
        page_icon='🤖',
        layout='wide',
        initial_sidebar_state='collapsed',
    )
    ensure_state()
    inject_css()

    locale = load_locale(st.session_state.lang)
    st.markdown("<div class='app-shell'>", unsafe_allow_html=True)

    cols = st.columns([0.22, 0.78], gap='large')
    with cols[0]:
        selected = render_sidebar(locale, st.session_state.page)
        if selected:
            st.session_state.page = selected

    with cols[1]:
        page_module = PAGES.get(st.session_state.page, 'pages.dashboard')
        module = __import__(page_module, fromlist=['*'])
        module.render(locale)

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == '__main__':
    main()

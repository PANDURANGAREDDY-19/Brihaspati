import streamlit as st
from components.locale import load_locale
from components.ui import inject_css, render_footer
from components.chatbot import render as render_chatbot

PAGES = {
    'home': 'pages.home',
    'courses': 'pages.courses',
    'dashboard': 'pages.dashboard',
    'practice': 'pages.practice',
    'about': 'pages.about',
}

NAV_ITEMS = [
    {'label': 'Home', 'page': 'home'},
    {'label': 'Courses', 'page': 'courses'},
    {'label': 'Dashboard', 'page': 'dashboard'},
    {'label': 'Practice', 'page': 'practice'},
    {'label': 'About', 'page': 'about'},
]


def ensure_state():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    if 'lang' not in st.session_state:
        st.session_state.lang = 'en'
    if 'search_query' not in st.session_state:
        st.session_state.search_query = ''


def render_header(locale):
    cols = st.columns([0.65, 0.35], gap='large', vertical_alignment='center')
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
        st.markdown(
            """
            <div class='search-shell' style='position: relative; width: 100%;'>
                <span class='search-icon' style='position: absolute; left: 1rem; top: 50%; transform: translateY(-50%); color: #94a3b8; pointer-events: none; z-index: 10;'>🔍</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.text_input('Search', key='search_query', placeholder='Search courses, topics, lessons', label_visibility='collapsed')

    st.markdown("<div style='border-bottom: 1px solid rgba(255, 255, 255, 0.1); margin-top: 1.5rem; margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)

    nav_widths = [1.0, 1.4, 1.6, 1.5, 1.1, 8.0]
    nav_cols = st.columns(nav_widths, gap='small')
    for idx, item in enumerate(NAV_ITEMS):
        active = st.session_state.page == item['page']
        if nav_cols[idx].button(item['label'], key=f"nav_{item['page']}", disabled=active):
            st.session_state.page = item['page']
            st.rerun()


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
    render_header(locale)

    page_module = __import__(PAGES.get(st.session_state.page, 'pages.home'), fromlist=['*'])
    page_module.render(locale)

    render_footer()

    render_chatbot(locale)



if __name__ == '__main__':
    main()

import streamlit as st
from components.ui import render_page_header, render_section_header

MOCK_REVIEW = {
    'score': 78,
    'suggestions': [
        'Break large functions into smaller helpers.',
        'Avoid global mutable state for testability.',
        'Add input validation for edge cases.'
    ],
    'performance': ['Use list comprehensions instead of loops where possible.'],
    'security': ['Sanitize user inputs before processing.']
}

def render(locale):
    st.markdown(f"<h2>{locale['review']['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color:var(--muted);'>{locale['review']['subtitle']}</div>", unsafe_allow_html=True)

    code = st.text_area(locale['review']['paste'], value='# Paste code here', height=320)
    if st.button(locale['review']['analyze']):
        st.markdown("<div class='card' style='margin-top:0.8rem;'>", unsafe_allow_html=True)
        render_section_header(locale['review']['quality'])
        st.markdown(f"<div style='font-size:26px; font-weight:800;'>{MOCK_REVIEW['score']}%</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div class='card' style='margin-top:0.8rem;'>", unsafe_allow_html=True)
        render_section_header(locale['review']['improvements'])
        for s in MOCK_REVIEW['suggestions']:
            st.markdown(f"<div style='margin-bottom:0.5rem;'>{s}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
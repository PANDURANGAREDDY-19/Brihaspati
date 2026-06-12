import streamlit as st
from components.ui import render_section_header

MOCK_ISSUES = {
    "Python": [
        {"issue": "Unused variable 'temp'", "severity": "Low", "fix": "Remove the unused variable or use it in logic.", "code": "def calculate(items):\n    total = 0\n    for item in items:\n        total += item\n    return total\n"},
        {"issue": "Missing return in recursive function", "severity": "High", "fix": "Add a return statement for the recursive path.", "code": "def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\n"},
    ],
    "JavaScript": [
        {"issue": "Potential null reference", "severity": "Medium", "fix": "Check that `response` exists before using properties.", "code": "const value = response ? response.data : null;"},
    ],
    "C": [
        {"issue": "Buffer overflow risk", "severity": "High", "fix": "Use snprintf and validate input length.", "code": "char buffer[32]; snprintf(buffer, sizeof(buffer), \"%s\", input);"},
    ],
}


def render(locale):
    st.markdown(f"<h2 style='margin-bottom:0.1rem;'>{locale['bug_finder']['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: var(--muted); margin-bottom:1.5rem;'>{locale['bug_finder']['subtitle']}</div>", unsafe_allow_html=True)

    language = st.selectbox(locale['bug_finder']['choose_language'], ["Python", "JavaScript", "C"])
    col_editor, col_issues = st.columns([2, 1], gap='large')
    with col_editor:
        code = st.text_area(locale['bug_finder']['code_placeholder'], value="# Paste your code here\n", height=420)
        if st.button(locale['bug_finder']['analyze_button']):
            st.session_state._last_code = code
            st.session_state._last_lang = language
            st.experimental_rerun()

    with col_issues:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        render_section_header(locale['bug_finder']['detected_issues'])
        issues = MOCK_ISSUES.get(st.session_state.get('_last_lang', language), [])
        if issues:
            for issue in issues:
                sev = issue['severity']
                badge = 'badge-warning' if sev in ['Medium', 'Low'] else 'badge-danger'
                st.markdown(f"<div style='margin-bottom:0.8rem;'><strong>{issue['issue']}</strong> <span class='small-badge {badge}'>{issue['severity']}</span><div style='color:var(--muted); margin-top:0.4rem;'>{issue['fix']}</div></div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card' style='margin-top:1rem;'><div class='section-title'>{locale['bug_finder']['corrected_code']}</div>", unsafe_allow_html=True)
            st.code(issues[0]['code'], language=st.session_state.get('_last_lang','python').lower())
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='color:var(--muted);'>{locale['bug_finder']['no_issues']}</div>", unsafe_allow_html=True)

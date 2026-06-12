import streamlit as st
from components.ui import render_page_header, render_section_header

SAMPLES = {
    "Python": {
        "code": "def add(a,b):\n    return a + b\n\nprint(add(5))",
        "issues": ["Missing second argument in function call on line 3"],
    },
    "JavaScript": {
        "code": "function add(a,b) {\n  return a + b;\n}\n\nconsole.log(add(5));",
        "issues": ["Missing second argument in function call"],
    },
}


def render(locale):
    render_page_header(locale["debugger"]["title"], locale["debugger"]["subtitle"])

    lang = st.selectbox(locale["debugger"]["language"], list(SAMPLES.keys()))
    st.text_area(
        locale["debugger"]["editor_placeholder"],
        value=SAMPLES[lang]["code"],
        height=320,
    )

    if st.button(locale["debugger"]["analyze"], type="primary"):
        st.markdown(
            "<div class='glass-panel' style='padding:1rem; border-radius:1rem; margin-top:1rem;'>",
            unsafe_allow_html=True,
        )
        render_section_header(locale["debugger"]["detected"])
        issues = SAMPLES[lang]["issues"]
        if issues:
            for issue in issues:
                st.markdown(
                    f"<div style='margin-bottom:0.5rem;'>🔴 {issue}</div>",
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                f"<div style='color:#10b981;'>{locale['debugger']['clean']}</div>",
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)

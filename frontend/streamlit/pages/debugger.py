import streamlit as st
from components.ui import render_page_header

SAMPLES = {
    "Python": {
        "code": "def add(a, b):\n    return a + b\n\nprint(add(5))",
        "issues": [
            "Missing second argument in function call on line 4 — add() requires 2 args."
        ],
    },
    "JavaScript": {
        "code": "function add(a, b) {\n  return a + b;\n}\n\nconsole.log(add(5));",
        "issues": ["Missing second argument in function call — add() requires 2 args."],
    },
}


def render(locale):
    render_page_header(locale["debugger"]["title"], locale["debugger"]["subtitle"])

    lang = st.selectbox(locale["debugger"]["language"], list(SAMPLES.keys()))
    st.text_area(
        locale["debugger"]["editor_placeholder"],
        value=SAMPLES[lang]["code"],
        height=280,
        key="debugger_code",
    )

    col_btn, _ = st.columns([1, 3])
    with col_btn:
        run = st.button(
            locale["debugger"]["analyze"], type="primary", use_container_width=True
        )

    if run:
        issues = SAMPLES[lang]["issues"]
        if issues:
            issue_html = "".join(
                f'<div style="display:flex;gap:0.6rem;align-items:flex-start;'
                f'margin-bottom:0.5rem;font-size:0.9rem;color:#e2e8f0;">'
                f"<span>🔴</span><span>{i}</span></div>"
                for i in issues
            )
            st.markdown(
                f"""
                <div class="result-panel">
                    <div class="result-section">
                        <h4>{locale["debugger"]["detected"]}</h4>
                        {issue_html}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="result-panel">
                    <div class="result-section">
                        <h4>{locale["debugger"]["detected"]}</h4>
                        <div style="color:#22c55e;font-size:0.9rem;">{locale["debugger"]["clean"]}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

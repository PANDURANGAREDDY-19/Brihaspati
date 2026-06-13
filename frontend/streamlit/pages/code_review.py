import streamlit as st
import asyncio
from components.ui import render_page_header
from api_client import review_code


def render(locale):
    render_page_header(locale["review"]["title"], locale["review"]["subtitle"])

    code = st.text_area(
        locale["review"]["paste"], value="# Paste your code here", height=300
    )
    lang = st.selectbox("Language", ["python", "javascript", "java", "cpp"])

    col_btn, _ = st.columns([1, 3])
    with col_btn:
        run = st.button(
            locale["review"]["analyze"], type="primary", use_container_width=True
        )

    if run:
        if not code.strip() or code.strip() == "# Paste your code here":
            st.warning("Please paste some code before reviewing.")
            return
        with st.spinner("Reviewing code…"):
            try:
                result = asyncio.run(review_code(code, lang))
            except Exception as e:
                st.error(f"Review failed: {e}")
                return

        summary = result.get("summary", "")
        issues = result.get("issues", [])
        suggestions = result.get("suggestions", [])
        corrected = result.get("corrected_code")

        # ── Summary ──
        if summary:
            st.markdown(
                f"""
                <div class="result-panel">
                    <div class="result-section">
                        <h4>Review Summary</h4>
                        <div class="body">{summary}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ── Issues ──
        if issues:
            issue_rows = "".join(
                f"""<div class="issue-row">
                        <span>{"🔴" if isinstance(i,dict) and i.get("severity") in ("critical","major") else "🔵"}</span>
                        <span>{i.get("message", i) if isinstance(i, dict) else i}</span>
                    </div>"""
                for i in issues
            )
            st.markdown(
                f"""
                <div class="result-panel">
                    <div class="result-section">
                        <h4>Issues Found</h4>
                        {issue_rows}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ── Suggestions ──
        if suggestions:
            sug_rows = "".join(
                f'<div class="suggestion-row"><span>💡</span><span>{s}</span></div>'
                for s in suggestions
            )
            st.markdown(
                f"""
                <div class="result-panel">
                    <div class="result-section">
                        <h4>Suggestions</h4>
                        {sug_rows}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # ── Corrected code ──
        if corrected:
            st.markdown(
                """
                <div class="result-panel">
                    <div class="result-section"><h4>Corrected Code</h4></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.code(corrected, language=lang)

        if not any([summary, issues, suggestions, corrected]):
            st.info("No issues found. Your code looks good!")

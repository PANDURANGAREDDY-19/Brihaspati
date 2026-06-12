import streamlit as st
import asyncio
from components.ui import render_page_header, render_section_header
from api_client import review_code


def render(locale):
    render_page_header(locale["review"]["title"], locale["review"]["subtitle"])

    code = st.text_area("Paste your code", value="# Paste your code here", height=320)
    lang = st.selectbox("Language", ["python", "javascript", "java", "cpp"])

    if st.button(locale["review"]["analyze"], type="primary"):
        with st.spinner("Reviewing code..."):
            try:
                result = asyncio.run(review_code(code, lang))
                summary = result.get("summary", "")

                st.markdown(
                    "<div class='glass-panel' style='padding:1rem; border-radius:1rem; margin-top:1rem;'>",
                    unsafe_allow_html=True,
                )
                render_section_header("Review Results")
                if summary:
                    st.markdown(
                        f"<div style='margin-top:0.5rem;'>{summary}</div>",
                        unsafe_allow_html=True,
                    )

                issues = result.get("issues", [])
                if issues:
                    st.markdown(
                        "<div style='margin-top:1rem;'>", unsafe_allow_html=True
                    )
                    render_section_header("Issues Found")
                    for issue in issues:
                        msg = (
                            issue.get("message", issue)
                            if isinstance(issue, dict)
                            else issue
                        )
                        sev = (
                            issue.get("severity", "info")
                            if isinstance(issue, dict)
                            else "info"
                        )
                        icon = {
                            "critical": "🔴",
                            "major": "🟡",
                            "minor": "🔵",
                            "info": "ℹ️",
                        }.get(sev, "ℹ️")
                        st.markdown(
                            f"<div style='margin-bottom:0.3rem;'>{icon} {msg}</div>",
                            unsafe_allow_html=True,
                        )
                    st.markdown("</div>", unsafe_allow_html=True)

                suggestions = result.get("suggestions", [])
                if suggestions:
                    st.markdown(
                        "<div style='margin-top:1rem;'>", unsafe_allow_html=True
                    )
                    render_section_header("Suggestions")
                    for s in suggestions:
                        st.markdown(
                            f"<div style='margin-bottom:0.3rem;'>💡 {s}</div>",
                            unsafe_allow_html=True,
                        )
                    st.markdown("</div>", unsafe_allow_html=True)

                corrected = result.get("corrected_code")
                if corrected:
                    st.markdown(
                        "<div style='margin-top:1rem;'>", unsafe_allow_html=True
                    )
                    render_section_header("Corrected Code")
                    st.code(corrected, language=lang)
                    st.markdown("</div>", unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Review failed: {e}")

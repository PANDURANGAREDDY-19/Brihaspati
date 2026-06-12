import streamlit as st
import asyncio
from components.ui import render_page_header
from api_client import check_health, get_backend_url, set_backend_url


def render(locale):
    render_page_header(locale["settings"]["title"], locale["settings"]["subtitle"])

    col1, col2 = st.columns(2, gap="large")
    with col1:
        lang_label = st.selectbox(
            locale["settings"]["language_label"],
            ["English", "తెలుగు"],
            index=0 if st.session_state.lang == "en" else 1,
        )
        new_lang = "te" if lang_label == "తెలుగు" else "en"
        if new_lang != st.session_state.lang:
            st.session_state.lang = new_lang
            st.rerun()

        backend_url = st.text_input(
            "Backend API URL",
            value=get_backend_url(),
            help="e.g. http://localhost:8000",
        )
        if backend_url != get_backend_url():
            set_backend_url(backend_url)
            st.success("Backend URL updated")

        if st.button("Check Connection", type="primary"):
            with st.spinner("Checking backend..."):
                health = asyncio.run(check_health())
                if health.get("status") == "healthy":
                    st.success(f"Connected — v{health.get('version', '?')}")
                elif health.get("status") == "degraded":
                    st.warning(
                        f"Degraded — Ollama: {health.get('ollama_connected', False)}"
                    )
                else:
                    st.error(
                        f"Unreachable — {health.get('error', 'Connection failed')}"
                    )

    with col2:
        st.markdown(
            "<div class='glass-panel' style='padding:1rem; border-radius:1rem;'>",
            unsafe_allow_html=True,
        )
        st.markdown("<strong>System Info</strong>", unsafe_allow_html=True)
        st.markdown(
            f"**Language:** {'తెలుగు' if st.session_state.lang == 'te' else 'English'}"
        )
        st.markdown(f"**Backend:** {get_backend_url()}")
        st.markdown("</div>", unsafe_allow_html=True)

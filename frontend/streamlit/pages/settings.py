import streamlit as st
import asyncio
from components.ui import render_page_header
from api_client import check_health, get_backend_url, set_backend_url


def render(locale):
    render_page_header(locale["settings"]["title"], locale["settings"]["subtitle"])

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="glass-panel" style="margin-bottom:0.75rem;">
                <p style="color:#6ee7b7;font-size:0.78rem;text-transform:uppercase;
                           letter-spacing:0.18em;margin:0;">Configuration</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

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
            st.success("Backend URL updated.")

        if st.button("Check Connection", type="primary", use_container_width=True):
            with st.spinner("Checking backend…"):
                health = asyncio.run(check_health())
            status = health.get("status", "unreachable")
            if status == "healthy":
                st.success(f"✅ Connected — v{health.get('version', '?')}")
            elif status == "degraded":
                st.warning(
                    f"⚠️ Degraded — Ollama: {health.get('ollama_connected', False)}"
                )
            else:
                st.error(f"❌ Unreachable — {health.get('error', 'Connection failed')}")

    with col2:
        lang_display = "తెలుగు" if st.session_state.lang == "te" else "English"
        st.markdown(
            f"""
            <div class="settings-panel">
                <h4 style="color:#6ee7b7;font-size:0.78rem;text-transform:uppercase;
                            letter-spacing:0.18em;margin:0 0 1rem;">System Info</h4>
                <div class="info-row">
                    <span class="key">UI Language</span>
                    <span class="val">{lang_display}</span>
                </div>
                <div class="info-row">
                    <span class="key">Backend URL</span>
                    <span class="val">{get_backend_url()}</span>
                </div>
                <div class="info-row">
                    <span class="key">AI Engine</span>
                    <span class="val">Ollama (local)</span>
                </div>
                <div class="info-row" style="border:none;">
                    <span class="key">Version</span>
                    <span class="val">1.0.0</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

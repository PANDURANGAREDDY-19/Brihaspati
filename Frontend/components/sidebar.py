import streamlit as st

NAV_ICONS = {
    "dashboard": "🏠",
    "ai_coach": "💬",
    "bug_finder": "🐞",
    "quiz_lab": "🧠",
    "challenges": "⚔️",
    "learn_concepts": "📚",
    "progress_tracker": "📈",
    "settings": "⚙️",
}


def render_sidebar(locale: dict, nav_order: list, current: str):
    # initialize sidebar state
    if "sidebar_collapsed" not in st.session_state:
        st.session_state.sidebar_collapsed = False

    # header with collapse toggle
    cols = st.columns([8, 1])
    with cols[0]:
        st.markdown(f"<div style='padding:0.35rem 0; font-weight:700; font-size:18px;'>CodeGuru AI</div>", unsafe_allow_html=True)
    with cols[1]:
        if st.button("☰", key="sidebar_toggle"):
            st.session_state.sidebar_collapsed = not st.session_state.sidebar_collapsed
            st.experimental_rerun()

    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

    # Navigation items
    for key in nav_order:
        label = locale.get("nav", {}).get(key, key)
        icon = NAV_ICONS.get(key, "🔹")
        if st.session_state.sidebar_collapsed:
            btn_label = f"{icon}"
        else:
            # show an arrow for the active page to highlight it
            active_marker = "➡️ " if key == current else ""
            btn_label = f"{active_marker}{icon} {label}"
        if st.button(btn_label, key=f"nav_{key}"):
            return key

    st.markdown("---")
    st.markdown(f"<div style='color: var(--muted); font-size:12px;'>Version 1.0 · Demo UI</div>", unsafe_allow_html=True)
    return None

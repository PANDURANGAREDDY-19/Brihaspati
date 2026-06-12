import streamlit as st

NAV_ORDER = [
    "home",
    "courses",
    "dashboard",
    "practice",
    "about",
]

ICONS = {
    "home": "🏠",
    "courses": "🎓",
    "dashboard": "📊",
    "practice": "🧪",
    "about": "ℹ️",
}


def render(locale, current):
    if 'collapsed' not in st.session_state:
        st.session_state.collapsed = False

    st.markdown(
        """
        <div class='sidebar-panel'>
            <div class='sidebar-brand'>
                <div class='brand-mark'>CM</div>
                <div>
                    <div class='brand-label'>CodeMentor AI</div>
                    <div class='brand-subtitle'>Learn. Practice. Build. Grow.</div>
                </div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    toggle_label = "Expand" if st.session_state.collapsed else "Collapse"
    if st.button(toggle_label, key='toggle'):
        st.session_state.collapsed = not st.session_state.collapsed
        st.rerun()

    st.markdown("<div class='sidebar-divider'></div>", unsafe_allow_html=True)

    for key in NAV_ORDER:
        label = locale.get('nav', {}).get(key, key)
        icon = ICONS.get(key, '•')
        if st.session_state.collapsed:
            text = f"{icon}"
        else:
            prefix = '▶ ' if key == current else '  '
            text = f"{prefix}{icon} {label}"
        if st.button(text, key=f"nav_{key}"):
            return key

    st.markdown(
        """
            <div class='sidebar-divider'></div>
            <div class='sidebar-footer'>
                <div>Frontend-only demo</div>
                <div class='sidebar-note'>Premium UI · No backend</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    return None

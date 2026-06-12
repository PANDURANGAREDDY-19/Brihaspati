import streamlit as st

LANGUAGE_OPTIONS = ["English", "Telugu", "Hindi"]
AI_PROVIDERS = ["Ollama", "OpenAI", "Gemini", "Groq"]
THEME_OPTIONS = ["Light", "Dark", "System"]


def render(locale, state):
    st.markdown(f"<h2 style='margin-bottom:0.1rem;'>{locale['settings']['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: var(--muted); margin-bottom:1.5rem;'>{locale['settings']['subtitle']}</div>", unsafe_allow_html=True)

    if 'profile' not in state:
        state.profile = {"name": "Future Engineer", "goal": "Get interview-ready", "preferred_language": "English"}

    col1, col2 = st.columns(2, gap="large")
    with col1:
        state.profile['name'] = st.text_input(locale['settings']['profile_name'], value=state.profile.get('name', ''))
        state.profile['goal'] = st.text_input(locale['settings']['learning_goal'], value=state.profile.get('goal', ''))
        state.profile['preferred_language'] = st.selectbox(locale['settings']['preferred_language'], LANGUAGE_OPTIONS, index=LANGUAGE_OPTIONS.index(state.profile.get('preferred_language','English')))
        state.language = st.selectbox(locale['settings']['language'], LANGUAGE_OPTIONS, index=LANGUAGE_OPTIONS.index(state.language))
        state.provider = st.selectbox(locale['settings']['ai_provider'], AI_PROVIDERS, index=AI_PROVIDERS.index(state.provider))
        state.theme = st.radio(locale['settings']['theme'], THEME_OPTIONS, index=THEME_OPTIONS.index(state.theme if state.theme in THEME_OPTIONS else 0))

    with col2:
        st.markdown("<div class='card' style='padding:1.3rem 1.5rem;'>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-size:1.05rem; font-weight:700; margin-bottom:0.9rem;'>{locale['settings']['byok_title']}</div>", unsafe_allow_html=True)
        state.ai_key = st.text_input(locale['settings']['api_key'], type='password', value=state.ai_key)
        st.markdown(f"<div style='color: var(--muted); margin-top:0.85rem;'>{locale['settings']['byok_desc']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    if st.button(locale['settings']['save_button']):
        st.success(locale['settings']['save_confirm'])
        st.experimental_rerun()

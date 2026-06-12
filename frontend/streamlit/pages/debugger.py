import streamlit as st
from components.ui import render_page_header, render_section_header

SAMPLES = {
    'Python': {
        'code': "def add(a,b):\n    res = a + b\n    print(res)",
        'issues': [{'issue':'Unused variable or missing return','severity':'Medium','fix':'Return the result instead of printing.'}]
    },
    'JavaScript': {
        'code': "function sum(a,b){\n  return a + b;\n}",
        'issues': []
    }
}

def render(locale):
    render_page_header(locale['debugger']['title'], locale['debugger']['subtitle'])

    lang = st.selectbox(locale['debugger']['language'], list(SAMPLES.keys()))
    code = st.text_area(locale['debugger']['editor_placeholder'], value=SAMPLES[lang]['code'], height=320)
    if st.button(locale['debugger']['analyze']):
        st.markdown("<div class='card' style='margin-top:0.8rem;'>", unsafe_allow_html=True)
        render_section_header(locale['debugger']['detected'])
        issues = SAMPLES[lang]['issues']
        if issues:
            for it in issues:
                st.markdown(f"<div><strong>{it['issue']}</strong><div style='color:var(--muted);'>{it['fix']}</div></div>", unsafe_allow_html=True)
        else:
            st.success(locale['debugger']['clean'])
        st.markdown("</div>", unsafe_allow_html=True)

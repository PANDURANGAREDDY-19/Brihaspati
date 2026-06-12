import streamlit as st
from components.ui import render_page_header

CHALS = [
    {'title':'Two Sum','difficulty':'Easy','tags':['Arrays'],'statement':'Find two indices that add to target.','input':'Array and target','output':'Pair of indices','sample_in':'[2,7,11,15],9','sample_out':'[0,1]'},
    {'title':'Valid Parentheses','difficulty':'Medium','tags':['Stack','Strings'],'statement':'Check if parentheses are valid.','input':'String','output':'Boolean','sample_in':'()[]{}','sample_out':'True'},
]

def render(locale):
    render_page_header(locale['challenges']['title'], locale['challenges']['subtitle'])
    for c in CHALS:
        st.markdown("<div class='card' style='margin-bottom:0.8rem;'>", unsafe_allow_html=True)
        st.markdown(f"<div style='display:flex;justify-content:space-between;align-items:center;'><div><strong>{c['title']}</strong><div style='color:var(--muted);'>{', '.join(c['tags'])}</div></div><div><span class='badge {c['difficulty'].lower()}'>{c['difficulty']}</span></div></div>", unsafe_allow_html=True)
        st.markdown(f"<div style='margin-top:0.6rem;color:var(--muted);'>{c['statement']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='margin-top:0.6rem;'><strong>{locale['challenges']['input_format']}:</strong> {c['input']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div><strong>{locale['challenges']['output_format']}:</strong> {c['output']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div><strong>{locale['challenges']['sample_input']}:</strong> {c['sample_in']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div><strong>{locale['challenges']['sample_output']}:</strong> {c['sample_out']}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

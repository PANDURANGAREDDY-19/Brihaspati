import streamlit as st
from components.ui import render_page_header

CHALS = [
    {
        "title": "Two Sum",
        "difficulty": "Easy",
        "tags": ["Arrays"],
        "statement": "Find two indices that add to target.",
        "input": "Array and target",
        "output": "Pair of indices",
        "sample_in": "[2,7,11,15], 9",
        "sample_out": "[0,1]",
    },
    {
        "title": "Valid Parentheses",
        "difficulty": "Medium",
        "tags": ["Stack", "Strings"],
        "statement": "Check if parentheses are valid.",
        "input": "String",
        "output": "Boolean",
        "sample_in": "()[]{}",
        "sample_out": "True",
    },
]


def render(locale):
    render_page_header(locale["challenges"]["title"], locale["challenges"]["subtitle"])

    for c in CHALS:
        level_class = c["difficulty"].lower()
        badge_color = {"easy": "#10b981", "medium": "#f59e0b", "hard": "#ef4444"}.get(
            level_class, "#94a3b8"
        )

        st.markdown(
            f"""
            <div class='glass-panel' style='padding:1rem; border-radius:1rem; margin-bottom:1rem;'>
                <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div>
                        <strong style='font-size:1.1rem; color:#f8fafc;'>{c['title']}</strong>
                        <div style='color:#94a3b8; font-size:0.85rem; margin-top:0.25rem;'>{', '.join(c['tags'])}</div>
                    </div>
                    <span style='background:{badge_color}; padding:0.2rem 0.6rem; border-radius:999px; font-size:0.75rem; font-weight:600; color:#fff;'>{c['difficulty']}</span>
                </div>
                <div style='margin-top:0.75rem; color:#cbd5e1;'>{c['statement']}</div>
                <div style='margin-top:0.75rem; display:grid; grid-template-columns:1fr 1fr; gap:0.5rem; font-size:0.875rem;'>
                    <div><strong style='color:#6ee7b7;'>{locale['challenges']['input_format']}:</strong> <span style='color:#94a3b8;'>{c['input']}</span></div>
                    <div><strong style='color:#6ee7b7;'>{locale['challenges']['output_format']}:</strong> <span style='color:#94a3b8;'>{c['output']}</span></div>
                    <div><strong style='color:#6ee7b7;'>{locale['challenges']['sample_input']}:</strong> <span style='color:#e2e8f0;'>{c['sample_in']}</span></div>
                    <div><strong style='color:#6ee7b7;'>{locale['challenges']['sample_output']}:</strong> <span style='color:#e2e8f0;'>{c['sample_out']}</span></div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

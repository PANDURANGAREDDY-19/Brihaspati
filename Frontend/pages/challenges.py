import streamlit as st
import pandas as pd
from components.ui import render_section_header

CHALLENGES = [
    {
        "title": "Array Pair Sum",
        "difficulty": "Easy",
        "tags": ["Arrays", "Two Pointers"],
        "acceptance": "78%",
        "statement": "Find pairs of numbers that add up to a target value.",
        "input": "An array of integers and a target sum.",
        "output": "All valid pairs that sum to the target.",
        "constraints": "n <= 10^5",
        "sample_input": "[2, 7, 11, 15], target = 9",
        "sample_output": "[(2,7)]",
    },
    {
        "title": "Valid Parentheses",
        "difficulty": "Medium",
        "tags": ["Strings", "Stack"],
        "acceptance": "63%",
        "statement": "Determine whether the parentheses in a string are balanced.",
        "input": "A string containing parentheses characters.",
        "output": "True if the string is valid, otherwise false.",
        "constraints": "length <= 10^4",
        "sample_input": "'()[]{}'",
        "sample_output": "True",
    },
    {
        "title": "Anagram Groups",
        "difficulty": "Hard",
        "tags": ["Hash Maps", "Strings"],
        "acceptance": "41%",
        "statement": "Group words that are anagrams of each other.",
        "input": "A list of lowercase words.",
        "output": "List of grouped anagrams.",
        "constraints": "n <= 2000",
        "sample_input": "['eat','tea','tan','ate']",
        "sample_output": "[['eat','tea','ate'],['tan']]",
    },
]


def render(locale):
    st.markdown(f"<h2 style='margin-bottom:0.1rem;'>{locale['challenges']['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: var(--muted); margin-bottom:1.5rem;'>{locale['challenges']['subtitle']}</div>", unsafe_allow_html=True)

    category = st.selectbox(locale['challenges']['category'], ["Arrays", "Strings", "Hash Maps", "Trees", "Graphs", "Dynamic Programming"])
    matching = [c for c in CHALLENGES if category in c['tags'] or category == "Arrays"]

    for challenge in matching:
        difficulty = challenge['difficulty'].lower()
        badge_class = 'easy' if difficulty == 'easy' else 'medium' if difficulty == 'medium' else 'hard'
        st.markdown("<div class='card' style='margin-bottom:1.4rem;'>", unsafe_allow_html=True)
        st.markdown(
            f"<div style='display:flex; justify-content:space-between; align-items:center;'>"
            f"<div><strong style='font-size:1.1rem;'>{challenge['title']}</strong><div style='color:var(--muted); margin-top:0.35rem;'>{', '.join(challenge['tags'])}</div></div>"
            f"<div style='text-align:right;'><span class='badge {badge_class}'>{challenge['difficulty']}</span><div style='color:var(--muted); margin-top:0.35rem;'>Acceptance: {challenge.get('acceptance','-')}</div></div></div>"
            , unsafe_allow_html=True,
        )
        st.markdown(f"<div style='color: var(--muted); margin:0.75rem 0;'>{challenge['statement']}</div>", unsafe_allow_html=True)
        st.markdown(f"<strong>{locale['challenges']['input_format']}:</strong> {challenge['input']}")
        st.markdown(f"<strong>{locale['challenges']['output_format']}:</strong> {challenge['output']}")
        st.markdown(f"<strong>{locale['challenges']['constraints']}:</strong> {challenge['constraints']}")
        st.markdown(f"<strong>{locale['challenges']['sample_input']}:</strong> {challenge['sample_input']}")
        st.markdown(f"<strong>{locale['challenges']['sample_output']}:</strong> {challenge['sample_output']}")
        st.markdown(f"<div style='margin-top:0.8rem;'><button class='btn-primary'>Attempt</button> <button class='btn-ghost'>Discuss</button></div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

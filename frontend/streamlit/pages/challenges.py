import streamlit as st
from components.ui import render_page_header

CHALS = [
    {
        "title": "Two Sum",
        "difficulty": "Easy",
        "tags": ["Arrays", "Hash Map"],
        "statement": "Given an array of integers and a target, return the indices of two numbers that add up to the target.",
        "input": "Array of integers + target integer",
        "output": "Pair of indices [i, j]",
        "sample_in": "[2, 7, 11, 15], target = 9",
        "sample_out": "[0, 1]",
    },
    {
        "title": "Valid Parentheses",
        "difficulty": "Medium",
        "tags": ["Stack", "Strings"],
        "statement": "Given a string of brackets, determine if the input string is valid (every open bracket is closed in the correct order).",
        "input": "String s",
        "output": "Boolean",
        "sample_in": '"()[]{}"',
        "sample_out": "True",
    },
    {
        "title": "Reverse Linked List",
        "difficulty": "Easy",
        "tags": ["Linked List", "Recursion"],
        "statement": "Reverse a singly linked list and return the reversed list.",
        "input": "Head node of linked list",
        "output": "Head node of reversed list",
        "sample_in": "1 → 2 → 3 → 4 → 5",
        "sample_out": "5 → 4 → 3 → 2 → 1",
    },
]

BADGE_COLORS = {"Easy": "#10b981", "Medium": "#f59e0b", "Hard": "#ef4444"}


def render(locale):
    render_page_header(locale["challenges"]["title"], locale["challenges"]["subtitle"])

    for c in CHALS:
        color = BADGE_COLORS.get(c["difficulty"], "#94a3b8")
        tags_html = " · ".join(c["tags"])
        st.markdown(
            f"""
            <div class="challenge-card">
                <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:1rem;">
                    <div>
                        <div class="c-title">{c["title"]}</div>
                        <div class="c-tags">{tags_html}</div>
                    </div>
                    <span class="difficulty-badge" style="background:{color};">{c["difficulty"]}</span>
                </div>
                <div class="c-body">{c["statement"]}</div>
                <div class="c-meta">
                    <div>
                        <span class="label">{locale["challenges"]["input_format"]}: </span>
                        <span class="val">{c["input"]}</span>
                    </div>
                    <div>
                        <span class="label">{locale["challenges"]["output_format"]}: </span>
                        <span class="val">{c["output"]}</span>
                    </div>
                    <div>
                        <span class="label">{locale["challenges"]["sample_input"]}: </span>
                        <span class="val">{c["sample_in"]}</span>
                    </div>
                    <div>
                        <span class="label">{locale["challenges"]["sample_output"]}: </span>
                        <span class="val">{c["sample_out"]}</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

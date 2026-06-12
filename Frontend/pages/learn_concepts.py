import streamlit as st
from components.ui import render_section_header

CATEGORIES = {
    "Python": [
        {
            "title": "List Comprehensions",
            "difficulty": "Beginner",
            "time": "12 min",
            "description": "Create concise loops and transform collections.",
            "explanation": "List comprehensions let you build lists using compact expressions.",
            "code": "squares = [n * n for n in range(10)]\nprint(squares)",
            "mistakes": "Forgetting the expression order or using brackets incorrectly.",
            "tips": "Start with simple examples, then add conditionals.",
        },
        {
            "title": "OOP Classes",
            "difficulty": "Intermediate",
            "time": "18 min",
            "description": "Model real-world problems using classes and objects.",
            "explanation": "Classes group related data and behavior, making code reusable.",
            "code": "class Student:\n    def __init__(self, name):\n        self.name = name\n\nstudent = Student('Asha')\nprint(student.name)",
            "mistakes": "Using mutable defaults or ignoring encapsulation.",
            "tips": "Keep methods focused and use descriptive names.",
        },
    ],
    "JavaScript": [
        {
            "title": "Async/Await",
            "difficulty": "Intermediate",
            "time": "14 min",
            "description": "Write cleaner asynchronous code with promises.",
            "explanation": "Async functions return promises, allowing `await` inside.",
            "code": "async function loadData() {\n  const response = await fetch('/api/data');\n  const result = await response.json();\n  console.log(result);\n}",
            "mistakes": "Forgetting to handle rejected promises or missing await.",
            "tips": "Use try/catch for network calls and test step-by-step.",
        },
    ],
    "Data Structures": [
        {
            "title": "Hash Maps",
            "difficulty": "Beginner",
            "time": "10 min",
            "description": "Store key-value pairs for fast lookups.",
            "explanation": "Hash maps use a hash function to store and retrieve values quickly.",
            "code": "grades = {'Asha': 94, 'Ravi': 88}\nprint(grades['Asha'])",
            "mistakes": "Using mutable keys or not checking for missing keys.",
            "tips": "Choose clear keys and handle default values gracefully.",
        },
    ],
    "Algorithms": [
        {
            "title": "Binary Search",
            "difficulty": "Intermediate",
            "time": "16 min",
            "description": "Search sorted lists in logarithmic time.",
            "explanation": "Binary search divides the search range until the target is found.",
            "code": "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        if arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n\nprint(binary_search([1,2,3,4], 3))",
            "mistakes": "Wrong midpoint update or off-by-one boundaries.",
            "tips": "Draw the array and track left/right pointers carefully.",
        },
    ],
}


def render(locale):
    st.markdown(f"<h2 style='margin-bottom:0.1rem;'>{locale['learn_concepts']['title']}</h2>", unsafe_allow_html=True)
    st.markdown(f"<div style='color: var(--muted); margin-bottom:1.8rem;'>{locale['learn_concepts']['subtitle']}</div>", unsafe_allow_html=True)

    category = st.selectbox(locale['learn_concepts']['choose_category'], list(CATEGORIES.keys()))
    concepts = CATEGORIES[category]

    grid = st.columns(2, gap="large")
    for index, concept in enumerate(concepts):
        with grid[index % 2]:
            st.markdown(
                f"""
                <div class='card'>
                    <div style='font-size:1.1rem; font-weight:700;'>{concept['title']}</div>
                    <div style='color: var(--muted); margin:0.45rem 0 0.85rem;'>{concept['description']}</div>
                    <div><strong>{locale['learn_concepts']['difficulty']}:</strong> {concept['difficulty']}</div>
                    <div><strong>{locale['learn_concepts']['time']}:</strong> {concept['time']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    selection = st.selectbox(locale['learn_concepts']['view_concept'], [c['title'] for c in concepts])
    detail = next(c for c in concepts if c['title'] == selection)

    st.markdown("<div class='card' style='margin-top:1.5rem;'>", unsafe_allow_html=True)
    render_section_header(detail['title'])
    st.markdown(f"<p>{detail['explanation']}</p>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:1rem;'><strong>Example code</strong></div>")
    st.code(detail['code'], language=category.lower() if category.lower() in ['python', 'javascript'] else 'python')
    st.markdown(f"<div style='margin-top:1rem;'><strong>{locale['learn_concepts']['common_mistakes']}</strong><br>{detail['mistakes']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='margin-top:0.75rem;'><strong>{locale['learn_concepts']['tips']}</strong><br>{detail['tips']}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

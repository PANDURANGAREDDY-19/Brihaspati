import streamlit as st
import asyncio
from components.ui import render_page_header
from api_client import get_backend_url
import httpx


async def generate_quiz(lang: str, topic: str, diff: str) -> list[dict] | None:
    try:
        async with httpx.AsyncClient(timeout=120) as client:
            resp = await client.post(
                f"{get_backend_url()}/api/v1/quiz/generate",
                json={
                    "language": lang,
                    "topic": topic,
                    "difficulty": diff,
                    "num_questions": 5,
                },
            )
            resp.raise_for_status()
            data = resp.json()
            return data.get("questions", [])
    except Exception as e:
        st.error(f"Failed to generate quiz: {e}")
        return None


def render(locale):
    render_page_header(locale["quiz_arena"]["title"], locale["quiz_arena"]["subtitle"])

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        lang = st.selectbox(locale["quiz_arena"]["language"], ["Python", "JavaScript"])
    with col2:
        topic = st.selectbox(
            locale["quiz_arena"]["topic"], ["Lists", "Functions", "Algorithms"]
        )
    with col3:
        diff = st.selectbox(
            locale["quiz_arena"]["difficulty"], ["Easy", "Medium", "Hard"]
        )

    col_btn, _ = st.columns([1, 3])
    with col_btn:
        if st.button(
            locale["quiz_arena"]["generate"], type="primary", use_container_width=True
        ):
            with st.spinner("Generating quiz questions with AI..."):
                questions = asyncio.run(generate_quiz(lang, topic, diff))
            if questions and len(questions) >= 5:
                st.session_state.quiz = questions
                st.session_state.quiz_answers = {}
                st.rerun()
            elif questions:
                st.warning(f"Only {len(questions)} questions generated. Try again.")
            else:
                st.error("Could not generate quiz. Please try again.")

    if "quiz" not in st.session_state:
        return

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    for i, q in enumerate(st.session_state.quiz, start=1):
        st.markdown(
            f"""
            <div class="quiz-card">
                <div class="quiz-q">Q{i}. {q["question"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        choice = st.radio(
            f"Select answer for Q{i}",
            q["options"],
            key=f"quiz_opt_{i}",
            label_visibility="collapsed",
        )
        col_check, _ = st.columns([1, 4])
        with col_check:
            if st.button(
                f"Check Q{i}", key=f"quiz_check_{i}", use_container_width=True
            ):
                st.session_state.quiz_answers[i] = choice

        if i in st.session_state.get("quiz_answers", {}):
            answered = st.session_state.quiz_answers[i]
            if answered == q["answer"]:
                st.success(f"✅ {locale['quiz_arena']['correct']}")
            else:
                st.error(
                    f"❌ {locale['quiz_arena']['incorrect']} Correct: **{q['answer']}**"
                )
            st.info(
                f"💡 {q['explain'] if 'explain' in q else q.get('explanation', '')}"
            )

"""LMS Structure page."""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.header import render_page_header
from components.footer import render_footer
from components.sidebar import render_sidebar_branding
from services.openai_client import OpenAIClient
from services.retrieval import load_knowledge_context


def main() -> None:
    st.set_page_config(page_title="LMS Structure", page_icon="M", layout="wide")

    css_path = Path(__file__).parent.parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

    render_sidebar_branding()
    render_page_header(
        "LMS Structure",
        "Generate a complete Moodle/LMS course structure with weekly modules and activities.",
    )
    st.markdown("---")

    col1, col2 = st.columns(2)
    with col1:
        course_title = st.text_input("Course Title", placeholder="e.g., Data Science Fundamentals")
        duration_weeks = st.number_input("Duration (weeks)", min_value=4, max_value=20, value=16)
    with col2:
        platform = st.selectbox("LMS Platform", ["Moodle", "Canvas", "Blackboard", "Google Classroom"])
        credits = st.number_input("Credits", min_value=1, max_value=20, value=4)

    additional_notes = st.text_area("Additional Notes", placeholder="Any specific requirements...", height=80)

    generate_clicked = st.button("Generate LMS Structure", use_container_width=True)

    if generate_clicked:
        if not course_title:
            st.warning("Please enter a course title.")
            return

        params = {
            "course_title": course_title,
            "duration_weeks": duration_weeks,
            "platform": platform,
            "credits": credits,
            "additional_notes": additional_notes,
        }

        with st.spinner("Generating LMS structure..."):
            client = OpenAIClient()
            context = load_knowledge_context()
            result = client.generate_lms_structure(params, context)

        st.markdown("---")
        st.markdown("### Generated LMS Structure")
        st.markdown(result)

    render_footer()


main()

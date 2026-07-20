"""Generate Course page."""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.header import render_page_header
from components.footer import render_footer
from components.sidebar import render_sidebar_branding
from components.forms import render_course_form
from services.openai_client import OpenAIClient
from services.retrieval import load_knowledge_context


def main() -> None:
    st.set_page_config(page_title="Generate Course", page_icon="M", layout="wide")

    css_path = Path(__file__).parent.parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

    render_sidebar_branding()
    render_page_header(
        "Generate Course",
        "Design a complete micro-credential or credit-based course aligned with NCrF, NHEQF, and OBE principles.",
    )
    st.markdown("---")

    form_data = render_course_form()

    if form_data:
        if not form_data.get("course_title"):
            st.warning("Please enter a course title.")
            return

        with st.spinner("Generating course design..."):
            client = OpenAIClient()
            context = load_knowledge_context()
            result = client.generate_course(form_data, context)

        st.markdown("---")
        st.markdown("### Generated Course Design")
        st.markdown(result)

    render_footer()


main()

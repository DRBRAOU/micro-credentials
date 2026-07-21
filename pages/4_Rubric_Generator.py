"""Rubric Generator page."""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.header import render_page_header
from components.footer import render_footer
from components.sidebar import render_sidebar_branding
from components.forms import render_rubric_form
from services.openai_client import OpenAIClient
from services.retrieval import load_knowledge_context


def main() -> None:
    st.set_page_config(page_title="Rubric Generator", page_icon="M", layout="wide")

    css_path = Path(__file__).parent.parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

    render_sidebar_branding()
    render_page_header(
        "Rubric Generator",
        "Create detailed rubrics with clear performance descriptors for any assessment.",
    )
    st.markdown("---")

    form_data = render_rubric_form()

    if form_data:
        if not form_data.get("assessment_name"):
            st.warning("Please enter an assessment name.")
            return

        with st.spinner("Generating rubric..."):
            client = OpenAIClient()
            context = load_knowledge_context()
            result = client.generate_rubric(form_data, context)

        st.markdown("---")
        st.markdown("### Generated Rubric")
        st.markdown(result)

    render_footer()


main()

"""Assessment Designer page."""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.header import render_page_header
from components.footer import render_footer
from components.sidebar import render_sidebar_branding
from components.forms import render_assessment_form
from services.openai_client import OpenAIClient
from services.retrieval import load_knowledge_context


def main() -> None:
    st.set_page_config(page_title="Assessment Designer", page_icon="M", layout="wide")

    css_path = Path(__file__).parent.parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

    render_sidebar_branding()
    render_page_header(
        "Assessment Designer",
        "Generate OBE-aligned assessments mapped to course outcomes and Bloom's Taxonomy levels.",
    )
    st.markdown("---")

    form_data = render_assessment_form()

    if form_data:
        with st.spinner("Generating assessment..."):
            client = OpenAIClient()
            context = load_knowledge_context()
            result = client.generate_assessment(form_data, context)

        st.markdown("---")
        st.markdown("### Generated Assessment")
        st.markdown(result)

    render_footer()


main()

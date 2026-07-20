"""Improve Course page."""

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
    st.set_page_config(page_title="Improve Course", page_icon="M", layout="wide")

    css_path = Path(__file__).parent.parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

    render_sidebar_branding()
    render_page_header(
        "Improve Course",
        "Paste your existing syllabus to get improvements aligned with NCrF, NHEQF, and OBE standards.",
    )
    st.markdown("---")

    syllabus = st.text_area(
        "Paste Your Syllabus",
        placeholder="Paste the complete course syllabus here...",
        height=300,
    )

    improve_clicked = st.button("Improve Course", use_container_width=True, disabled=(len(syllabus.strip()) == 0))

    if improve_clicked and syllabus.strip():
        with st.spinner("Analyzing and improving syllabus..."):
            client = OpenAIClient()
            context = load_knowledge_context()
            result = client.improve_course(syllabus, context)

        st.markdown("---")
        st.markdown("### Improved Syllabus")
        st.markdown(result)

    render_footer()


main()

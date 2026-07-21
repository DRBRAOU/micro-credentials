"""Micro-Credential Course Designer - Main Entry Point.

Run with: python -m streamlit run app.py
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from components.header import render_header
from components.footer import render_footer
from components.sidebar import render_sidebar_branding
from components.forms import render_course_form
from services.openai_client import OpenAIClient
from services.retrieval import load_knowledge_context


def load_css() -> None:
    """Load custom CSS."""
    css_path = Path(__file__).parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


def main() -> None:
    """Application entry point."""
    st.set_page_config(
        page_title="Micro-Credential Course Designer",
        page_icon="M",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    load_css()
    render_sidebar_branding()
    render_header()

    st.markdown("---")

    # Generate Course form directly on landing page
    st.markdown("### Generate Course")
    st.caption("Fill in the details below to generate a complete course design.")

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


if __name__ == "__main__":
    main()

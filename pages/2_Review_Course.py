"""Review Course page."""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from components.header import render_page_header
from components.footer import render_footer
from components.sidebar import render_sidebar_branding
from services.openai_client import OpenAIClient
from services.retrieval import load_knowledge_context, read_uploaded_file


def main() -> None:
    st.set_page_config(page_title="Review Course", page_icon="M", layout="wide")

    css_path = Path(__file__).parent.parent / "assets" / "styles.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

    render_sidebar_branding()
    render_page_header(
        "Review Course",
        "Upload a course document for review against NCrF, NHEQF, UGC guidelines, and OBE standards.",
    )
    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload Course Document",
        type=["pdf", "docx", "txt"],
        help="Supported formats: PDF, DOCX, TXT",
    )

    if uploaded_file:
        st.caption(f"Uploaded: {uploaded_file.name} ({uploaded_file.size / 1024:.1f} KB)")

    review_clicked = st.button("Review Course", use_container_width=True, disabled=(uploaded_file is None))

    if review_clicked and uploaded_file:
        content = read_uploaded_file(uploaded_file)
        if not content or content.startswith("["):
            st.error(content or "Could not read the file.")
            return

        with st.spinner("Reviewing course document..."):
            client = OpenAIClient()
            context = load_knowledge_context()
            result = client.review_course(content, context)

        st.markdown("---")
        st.markdown("### Review Results")
        st.markdown(result)

    render_footer()


main()

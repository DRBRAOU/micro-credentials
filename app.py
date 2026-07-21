"""Micro-Credential Course Designer - Main Entry Point.

Run with: python -m streamlit run app.py
"""

import streamlit as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from components.header import render_header
from components.footer import render_footer
from components.cards import render_feature_cards
from components.sidebar import render_sidebar_branding
from services.retrieval import get_loaded_documents_info


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

    st.markdown(
        "Designs, reviews, and improves higher education micro-credential and "
        "credit-based courses aligned with NCrF, NHEQF, UGC guidelines, "
        "Bloom's Taxonomy, and Outcome-Based Education (OBE)."
    )

    st.markdown("---")
    st.markdown("### Features")

    features = [
        {"title": "Course Design", "description": "Generate complete course structures with outcomes, units, and assessments."},
        {"title": "Course Review", "description": "Analyze existing courses for framework alignment and gaps."},
        {"title": "Assessment Design", "description": "Create OBE-aligned assessments mapped to Bloom's Taxonomy."},
        {"title": "Rubrics", "description": "Generate criterion-referenced rubrics with performance descriptors."},
        {"title": "LMS Structure", "description": "Design Moodle-ready course layouts with modules and activities."},
        {"title": "Export", "description": "Download course proposals in DOCX, PDF, or Markdown format."},
    ]

    render_feature_cards(features)

    # Knowledge documents status
    st.markdown("---")
    st.markdown("### Knowledge Documents Loaded")
    docs_info = get_loaded_documents_info()
    if docs_info:
        for name, chars in docs_info:
            status = "Loaded" if chars > 0 else "Failed to read"
            st.text(f"  {name} — {status} ({chars:,} chars)")
        st.caption(f"Total: {len(docs_info)} documents")
    else:
        st.text("  No documents found in knowledge/ folder.")

    render_footer()


if __name__ == "__main__":
    main()

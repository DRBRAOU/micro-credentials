"""Header component."""

import streamlit as st
from pathlib import Path


def render_header() -> None:
    """Render the application header with logo and title."""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        logo_path = Path(__file__).parent.parent / "assets" / "logo.png"
        if logo_path.exists():
            st.image(str(logo_path), width=100)
        st.markdown("## Micro-Credential Course Designer")
        st.markdown("**Dr. B.R. Ambedkar Open University**")


def render_page_header(title: str, description: str = "") -> None:
    """Render a page-level header."""
    st.markdown(f"### {title}")
    if description:
        st.caption(description)

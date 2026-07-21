"""Header component."""

import streamlit as st
from pathlib import Path


def render_header() -> None:
    """Render the application header with centered logo, title, and subtitle."""
    logo_path = Path(__file__).parent.parent / "assets" / "logo.png"

    st.markdown(
        """<div style="text-align: center; padding: 1rem 0;">""",
        unsafe_allow_html=True,
    )

    if logo_path.exists():
        import base64
        logo_bytes = logo_path.read_bytes()
        logo_b64 = base64.b64encode(logo_bytes).decode()
        st.markdown(
            f'<div style="text-align: center;"><img src="data:image/png;base64,{logo_b64}" width="100"></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="text-align: center;">
            <h2 style="margin-bottom: 0.25rem;">Micro-Credential Course Designer</h2>
            <p style="font-weight: 600; color: #374151; margin-bottom: 0.5rem;">Dr. B.R. Ambedkar Open University</p>
            <p style="color: #6b7280; max-width: 700px; margin: 0 auto; font-size: 0.9rem; line-height: 1.6;">
                Designs, reviews, and improves higher education micro-credential and 
                credit-based courses aligned with NCrF, NHEQF, UGC guidelines, 
                Bloom's Taxonomy, and Outcome-Based Education (OBE).
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


def render_page_header(title: str, description: str = "") -> None:
    """Render a page-level header."""
    st.markdown(f"### {title}")
    if description:
        st.caption(description)

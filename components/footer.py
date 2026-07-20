"""Footer component."""

import streamlit as st


def render_footer() -> None:
    """Render the application footer."""
    st.markdown("---")
    st.markdown(
        '<div class="footer">Micro-Credential Course Designer v1.0 | '
        "Dr. B.R. Ambedkar Open University</div>",
        unsafe_allow_html=True,
    )

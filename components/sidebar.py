"""Sidebar branding component."""

import streamlit as st


def render_sidebar_branding() -> None:
    """Render sidebar branding below the native navigation."""
    with st.sidebar:
        st.markdown("---")
        st.markdown("**Micro-Credential Course Designer**")
        st.caption("Dr. B.R. Ambedkar Open University")
        st.markdown("---")
        st.caption("Version 1.0")

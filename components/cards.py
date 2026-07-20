"""Card components."""

import streamlit as st
from typing import List, Dict


def render_feature_cards(features: List[Dict[str, str]]) -> None:
    """Render a grid of feature cards."""
    cols = st.columns(3)
    for i, feature in enumerate(features):
        with cols[i % 3]:
            st.markdown(
                f"""<div class="card">
                <div class="card-title">{feature['title']}</div>
                <div class="card-description">{feature['description']}</div>
                </div>""",
                unsafe_allow_html=True,
            )

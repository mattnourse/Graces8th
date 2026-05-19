import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Toy Dash to Grace",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Strip Streamlit chrome so the game fills the screen
st.markdown(
    """
    <style>
      .block-container { padding: 0 !important; max-width: 100% !important; }
      header, footer, #MainMenu { display: none !important; }
      [data-testid="stToolbar"] { display: none !important; }
      .stApp { background: #1a1033; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Read the game HTML from the same folder as this script
html_path = Path(__file__).parent / "toy_dash_to_grace_vs_tala.html"
html = html_path.read_text(encoding="utf-8")

# Render it. Height matches the game's 16:9 logical canvas (800x450) plus
# room for the on-screen control buttons.
components.html(html, height=900, scrolling=False)

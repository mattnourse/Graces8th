import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
 
st.set_page_config(
    page_title="Toy Dash to Grace",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)
 
# Strip ALL Streamlit chrome and make the iframe fill the entire viewport
# so the on-screen game controls stay visible on iPhone.
st.markdown(
    """
    <style>
      html, body, .stApp, [data-testid="stAppViewContainer"], .main, .block-container {
        margin: 0 !important;
        padding: 0 !important;
        max-width: 100% !important;
        width: 100% !important;
        height: 100vh !important;
        overflow: hidden !important;
        background: #1a1033 !important;
      }
      header, footer, #MainMenu, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"],
      [data-testid="stHeader"] { display: none !important; }
 
      /* The iframe Streamlit creates for components.html — make it fill the screen */
      .stApp iframe {
        width: 100vw !important;
        height: 100vh !important;
        max-width: 100vw !important;
        min-height: 100vh !important;
        border: 0 !important;
        display: block !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)
 
# Load the game HTML
html_path = Path(__file__).parent / "toy_dash_to_grace_vs_tala.html"
html = html_path.read_text(encoding="utf-8")
 
# Render with a generous height — the CSS above forces it to 100vh anyway.
components.html(html, height=2000, scrolling=False)
 

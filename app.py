import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from agents.simulation_agent import SimulationAgent
from agents.scenarios import *

st.set_page_config(
    page_title="TerraTwin",
    page_icon="🛰️",
    layout="wide",
)

# Remove Streamlit's default chrome (toolbar/header/menu/footer) so the
# dashboard fills the page edge-to-edge with nothing overlapping it.
st.markdown(
    """
    <style>
        .block-container { padding-top: 0rem; padding-bottom: 0rem; max-width: 100% !important; }
        header[data-testid="stHeader"] { display: none; }
        #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] { display: none; }
        body { background: #050911; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "terratwin.html"
html_code = html_path.read_text(encoding="utf-8")

components.html(html_code, height=1850, scrolling=True)
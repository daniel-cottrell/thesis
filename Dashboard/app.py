# -----------------------------------------------------------------------------
# app.py
# -----------------------------------------------------------------------------
# Streamlit dashboard entry point for exploring Farey-based fractals.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

import streamlit as st
from src import fractal, plotting

st.set_page_config(page_title="Farey Fractals", layout="wide")
st.markdown(
    """
    <div style='
        background: linear-gradient(90deg, #3f51b5, #00acc1, #43cea2, #00acc1, #3f51b5);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        width: 100%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    '>
        <h1 style='color: #000000;'> Farey Fractals </h1>
    </div>
    """,
    unsafe_allow_html=True
)

left_col, middle_col, right_col = st.columns([2, 0.2, 2])

with left_col:
    # Create tabs
    tabs = st.tabs(["Fractal Parameter Inputs"])

    with tabs[0]:
        col1, col2 = st.columns(2)

        with col1:
            N = st.slider("Order (N)", min_value=50, max_value=500,
                          value=257, step=1)
            K = st.slider("Katz criterion (K)", min_value=float(0), max_value=float(1),
                          value=0.1, step=0.01)
            
            points = fractal.generate_fractal_points(N, K)

with right_col:
    fig = plotting.plot_fractal(points, N, K)
    st.pyplot(fig)



# Add more interactive controls (colormap, point size, zoom)
# Save plots as images/PDFs directly from streamlit
# Create a summary of the mathematical properties
# Let users compare multiple fractals side by side









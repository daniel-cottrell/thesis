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

st.write("")
st.write("")

left_col, middle_col, right_col = st.columns([2, 0.2, 2])

with left_col:
    N = st.slider("Order (N)", min_value=50, max_value=1000,
                  value=257, step=1)
    K = st.slider("Katz criterion (K)", min_value=float(0), max_value=float(5),
                  value=0.1, step=0.01)
    
    point_size = st.slider("Point Size", min_value=0.1, max_value=5.0,
                           value=0.5, step=0.1)

    points = fractal.generate_fractal_points(N, K)

with right_col:
    fig = plotting.plot_fractal(points, N, K, point_size)#, colormap)
    st.pyplot(fig)



# Add more interactive controls (colormap, point size, zoom)
# Come up with metric for colormap based on the thesis
#
# Create a summary of the mathematical properties, displayed underneath fractal
# Let users compare two fractals side by side (single and dual mode)
# For selecting order, add option for only prime number selection vs any number









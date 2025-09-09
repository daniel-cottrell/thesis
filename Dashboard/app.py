# -----------------------------------------------------------------------------
# app.py
# -----------------------------------------------------------------------------
# Streamlit dashboard entry point for exploring Farey-based fractals.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

import streamlit as st 
from src import fractal_corner, fractal_centre, plotting

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

# Mode selection
mode = st.radio(
    "Mode",
    ["Single Fractal", "Dual Fractals"],
    index=0,
    horizontal=True
)

if mode == "Single Fractal":
    left_col, _, right_col = st.columns([2, 0.2, 2])

    with left_col:
        N = st.slider("Order (N)", 50, 1000, 257, 1)
        K = st.slider("Katz criterion (K)", 0.0, 5.0, 0.1, 0.01)
        
        point_size = st.slider("Point Size", 0.1, 5.0, 0.5, 0.1)

        origin_choice = st.radio(
            "Fractal Origin",
            ["Corner", "Centre"],
            index=1,
            horizontal=True
        )

        if origin_choice == "Corner":
            points = fractal_corner.generate_fractal_points(N, K)
        else:
            points = fractal_centre.generate_fractal_points(N, K)

    with right_col:
        fig = plotting.plot_fractal(points, N, K, point_size)
        st.pyplot(fig)

else:  # Dual Fractals
    st.subheader("Synchronisation Options")
    sync_N = st.checkbox("Synchronise N (Order)")
    sync_K = st.checkbox("Synchronise K (Katz criterion)")
    sync_ps = st.checkbox("Synchronise Point Size")
    sync_origin = st.checkbox("Synchronise Origin")

    col1, col2 = st.columns(2)

    # ---- FRACTAL A ----
    with col1:
        st.subheader("Fractal A")
        N1 = st.slider("Order (N1)", 50, 1000, 257, 1, key="N1")
        K1 = st.slider("Katz criterion (K1)", 0.0, 5.0, 0.1, 0.01, key="K1")
        point_size1 = st.slider("Point Size (A)", 0.1, 5.0, 0.5, 0.1, key="ps1")
        origin_choice1 = st.radio("Fractal Origin (A)", ["Corner", "Centre"], index=1, horizontal=True, key="o1")

        if origin_choice1 == "Corner":
            points1 = fractal_corner.generate_fractal_points(N1, K1)
        else:
            points1 = fractal_centre.generate_fractal_points(N1, K1)

        fig1 = plotting.plot_fractal(points1, N1, K1, point_size1)
        st.pyplot(fig1)

    # ---- FRACTAL B ----
    with col2:
        st.subheader("Fractal B")

        # Order (N)
        if sync_N:
            N2 = st.slider("Order (N2)", 50, 1000, N1, 1, key="N2", disabled=True)
        else:
            N2 = st.slider("Order (N2)", 50, 1000, 500, 1, key="N2")

        # Katz criterion (K)
        if sync_K:
            K2 = st.slider("Katz criterion (K2)", 0.0, 5.0, K1, 0.01, key="K2", disabled=True)
        else:
            K2 = st.slider("Katz criterion (K2)", 0.0, 5.0, 0.2, 0.01, key="K2")

        # Point size
        if sync_ps:
            point_size2 = st.slider("Point Size (B)", 0.1, 5.0, point_size1, 0.1, key="ps2", disabled=True)
        else:
            point_size2 = st.slider("Point Size (B)", 0.1, 5.0, 0.5, 0.1, key="ps2")

        # Origin
        if sync_origin:
            origin_choice2 = st.radio("Fractal Origin (B)", ["Corner", "Centre"], index=(0 if origin_choice1 == "Corner" else 1), horizontal=True, key="o2", disabled=True)
        else:
            origin_choice2 = st.radio("Fractal Origin (B)", ["Corner", "Centre"], index=1, horizontal=True, key="o2")

        if origin_choice2 == "Corner":
            points2 = fractal_corner.generate_fractal_points(N2, K2)
        else:
            points2 = fractal_centre.generate_fractal_points(N2, K2)

        fig2 = plotting.plot_fractal(points2, N2, K2, point_size2)
        st.pyplot(fig2)



# Add more interactive controls (colormap, point size, zoom)
# Come up with metric for colormap based on the thesis
#
# Create a summary of the mathematical properties, displayed underneath fractal
# Let users compare two fractals side by side (single and dual mode)
# For selecting order, add option for only prime number selection vs any number









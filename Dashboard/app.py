# -----------------------------------------------------------------------------
# app.py
# -----------------------------------------------------------------------------
# Streamlit dashboard entry point for exploring Farey-based fractals.
# 
# Author: Daniel Cottrell
# Part of the Farey-based fractal project.
# -----------------------------------------------------------------------------

import streamlit as st 
from src import fractal_corner, fractal_centre, intersect, plotting, metrics

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

        inverse = st.checkbox("Inverse Mapping (Swap Black and White)", value=False)

        if origin_choice == "Corner":
            points = fractal_corner.generate_fractal_points(N, K)
        else:
            points = fractal_centre.generate_fractal_points(N, K)

    with right_col:
        fig = plotting.plot_fractal(points, N, K, point_size, origin_choice.lower(), inverse=inverse)
        st.pyplot(fig)

        if points:
            st.write("**Metrics**")
            dim = metrics.fractal_dimension(points)
            st.text(f"Dimension = {dim:.3f}")

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

        st.write("")
        st.write("")

        fig1 = plotting.plot_fractal(points1, N1, K1, point_size1, origin_choice1.lower())
        st.pyplot(fig1)

        if points1:
            st.write("**Metrics (A):**")
            st.text(f"Dimension = {metrics.fractal_dimension(points1):.3f}")
            #st.text(f"Entropy = {metrics.fractal_entropy(points1):.3f}")

    # ---- FRACTAL B ----
    with col2:
        st.subheader("Fractal B")

        if sync_N:
            N2 = st.slider("Order (N2)", 50, 1000, N1, 1, key="N2", disabled=True)
        else:
            N2 = st.slider("Order (N2)", 50, 1000, 500, 1, key="N2")

        if sync_K:
            K2 = st.slider("Katz criterion (K2)", 0.0, 5.0, K1, 0.01, key="K2", disabled=True)
        else:
            K2 = st.slider("Katz criterion (K2)", 0.0, 5.0, 0.2, 0.01, key="K2")

        if sync_ps:
            point_size2 = st.slider("Point Size (B)", 0.1, 5.0, point_size1, 0.1, key="ps2", disabled=True)
        else:
            point_size2 = st.slider("Point Size (B)", 0.1, 5.0, 0.5, 0.1, key="ps2")

        if sync_origin:
            origin_choice2 = st.radio("Fractal Origin (B)", ["Corner", "Centre"],
                                      index=(0 if origin_choice1 == "Corner" else 1),
                                      horizontal=True, key="o2", disabled=True)
        else:
            origin_choice2 = st.radio("Fractal Origin (B)", ["Corner", "Centre"], index=1, horizontal=True, key="o2")

        if origin_choice2 == "Corner":
            points2 = fractal_corner.generate_fractal_points(N2, K2)
        else:
            points2 = fractal_centre.generate_fractal_points(N2, K2)

        st.write("")
        st.write("")

        fig2 = plotting.plot_fractal(points2, N2, K2, point_size2, origin_choice2.lower())
        st.pyplot(fig2)

        if points2:
            st.write("**Metrics (B):**")
            st.text(f"Dimension = {metrics.fractal_dimension(points2):.3f}")
            #st.text(f"Entropy = {metrics.fractal_entropy(points2):.3f}")

    st.write("")
    if N1 != N2:
        st.write("Hausdorff Distance is only calculated when N are the same size.")
    else:
        st.text(f"Hausdorff Distance (A and B) = {metrics.fractal_distance(points1, points2):.3f}")
    
    st.write("")
    st.write("")
    st.write("")

    # ---- COMBINED OVERLAY ----
    st.subheader("Overlay of Fractal A and B")
    import matplotlib.pyplot as plt
    fig_overlay, ax = plt.subplots(figsize=(8, 8))

    if points1:
        x1, y1 = zip(*points1)
        ax.scatter(x1, y1, s=point_size1, c="red", label="Fractal A", alpha=0.6)
    if points2:
        x2, y2 = zip(*points2)
        ax.scatter(x2, y2, s=point_size2, c="blue", label="Fractal B", alpha=0.6)

    ax.set_title(f"N1={N1}, K1={K1}, origin={origin_choice1.lower()}  |  """
                 f"N2={N2}, K2={K2}, origin={origin_choice2.lower()}")
    ax.set_aspect("equal")
    ax.legend()

    st.pyplot(fig_overlay)

    st.write("")
    st.write("")

    # ---- FRACTAL INTERSECTION ----
    st.subheader("Intersection of Fractal A and B")

    intersection_pts = intersect.intersect_points(points1, points2, tol=1)

    fig_inter, ax = plt.subplots(figsize=(8, 8))
    if intersection_pts:
        x_int, y_int = zip(*intersection_pts)
        ax.scatter(x_int, y_int, s=min(point_size1, point_size2),
                   c="purple", label="Intersection", alpha=0.7)
    ax.set_title(
        f"N1={N1}, K1={K1}, origin={origin_choice1.lower()}  ∩  "
        f"N2={N2}, K2={K2}, origin={origin_choice2.lower()}"
    )
    ax.set_aspect("equal")

    st.pyplot(fig_inter)

    st.write("")
    st.write("")

    # ---- FRACTAL DIFFERENCE (A - B) ----
    st.subheader("Difference: Fractal A − Fractal B")

    difference_pts = intersect.difference_points(points1, points2, tol=1)

    fig_diff, ax = plt.subplots(figsize=(8, 8))
    if difference_pts:
        x_diff, y_diff = zip(*difference_pts)
        ax.scatter(x_diff, y_diff, s=point_size1,
                   c="green", label="A − B", alpha=0.7)
    ax.set_title(
        f"N1={N1}, K1={K1}, origin={origin_choice1.lower()}  −  "
        f"N2={N2}, K2={K2}, origin={origin_choice2.lower()}"
    )
    ax.set_aspect("equal")
    ax.legend()
    st.pyplot(fig_diff)





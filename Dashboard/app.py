# -----------------------------------------------------------------------------
# app.py
# -----------------------------------------------------------------------------
# Streamlit dashboard entry point for exploring Farey-based fractals.
# 
# Author: Daniel Cottrell
# Part of the Farey fractal project.
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
    horizontal=True,
    help="Choose whether to explore a single Farey fractal or compare two fractals side-by-side."
)

# K Range selection
K_range_choice = st.radio(
    "Select K Range",
    ["Small-scale (0-1)", "Large-scale (0-5)"],
    index=0,
    horizontal=True,
    help="Select the range of the Katz criterion (K). Small-scale highlights subtle variations, while large-scale explores broader structural changes."
)

K_min, K_max = (0.0, 1.0) if "Small-scale" in K_range_choice else (0.0, 5.0)

if mode == "Single Fractal":
    left_col, _, right_col = st.columns([2, 0.2, 2])

    with left_col:
        N = st.slider("Order (N)",
                       50, 1000, 257, 1,
                       help="Sets the Farey sequence order. Higher values increase detail and complexity of the fractal."
                       )
        
        K = st.slider("Katz criterion (K)",
                      K_min, K_max, 0.1, 0.01,
                      help="Controls how many points satisfy the selection threshold."
                      )
        
        point_size = st.slider("Point Size",
                               0.1, 5.0, 0.5, 0.1,
                               help="Adjusts the rendered point size in the fractal plots."
                               )

        origin_choice = st.radio(
            "Fractal Origin",
            ["Corner", "Centre"],
            index=0,
            horizontal=True,
            help="Choose the coordinate origin used when constructing the fractal geometry."
        )

        inverse = st.checkbox("Invert Mapping",
                              value=False,
                              help="Swaps black and white to highlight complementary patterns.")

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
    sync_N = st.checkbox("Synchronise N (Order)", help="Lock both fractals to use the same Farey order.")
    sync_K = st.checkbox("Synchronise K (Katz criterion)", help="Lock both fractals to use the same K value.")
    sync_ps = st.checkbox("Synchronise Point Size", help="Ensure both fractals use the same point size.")
    sync_origin = st.checkbox("Synchronise Origin", help="Use the same origin for both fractals.")

    col1, col2 = st.columns(2)

    # ---- FRACTAL A ----
    with col1:
        st.subheader("Fractal A")
        N1 = st.slider("Order (N1)", 50, 1000, 257, 1, key="N1",
                       help="Farey sequence order for Fractal A.")
        K1 = st.slider("Katz criterion (K1)", K_min, K_max, 0.1, 0.01, key="K1",
                       help="Transformation parameter controlling comlexity of Fractal A.")
        point_size1 = st.slider("Point Size (A)", 0.1, 5.0, 0.5, 0.1, key="ps1",
                                help="Display size of each plotted point for Fractal A.")
        origin_choice1 = st.radio("Fractal Origin (A)", ["Corner", "Centre"], index=0,
                                  horizontal=True, key="o1",
                                  help="Choose the construction origin for Fractal A.")
        inverse = st.checkbox("Invert Mapping", value=False, key="i1",
                              help="Swaps black and white to highlight complementary patterns.")

        if origin_choice1 == "Corner":
            points1 = fractal_corner.generate_fractal_points(N1, K1)
        else:
            points1 = fractal_centre.generate_fractal_points(N1, K1)

        st.write("")
        st.write("")

        fig1 = plotting.plot_fractal(points1, N1, K1, point_size1, origin_choice1.lower(), inverse=inverse)
        st.pyplot(fig1)

        if points1:
            st.write("**Metrics (A):**")
            st.text(f"Dimension = {metrics.fractal_dimension(points1):.3f}")

    # ---- FRACTAL B ----
    with col2:
        st.subheader("Fractal B")

        if sync_N:
            N2 = N1
            st.slider("Order (N2)", 50, 1000, N2, 1, key="N2", disabled=True,
                           help="Farey sequence order for Fractal B (synchronised with A).")
        else:
            N2 = st.slider("Order (N2)", 50, 1000, 500, 1, key="N2",
                           help="Farey sequence order for Fractal B.")

        if sync_K:
            K2 = K1
            st.slider("Katz criterion (K2)", K_min, K_max, K2, 0.01, key="K2", disabled=True,
                           help="Transformation parameter for Fractal B (synchronised with A).")
        else:
            K2 = st.slider("Katz criterion (K2)", K_min, K_max, 0.2, 0.01, key="K2",
                           help="Transformation parameter controlling complexity of Fractal B.")

        if sync_ps:
            point_size2 = point_size1
            st.slider("Point Size (B)", 0.1, 5.0, point_size2, 0.1, key="ps2", disabled=True,
                                    help="Point size for Fractal B (synchronised with A).")
        else:
            point_size2 = st.slider("Point Size (B)", 0.1, 5.0, 0.5, 0.1, key="ps2",
                                    help="Display size of each plotted point for Fractal B.")

        if sync_origin:
            index2 = 0 if origin_choice1 == "Corner" else 1
            origin_choice2 = origin_choice1
            st.radio("Fractal Origin (B)", ["Corner", "Centre"],
                                      index=index2, horizontal=True, key="o2", disabled=True,
                                      help="Construction origin for Fractal B (synchronised with A).")
        else:
            origin_choice2 = st.radio("Fractal Origin (B)", ["Corner", "Centre"], index=0,
                                      horizontal=True, key="o2",
                                      help="Choose the construction origin for Fractal B.")

        inverse = st.checkbox("Invert Mapping", value=False,
                              help="Swaps black and white to highlight complementary patterns.")


        if origin_choice2 == "Corner":
            points2 = fractal_corner.generate_fractal_points(N2, K2)
        else:
            points2 = fractal_centre.generate_fractal_points(N2, K2)

        st.write("")
        st.write("")

        fig2 = plotting.plot_fractal(points2, N2, K2, point_size2, origin_choice2.lower(), inverse=inverse)
        st.pyplot(fig2)

        if points2:
            st.write("**Metrics (B):**")
            st.text(f"Dimension = {metrics.fractal_dimension(points2):.3f}")

    st.write("")
    if N1 != N2:
        st.write("Hausdorff Distance is only calculated when N are the same size.")
    else:
        st.text(f"Hausdorff Distance (A and B) = {metrics.fractal_distance(points1, points2):.3f}")
    
    st.write("")
    st.write("")
    st.write("")

    # ---- COMBINED OVERLAY ----
    st.subheader("Overlay of Fractal A and B", help="Visual comparison of both fractals plotted together.")
    import matplotlib.pyplot as plt
    fig_overlay, ax = plt.subplots(figsize=(8, 8))

    if points1:
        x1, y1 = zip(*points1)
        ax.scatter(x1, y1, s=point_size1, c="red", label="Fractal A", alpha=0.6)
    if points2:
        x2, y2 = zip(*points2)
        ax.scatter(x2, y2, s=point_size2, c="blue", label="Fractal B", alpha=0.6)

    ax.set_aspect("equal")
    ax.legend()

    st.pyplot(fig_overlay)

    st.write("")
    st.write("")

    # ---- FRACTAL INTERSECTION ----
    st.subheader("Intersection of Fractal A and B", help="Shows overlapping points shared by both fractals.")

    intersection_pts = intersect.intersect_points(points1, points2, tol=1)

    fig_inter, ax = plt.subplots(figsize=(8, 8))
    if intersection_pts:
        x_int, y_int = zip(*intersection_pts)
        ax.scatter(x_int, y_int, s=min(point_size1, point_size2),
                   c="purple")
    ax.set_aspect("equal")

    st.pyplot(fig_inter)

    st.write("")
    st.write("")

    # ---- FRACTAL DIFFERENCE (A - B) ----
    st.subheader("Difference: Fractal A − Fractal B", help="Displays points unique to Fractal A. If Fractal A has no unique points relative to Fractal B, this appears empty.")

    difference_pts = intersect.difference_points(points1, points2, tol=1)

    fig_diff, ax = plt.subplots(figsize=(8, 8))
    if difference_pts:
        x_diff, y_diff = zip(*difference_pts)
        ax.scatter(x_diff, y_diff, s=point_size1,
                   c="green")
    
    ax.set_aspect("equal")
    st.pyplot(fig_diff)





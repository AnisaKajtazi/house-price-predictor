import streamlit as st
from streamlit_folium import st_folium
import folium

def render_map():

    st.subheader("🗺️ Click on map")

    m = folium.Map(
        location=[42.6629, 21.1655],
        zoom_start=13
    )

    map_data = st_folium(
        m,
        height=650,
        use_container_width=True
    )

    if map_data and map_data.get("last_clicked"):
        lat = map_data["last_clicked"]["lat"]
        lon = map_data["last_clicked"]["lng"]

        st.success(f"Selected: {lat:.4f}, {lon:.4f}")

        return lat, lon

    return None, None
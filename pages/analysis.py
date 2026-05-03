from components.map_ui import render_map
from utils.location_engine import adjust_price_by_location

import streamlit as st
st.set_page_config(layout="wide")

import pandas as pd
import joblib
from utils.style import load_style

load_style()

st.markdown("""
<style>
.block-container {
    max-width: 95% !important;
    padding-top: 20px;
}
</style>
""", unsafe_allow_html=True)

model = joblib.load("models/model_v1.joblib")

if st.button("Back"):
    st.switch_page("app.py")

st.title("AI Analysis Dashboard")

if "features" not in st.session_state or "prediction" not in st.session_state:
    st.warning("⚠️ Please go back and enter house data first.")
    
    if st.button("Go to Prediction Page"):
        st.switch_page("app.py")
    
    st.stop()

features = st.session_state.features
prediction = st.session_state.prediction




st.subheader("What impacts price the most")

try:
    importance = model.coef_
except:
    importance = model.feature_importances_

feature_names = [
    'area','bedrooms','bathrooms','stories',
    'mainroad','guestroom','basement',
    'hotwaterheating','airconditioning',
    'parking','prefarea','furnishingstatus'
]

df_imp = pd.DataFrame({
    "Feature": feature_names,
    "Impact": importance
}).sort_values(by="Impact", ascending=False)

col1, col2, col3 = st.columns(3)
col1.bar_chart(df_imp.set_index("Feature"))
col2.bar_chart(features.T)
col3.metric("Price", f"${prediction:,.0f}")




st.subheader("Relationships (Market Behavior)")

df = None

try:
    df = pd.read_csv("data/processed/processed.csv")

    col4, col5, col6 = st.columns(3)

    col4.line_chart(df.sort_values("area")[["area", "price"]].set_index("area"))
    col5.bar_chart(df.groupby("bedrooms")["price"].mean())
    col6.bar_chart(df.groupby("parking")["price"].mean())

except:
    st.warning("Dataset not found")




st.subheader("What happens if you change features?")

col7, col8, col9 = st.columns(3)

with col7:
    new_area = st.slider("Area", 1000, 10000, int(features['area'][0]))

with col8:
    new_bedrooms = st.slider("Bedrooms", 1, 6, int(features['bedrooms'][0]))

with col9:
    new_parking = st.slider("Parking", 0, 3, int(features['parking'][0]))

new_features = features.copy()
new_features['area'] = new_area
new_features['bedrooms'] = new_bedrooms
new_features['parking'] = new_parking

new_price = model.predict(new_features)[0]
diff = new_price - prediction

col10, col11, col12 = st.columns(3)

col10.metric("New Price", f"${new_price:,.0f}", f"{diff:,.0f}")

if diff > 0:
    col11.success("Price is increasing 📈")
else:
    col11.error("Price is decreasing 📉 ")




st.subheader("AI Insights")

col13, col14, col15 = st.columns(3)

if features['area'][0] < 4000:
    col13.warning("Small area → price limited")

if features['bedrooms'][0] < 3:
    col14.info("More bedrooms = higher value")

if features['parking'][0] == 0:
    col15.error("No parking ↓ value")




st.subheader("Market Position")

try:
    avg_price = df["price"].mean()

    if prediction > avg_price:
        st.success("Above market average")
    else:
        st.info("Below market average")

except:
    pass




st.subheader("Location Impact on Price")

lat, lon = render_map()

if lat is not None and lon is not None:

    new_price_loc, diff_loc, zone, multiplier = adjust_price_by_location(
        prediction, lat, lon
    )

    colA, colB, colC = st.columns(3)

    colA.metric("Original Price", f"${prediction:,.0f}")
    colB.metric("Location Price", f"${new_price_loc:,.0f}", f"{diff_loc:,.0f}")

    if zone == "A":
        colC.success("📍 Premium Area (Center)")
    elif zone == "B":
        colC.info("📍 Normal Area")
    else:
        colC.error("📍 Cheap Area")

else:
    st.info("Click somewhere on the map")

st.markdown('</div>', unsafe_allow_html=True)
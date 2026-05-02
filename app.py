import streamlit as st
import pandas as pd
import joblib

# 🎨 STYLE (background + blur glass effect)
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1494526585095-c41746248156");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .block-container {
        backdrop-filter: blur(15px);
        background: rgba(255, 255, 255, 0.2);
        padding: 2rem;
        border-radius: 15px;
        color: black;
    }

    input, select {
        background-color: rgba(255,255,255,0.7) !important;
        border-radius: 8px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load model
model = joblib.load("models/model_v1.joblib")

# ✨ TITLE
st.title("🏠 AI House Price Predictor")
st.markdown("### Get instant predictions powered by Machine Learning 💡")

# Inputs
area = st.number_input("Area", value=3000)
bedrooms = st.number_input("Bedrooms", value=2)
bathrooms = st.number_input("Bathrooms", value=2)
stories = st.number_input("Stories", value=2)

# 🔥 YES / NO (user-friendly)
mainroad = 1 if st.selectbox("Main Road", ["Yes", "No"]) == "Yes" else 0
guestroom = 1 if st.selectbox("Guest Room", ["Yes", "No"]) == "Yes" else 0
basement = 1 if st.selectbox("Basement", ["Yes", "No"]) == "Yes" else 0
hotwaterheating = 1 if st.selectbox("Hot Water Heating", ["Yes", "No"]) == "Yes" else 0
airconditioning = 1 if st.selectbox("Air Conditioning", ["Yes", "No"]) == "Yes" else 0

parking = st.number_input("Parking", value=1)

prefarea = 1 if st.selectbox("Preferred Area", ["Yes", "No"]) == "Yes" else 0

# 🛋️ Furnishing clean
furnishing = st.selectbox(
    "Furnishing",
    ["Furnished", "Semi-Furnished", "Unfurnished"]
)

if furnishing == "Furnished":
    furnishingstatus = 2
elif furnishing == "Semi-Furnished":
    furnishingstatus = 1
else:
    furnishingstatus = 0

# Predict button
if st.button("Predict Price"):
    features = pd.DataFrame([[
        area, bedrooms, bathrooms, stories,
        mainroad, guestroom, basement,
        hotwaterheating, airconditioning,
        parking, prefarea, furnishingstatus
    ]], columns=[
        'area', 'bedrooms', 'bathrooms', 'stories',
        'mainroad', 'guestroom', 'basement',
        'hotwaterheating', 'airconditioning',
        'parking', 'prefarea', 'furnishingstatus'
    ])

    prediction = model.predict(features)

    st.success(f"💰 Predicted Price: ${prediction[0]:,.2f}")
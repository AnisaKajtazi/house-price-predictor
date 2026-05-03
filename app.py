import streamlit as st
import pandas as pd
import joblib
from utils.style import load_style

load_style()

if "predicted" not in st.session_state:
    st.session_state.predicted = False

if "step1_done" not in st.session_state:
    st.session_state.step1_done = False

model = joblib.load("models/model_v1.joblib")

st.title("AI House Price Predictor")



st.subheader("Step 1: Basic Info")
purpose = st.selectbox("Purpose", ["Buy", "Rent"])
members = st.slider("Family Members", 1, 10)

if st.button("Continue"):
    st.session_state.step1_done = True

st.markdown('</div>', unsafe_allow_html=True)



if st.session_state.step1_done:

    st.markdown('<div class="card-big">', unsafe_allow_html=True)

    st.subheader("Step 2: House Details")

    area = st.number_input("Area", value=3000)
    bedrooms = st.number_input("Bedrooms", value=2)
    bathrooms = st.number_input("Bathrooms", value=2)
    stories = st.number_input("Stories", value=2)

    mainroad = 1 if st.selectbox("Main Road", ["Yes", "No"]) == "Yes" else 0
    guestroom = 1 if st.selectbox("Guest Room", ["Yes", "No"]) == "Yes" else 0
    basement = 1 if st.selectbox("Basement", ["Yes", "No"]) == "Yes" else 0
    hotwaterheating = 1 if st.selectbox("Hot Water Heating", ["Yes", "No"]) == "Yes" else 0
    airconditioning = 1 if st.selectbox("Air Conditioning", ["Yes", "No"]) == "Yes" else 0

    parking = st.number_input("Parking", value=1)
    prefarea = 1 if st.selectbox("Preferred Area", ["Yes", "No"]) == "Yes" else 0

    furnishing = st.selectbox(
        "Furnishing",
        ["Furnished", "Semi-Furnished", "Unfurnished"]
    )

    furnishingstatus = 2 if furnishing == "Furnished" else 1 if furnishing == "Semi-Furnished" else 0

    if st.button("Predict Price 💡"):

        features = pd.DataFrame([[area, bedrooms, bathrooms, stories,
                                  mainroad, guestroom, basement,
                                  hotwaterheating, airconditioning,
                                  parking, prefarea, furnishingstatus]],
                                columns=[
                                    'area','bedrooms','bathrooms','stories',
                                    'mainroad','guestroom','basement',
                                    'hotwaterheating','airconditioning',
                                    'parking','prefarea','furnishingstatus'
                                ])

        prediction = model.predict(features)[0]

        st.session_state.features = features
        st.session_state.prediction = prediction
        st.session_state.predicted = True

        st.success(f" ${prediction:,.2f}")

    if st.session_state.predicted:
        if st.button("Open AI Analysis 📊"):
            st.switch_page("pages/analysis.py")


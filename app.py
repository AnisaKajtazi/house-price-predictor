import streamlit as st
import pandas as pd
import joblib
from utils.style import load_style

load_style()



defaults = {
    "predicted": False,
    "step1_done": False,
    "area": None,
    "bedrooms": None,
    "bathrooms": None,
    "stories": None,
    "parking": None,
    "mainroad": None,
    "guestroom": None,
    "basement": None,
    "hotwaterheating": None,
    "airconditioning": None,
    "prefarea": None,
    "furnishing": None
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

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


    area = st.number_input(
        "Area (sqft)",
        min_value=1650,
        max_value=16200,
        value=st.session_state.area,
        placeholder="1650 - 16200"
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=6,
        value=st.session_state.bedrooms,
        placeholder="1 - 6"
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=4,
        value=st.session_state.bathrooms,
        placeholder="1 - 4"
    )

    stories = st.number_input(
        "Stories",
        min_value=1,
        max_value=4,
        value=st.session_state.stories,
        placeholder="1 - 4"
    )

    parking = st.number_input(
        "Parking",
        min_value=0,
        max_value=3,
        value=st.session_state.parking,
        placeholder="0 - 3"
    )





    def select_with_placeholder(label, key):
        options = ["-- Select --", "Yes", "No"]
        value = st.selectbox(label, options, index=0 if st.session_state[key] is None else options.index(st.session_state[key]))

        if value == "Yes":
            st.session_state[key] = "Yes"
            return 1
        elif value == "No":
            st.session_state[key] = "No"
            return 0
        else:
            st.session_state[key] = None
            return None

    mainroad = select_with_placeholder("Main Road", "mainroad")
    guestroom = select_with_placeholder("Guest Room", "guestroom")
    basement = select_with_placeholder("Basement", "basement")
    hotwaterheating = select_with_placeholder("Hot Water Heating", "hotwaterheating")
    airconditioning = select_with_placeholder("Air Conditioning", "airconditioning")
    prefarea = select_with_placeholder("Preferred Area", "prefarea")




    furnishing_options = ["-- Select --", "Furnished", "Semi-Furnished", "Unfurnished"]
    furnishing = st.selectbox(
        "Furnishing",
        furnishing_options,
        index=0 if st.session_state.furnishing is None else furnishing_options.index(st.session_state.furnishing)
    )

    if furnishing != "-- Select --":
        st.session_state.furnishing = furnishing

    if furnishing == "Furnished":
        furnishingstatus = 2
    elif furnishing == "Semi-Furnished":
        furnishingstatus = 1
    elif furnishing == "Unfurnished":
        furnishingstatus = 0
    else:
        furnishingstatus = None



    st.session_state.area = area
    st.session_state.bedrooms = bedrooms
    st.session_state.bathrooms = bathrooms
    st.session_state.stories = stories
    st.session_state.parking = parking



    if st.button("Predict Price 💡"):

        if None in [
            area, bedrooms, bathrooms, stories, parking,
            mainroad, guestroom, basement,
            hotwaterheating, airconditioning,
            prefarea, furnishingstatus
        ]:
            st.error("⚠️ Please fill all fields correctly")
        else:

            features = pd.DataFrame([[
                area, bedrooms, bathrooms, stories,
                mainroad, guestroom, basement,
                hotwaterheating, airconditioning,
                parking, prefarea, furnishingstatus
            ]],
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

            st.success(f"${prediction:,.2f}")


    if st.session_state.predicted:
        if st.button("Open AI Analysis 📊"):
            st.switch_page("pages/analysis.py")
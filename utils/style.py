import streamlit as st

def load_style():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1494526585095-c41746248156");
        background-size: cover;
        background-position: center;
    }


    .block-container {
        max-width: 900px;
        margin: auto;
        margin-top: 60px;
        padding: 40px;

        backdrop-filter: blur(20px);
        background: rgba(255,255,255,0.25);
        border-radius: 20px;
    }

    input, select {
    background-color: rgba(255,255,255,0.9) !important;
    border-radius: 10px !important;
    color: black !important;
}
div[data-baseweb="input"] input {
    color: black !important;
    -webkit-text-fill-color: black !important;
}
    button {
        border-radius: 10px !important;
        height: 45px;
    }

    .analysis-wide .block-container {
        max-width: 1200px;
    }


.analysis-page .block-container {
    max-width: 95% !important;
    width: 95% !important;
    padding: 30px !important;
    margin-top: 20px !important;
}

    </style>
    """, unsafe_allow_html=True)
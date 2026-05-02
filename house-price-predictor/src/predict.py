import joblib
import numpy as np
import pandas as pd  # 👉 KJO MUNGONTE

def load_model(path):
    return joblib.load(path)

def predict_price(model, features):
    prediction = model.predict(features)
    return prediction[0]

if __name__ == "__main__":
    model = load_model("models/model_v1.joblib")

    print("Enter house details:")

    area = int(input("Area: "))
    bedrooms = int(input("Bedrooms: "))
    bathrooms = int(input("Bathrooms: "))
    stories = int(input("Stories: "))
    mainroad = int(input("Main road (1=yes, 0=no): "))
    guestroom = int(input("Guest room (1=yes, 0=no): "))
    basement = int(input("Basement (1=yes, 0=no): "))
    hotwaterheating = int(input("Hot water heating (1=yes, 0=no): "))
    airconditioning = int(input("Air conditioning (1=yes, 0=no): "))
    parking = int(input("Parking: "))
    prefarea = int(input("Preferred area (1=yes, 0=no): "))
    furnishingstatus = int(input("Furnishing (2=furnished, 1=semi, 0=unfurnished): "))

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

    price = predict_price(model, features)

    print(f"\nPredicted House Price: {price:.2f}")
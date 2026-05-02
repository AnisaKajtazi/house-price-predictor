import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


def load_data(path):
    df = pd.read_csv(path)
    return df


def train_model(df):
    X = df.drop('price', axis=1)
    y = df['price']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model


def save_model(model, path):
    joblib.dump(model, path)


if __name__ == "__main__":
    df = load_data("data/processed/processed.csv")
    model = train_model(df)
    save_model(model, "models/model_v1.joblib")

    print("Model trained and saved!")
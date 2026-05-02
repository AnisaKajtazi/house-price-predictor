import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    # Encoding yes/no columns
    binary_cols = [
        'mainroad', 'guestroom', 'basement',
        'hotwaterheating', 'airconditioning', 'prefarea'
    ]

    for col in binary_cols:
        df[col] = df[col].map({'yes': 1, 'no': 0})

    # Encoding furnishingstatus
    df['furnishingstatus'] = df['furnishingstatus'].map({
        'furnished': 2,
        'semi-furnished': 1,
        'unfurnished': 0
    })

    return df

def save_processed_data(df, path):
    df.to_csv(path, index=False)


if __name__ == "__main__":
    df = load_data("data/raw/Housing.csv")
    df = preprocess_data(df)
    save_processed_data(df, "data/processed/processed.csv")

    print("Preprocessing done!")
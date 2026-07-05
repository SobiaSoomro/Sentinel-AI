import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from extract_features import extract_features


def load_model():

    # Load dataset
    data = pd.read_csv("spam_links_dataset.csv")

    # Extract Features
    feature_list = [
        extract_features(url)
        for url in data["URL"]
    ]

    features_df = pd.DataFrame(feature_list)

    labels = data["Label"]

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        features_df,
        labels,
        test_size=0.2,
        random_state=42
    )

    # Train Model
    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Accuracy
    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print(f"\n✅ Model Accuracy: {accuracy*100:.2f}%")

    return model
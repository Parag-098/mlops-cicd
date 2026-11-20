"""Train and evaluate the assignment's Iris Logistic Regression model."""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def train_model() -> float:
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data,
        iris.target,
        test_size=0.2,
        stratify=iris.target,
        random_state=42,
    )
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return float(accuracy_score(y_test, predictions))


if __name__ == "__main__":
    print(f"Model Accuracy: {train_model():.4f}")

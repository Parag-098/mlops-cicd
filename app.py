"""Small command-line entry point for the Iris CI/CD example."""

from src.model import train_model


def main() -> None:
    accuracy = train_model()
    print("Iris Logistic Regression application completed.")
    print(f"Model Accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    main()

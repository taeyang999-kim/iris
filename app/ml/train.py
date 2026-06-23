from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import os

iris = load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

os.makedirs("models_store", exist_ok=True)

joblib.dump(model, "models_store/iris_model.pkl")

print("Model saved!")
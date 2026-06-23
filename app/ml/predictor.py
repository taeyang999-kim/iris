import joblib
from config import MODEL_PATH

model = joblib.load(MODEL_PATH)

labels = ["setosa", "versicolor", "virginica"]

def predict_iris(data):
    pred = model.predict([data])[0]
    return labels[pred]
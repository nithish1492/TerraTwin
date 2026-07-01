import joblib

model = joblib.load("models/water_model.pkl")

def predict_rainfall(values):
    prediction = model.predict([values])
    return prediction[0]
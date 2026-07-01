import joblib

model = joblib.load("models/healthcare_model.pkl")

def predict_disease(values):
    prediction = model.predict([values])
    return prediction[0]
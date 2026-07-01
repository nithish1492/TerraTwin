import joblib

model = joblib.load("models/agriculture_model.pkl")

def recommend_crop(values):
    prediction = model.predict([values])
    return prediction[0]
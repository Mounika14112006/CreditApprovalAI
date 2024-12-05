from flask import Flask, jsonify, request
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import FunctionTransformer

app = Flask(__name__)
CORS(app)

def label_encode(data):
    label_encoder = LabelEncoder()
    return np.array([label_encoder.fit_transform(col) for col in data.T]).T

model_pipeline = joblib.load('updated_lgbm_model.joblib') 

def convert_numpy_types(obj):
    if isinstance(obj, (np.integer, np.floating)):
        return obj.item() 
    return obj

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        required_fields = [
            "person_age",
            "person_income",
            "person_home_ownership",
            "person_emp_length",
            "loan_intent",
            "loan_amnt",
            "loan_int_rate",
            "loan_percent_income",
            "cb_person_default_on_file",
            "cb_person_cred_length"
        ]
        
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        input_data = pd.DataFrame([{
            "person_age": data["person_age"],
            "person_income": data["person_income"],
            "person_home_ownership": data["person_home_ownership"],
            "person_emp_length": data["person_emp_length"],
            "loan_intent": data["loan_intent"],
            "loan_amnt": data["loan_amnt"],
            "loan_int_rate": data["loan_int_rate"],
            "loan_percent_income": data["loan_percent_income"],
            "cb_person_default_on_file": data["cb_person_default_on_file"],
            "cb_person_cred_length": data["cb_person_cred_length"]
        }])
        if data["loan_amnt"] == 0:
            return jsonify({
                "message": "Prediction successful",
                "prediction": "C"  
            }), 200

        input_data_processed = model_pipeline['preprocessor'].transform(input_data)  
        prediction = model_pipeline['model'].predict(input_data_processed)[0]  

        prediction = convert_numpy_types(prediction)

        return jsonify({
            "message": "Prediction successful",
            "prediction": prediction
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request
import joblib
import numpy as np
import pandas as pd
from flask_cors import CORS
import sqlite3
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
CORS(app)

DATABASE = 'user_data.db'

def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS user_input (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    person_age INTEGER,
                    person_income INTEGER,
                    person_home_ownership TEXT,
                    person_emp_length INTEGER,
                    loan_intent TEXT,
                    loan_amnt INTEGER,
                    loan_int_rate FLOAT,
                    loan_percent_income FLOAT,
                    cb_person_default_on_file TEXT,
                    cb_person_cred_length INTEGER,
                    eligibility TEXT)''')  
    conn.commit()
    conn.close()


create_db()

def label_encode(data):
    label_encoder = LabelEncoder()
    return np.array([label_encoder.fit_transform(col) for col in data.T]).T

model_pipeline = joblib.load('updated_lgbm_model.joblib') 

def convert_numpy_types(obj):
    if isinstance(obj, (np.integer, np.floating)):
        return obj.item() 
    return obj

def save_to_db(data, eligibility):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''INSERT INTO user_input (
                    person_age, person_income, person_home_ownership, 
                    person_emp_length, loan_intent, loan_amnt, loan_int_rate, 
                    loan_percent_income, cb_person_default_on_file, cb_person_cred_length, eligibility) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                    (
                        data['person_age'], data['person_income'], data['person_home_ownership'],
                        data['person_emp_length'], data['loan_intent'], data['loan_amnt'],
                        data['loan_int_rate'], data['loan_percent_income'], 
                        data['cb_person_default_on_file'], data['cb_person_cred_length'],
                        eligibility  
                    ))
    conn.commit()
    conn.close()

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

        input_data_processed = model_pipeline['preprocessor'].transform(input_data)  
        prediction = model_pipeline['model'].predict(input_data_processed)[0]  

        prediction = convert_numpy_types(prediction)
        
        eligibility = "1" if prediction in ['A', 'B'] else "0"

        save_to_db(data, eligibility)

        return jsonify({
            "message": "Prediction successful",
            "eligibility": eligibility
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

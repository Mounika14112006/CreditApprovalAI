
# Credit Approval AI

**Credit Approval AI** is a machine learning application designed to predict loan approval eligibility based on user-provided financial information. The application is built using **Flask** for the backend API and **Streamlit** for the frontend web interface. It uses a pre-trained **LightGBM** model to make predictions and stores the user's input data in an SQLite database.

## Features

- **Loan Prediction**: Predict loan approval based on a variety of features such as age, income, credit history, etc.
- **User Input Form**: A simple, intuitive form for users to input their financial details and check their eligibility for a loan.
- **Database**: Stores the user input along with the prediction result in an SQLite database.
- **Model**: Uses a pre-trained **LightGBM** model to generate predictions based on the user's inputs.

## Requirements

Before running the project, make sure you have the following dependencies installed:

- Python 3.7+
- Flask 2.1.0
- Flask-Cors 3.1.1
- Streamlit 1.18.0
- scikit-learn
- pandas
- joblib
- sqlite3 (comes with Python)
- requests

Install all required dependencies by running:

```bash
pip install -r requirements.txt
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/creditapprovalai.git
Navigate to the project folder:

bash
Copy code
cd creditapprovalai
Set up a virtual environment (optional but recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Running the Application
1. Running the Flask API
The backend API is built using Flask. To start the API server:

bash
Copy code
python api.py
By default, the Flask app will run on http://127.0.0.1:5000. This will expose an endpoint /predict where users can send a POST request to get loan eligibility predictions.

2. Running the Streamlit Web Application
The frontend of the application is built using Streamlit. To launch the web interface:

bash
Copy code
streamlit run loan_app.py
This will start a local Streamlit server and open the app in your browser, where users can input their financial information and check their loan eligibility.

3. Interacting with the API
To interact with the API programmatically (outside of the Streamlit interface), you can send a POST request to the /predict endpoint with the required user data:

Example of JSON input:

json
Copy code
{
    "person_age": 30,
    "person_income": 50000,
    "person_home_ownership": "OWN",
    "person_emp_length": 5,
    "loan_intent": "PERSONAL",
    "loan_amnt": 10000,
    "loan_int_rate": 15.0,
    "loan_percent_income": 0.2,
    "cb_person_default_on_file": "N",
    "cb_person_cred_length": 5
}
Note: You can use the requests library in Python to send the data, as done in the Streamlit app.

4. Checking Database Records
This application stores the user inputs and predictions in an SQLite database (user_data.db). You can inspect the stored records by running the following code:

python
Copy code
import sqlite3

conn = sqlite3.connect('user_data.db') 
cursor = conn.cursor()

cursor.execute("SELECT * FROM user_input")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
This will fetch all records stored in the user_input table and print them to the console.

Data
The model was trained on a historical dataset of loan approval decisions. The application uses this model to predict eligibility for new loan applications based on user input.

user_data.db: SQLite database that stores the user inputs along with the eligibility result.
updated_lgbm_model.joblib: The pre-trained LightGBM model used for predicting loan eligibility.
credit_risk_dataset.csv: Sample dataset used to train the model (can be used for training or testing).
Database Schema
The SQLite database (user_data.db) contains a table called user_input with the following columns:

id: Primary key (autoincrement).
person_age: Age of the user.
person_income: Income of the user.
person_home_ownership: Home ownership status (RENT, OWN, MORTGAGE).
person_emp_length: Years of employment.
loan_intent: Intent for the loan (e.g., PERSONAL, EDUCATION, etc.).
loan_amnt: Loan amount requested.
loan_int_rate: Interest rate for the loan.
loan_percent_income: Percentage of income being requested as a loan.
cb_person_default_on_file: Whether there is a default on file (Y or N).
cb_person_cred_length: Length of the credit history in years.
eligibility: The loan approval status ("1" for eligible, "0" for not eligible).
Example Usage
Streamlit Interface:
Go to the home page and click "Get Started Now" to begin the loan eligibility check process.
Fill out the form with your personal and financial information.
Click "Check Eligibility" to get the prediction.
The eligibility result will be displayed, along with the details of the form you filled out.
API Usage:
To use the API, you can send a POST request to the /predict endpoint with the required data in JSON format. The API will respond with a success message and loan eligibility status (1 for eligible, 0 for not eligible).

Example POST request:

bash
Copy code
POST http://127.0.0.1:5000/predict
Content-Type: application/json

{
    "person_age": 30,
    "person_income": 50000,
    "person_home_ownership": "OWN",
    "person_emp_length": 5,
    "loan_intent": "PERSONAL",
    "loan_amnt": 10000,
    "loan_int_rate": 15.0,
    "loan_percent_income": 0.2,
    "cb_person_default_on_file": "N",
    "cb_person_cred_length": 5
}
Response:

json
Copy code
{
    "message": "Prediction successful",
    "eligibility": "1"
}
Contributing
We welcome contributions! If you'd like to contribute to the project, please fork the repository, create a new branch, and submit a pull request.

Steps for contribution:
Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit them (git commit -m 'Add new feature').
Push to your forked repository (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Thanks to the creators of LightGBM for providing a fast and efficient model for prediction.
Thanks to Streamlit and Flask for providing excellent frameworks for building web applications and APIs.
Contact
For any questions, suggestions, or issues, feel free to open an issue on GitHub or contact the repository owner.

Enjoy using Credit Approval AI!

markdown
Copy code

### Key Sections Explained:
- **Introduction**: A brief description of the project, including key features like loan prediction and database storage.
- **Installation Instructions**: Step-by-step guide on setting up the project.
- **Running the Application**: Instructions on running both the Flask API and the Streamlit frontend.
- **Database Usage**: How the database stores user data and how to inspect it.
- **API and Streamlit Usage**: Detailed examples for both API interaction and Streamlit web interface usage.
- **Contributing**: Instructions on how others can contribute to the project.
- **License**: Information on licensing (MIT license by default).


You said:
🚀 AI Predictive Models for Credit Underwriting
Leverage AI-powered predictive models to revolutionize credit underwriting and streamline decision-making.

📜 Overview
This project enhances the accuracy and efficiency of credit underwriting using AI-based predictive models. By analyzing historical financial data, the system predicts the likelihood of a customer defaulting on a loan, empowering financial institutions with data-driven insights.

📂 Table of Contents
About
Features
Requirements
Setup
How It Works
Usage
Results
Contributing
License
Acknowledgements
🛠️ About
Predictive Modeling: Leverages machine learning algorithms to predict credit risk.
Data Preprocessing: Includes data cleaning, feature selection, and transformation.
Model Evaluation: Implements metrics such as accuracy, precision, recall, F1-score, and ROC-AUC.
Visualizations: Provides clear visual insights into model performance and decision boundaries.
🌟 Features
🌐 Two Apps:
Flask App: Traditional web application.
Streamlit App: Interactive dashboard for predictions.
🔄 Input Preprocessing: Includes log transformations and one-hot encoding.
📊 Pre-trained Model: A machine learning model (model.pkl) ready for predictions.
💻 Requirements
Python 3.x
Required Libraries:
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
flask
⚙️ Setup
Clone the repository:
git clone https://github.com/Aayushipandey54/AI_Predictive_Models_for_Credit_Underwriting.git  
cd AI_Predictive_Models_for_Credit_Underwriting  
⚡ How It Works
1️⃣ Data Preprocessing Clean the dataset (handle missing values and outliers). Encode categorical variables. Split data into training and testing sets. 2️⃣ Model Training Trains the following models:

Logistic Regression Decision Trees Random Forests Neural Networks 3️⃣ Model Evaluation Evaluates models using:

Confusion Matrix Cross-validation Accuracy, Recall, Precision, F1-Score, and ROC-AUC 4️⃣ Predictions Generates predictions on unseen data for credit risk assessment.
🛠️ Usage
1.To train and evaluate the models, run:

python main.py
2.For predictions, use either: Flask App:

flask run
3.Streamlit App:

streamlit run app.py
📈 Results
Model Accuracy: Displays performance metrics for all trained models. Confusion Matrix: Helps analyze errors. ROC-AUC Curve: Provides visualization of model performance.

🤝 Contributing
Fork the repository. 1.Create a new branch for your feature:

git checkout -b feature-name
2.Commit your changes:

git commit -m "Add feature"
3.Push your changes:

git push origin feature-name
Create a pull request.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙌 Acknowledgements
References for credit underwriting methodologies. Resources on machine learning techniques.
⚙️ Final Step: Install Dependencies
Install all required dependencies using the following command:

pip install -r requirements.txt
🚀Leverage AI-powered predictive models to revolutionize credit underwriting and streamline decision-making.
🈁System Architecture
System Architecture
🪢USE CASE DIAGRAM
USE CASE DIAGRAM
Activity Diadram
Activity Diadram
🎥 Demo Video
Watch the Video        like this
ChatGPT said:
ChatGPT
Here’s a detailed and polished README.md for your project, incorporating all the sections you've outlined:

markdown
Copy code
# 🚀 AI Predictive Models for Credit Underwriting

Leverage AI-powered predictive models to revolutionize credit underwriting and streamline decision-making. This project enhances the accuracy and efficiency of credit underwriting using AI-based predictive models. By analyzing historical financial data, the system predicts the likelihood of a customer defaulting on a loan, empowering financial institutions with data-driven insights.

## 📜 Overview

This project implements machine learning models to assess credit risk and predict loan eligibility. It includes data preprocessing, model training, evaluation, and visualizations. The system provides tools for both a traditional Flask app and an interactive Streamlit dashboard to display predictions and insights.

## 📂 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [System Architecture](#system-architecture)
- [Use Case Diagram](#use-case-diagram)
- [Activity Diagram](#activity-diagram)
- [Demo Video](#demo-video)

---

## 🛠️ About

### Predictive Modeling

This system leverages machine learning algorithms to predict the likelihood of a customer defaulting on a loan, streamlining credit underwriting processes.

### Data Preprocessing

The preprocessing pipeline involves data cleaning, feature selection, handling missing values, and encoding categorical variables such as "Home Ownership" and "Loan Intent".

### Model Evaluation

The models are evaluated based on key metrics such as accuracy, precision, recall, F1-score, and ROC-AUC, ensuring that predictions are accurate and reliable.

### Visualizations

Clear visualizations are provided to display model performance, error analysis, and decision boundaries.

---

## 🌟 Features

- **🌐 Two Apps**:
  - **Flask App**: A traditional web application for making predictions.
  - **Streamlit App**: An interactive dashboard for predictions, offering an enhanced user experience.

- **🔄 Input Preprocessing**: Includes log transformations and one-hot encoding of categorical features.

- **📊 Pre-trained Model**: Uses a pre-trained machine learning model (`model.pkl`) for making predictions.

---

## 💻 Requirements

To run this project, you need Python 3.x and the following libraries:

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `streamlit`
- `flask`

---

## ⚙️ Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Aayushipandey54/AI_Predictive_Models_for_Credit_Underwriting.git
    cd AI_Predictive_Models_for_Credit_Underwriting
    ```

2. **Install dependencies**:

    Install all required dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

---

## ⚡ How It Works

### 1️⃣ Data Preprocessing
- Clean the dataset by handling missing values and outliers.
- Encode categorical variables using one-hot encoding and label encoding.
- Split the data into training and testing sets.

### 2️⃣ Model Training
The following machine learning models are trained to assess credit risk:
- Logistic Regression
- Decision Trees
- Random Forests
- Neural Networks

### 3️⃣ Model Evaluation
Evaluate models using:
- **Confusion Matrix**
- **Cross-validation**
- **Accuracy, Recall, Precision, F1-Score**, and **ROC-AUC**

### 4️⃣ Predictions
Generate predictions on unseen data for credit risk assessment.

---

## 🛠️ Usage

1. **Train and evaluate the models**:
    Run the following command to start model training and evaluation:

    ```bash
    python main.py
    ```

2. **For predictions**, use either the Flask or Streamlit app:

   - **Flask App**:
     ```bash
     flask run
     ```
     This will run the Flask API and expose a `/predict` endpoint to accept user data and return loan eligibility predictions.

   - **Streamlit App**:
     ```bash
     streamlit run app.py
     ```
     This will open an interactive web interface where users can fill in their information and view predictions.

---

## 📈 Results

- **Model Accuracy**: Displays performance metrics for all trained models.
- **Confusion Matrix**: Helps analyze classification errors.
- **ROC-AUC Curve**: Provides a visualization of model performance.

---

## 🤝 Contributing

We welcome contributions! Here's how you can contribute:

1. **Fork the repository**.
2. **Create a new branch** for your feature:
    ```bash
    git checkout -b feature-name
    ```

3. **Commit your changes**:
    ```bash
    git commit -m "Add feature"
    ```

4. **Push your changes**:
    ```bash
    git push origin feature-name
    ```

5. **Create a pull request**.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- References for **credit underwriting methodologies**.
- Resources on **machine learning techniques**.

---

### 🚀 Leverage AI-powered predictive models to revolutionize credit underwriting and streamline decision-making.
Key Sections:
About: Describes the purpose and capabilities of the project.
Features: Lists the major features, including the two apps (Flask and Streamlit).
Requirements: Specifies the Python version and libraries required.
Setup: Detailed steps to set up and install the project.
How It Works: Describes the pipeline, including data preprocessing, model training, and evaluation.
Usage: Instructions for running the project locally for training and prediction.
Results: Explains the evaluation metrics and model performance visualizations.
Contributing: Provides guidelines for contributing to the project.
License: MIT License for open-source use.
Acknowledgements: Gives credit for the resources and methods used in the project.
This README is designed to be comprehensive while keeping the instructions clear for users and developers who wish to work with or contribute to the project.



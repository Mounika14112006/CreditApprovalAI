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

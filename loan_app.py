import streamlit as st
import requests
import json


st.set_page_config(
    page_title="Credit Assessment",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
        .main {
            background-color: #f0f8ff;
        }
        .header {
            color: #1d3557;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            margin-top: 20px;
        }
        .subheader {
            color: #457b9d;
            text-align: center;
            font-size: 20px;
            margin-bottom: 20px;
        }
        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
        .footer {
            margin-top: 50px;
            text-align: center;
            font-size: 14px;
            color: #6c757d;
        }
        .banner-image {
            width: 100%;  
            height: 300px;  
            object-fit: cover;  
        }
    </style>
    """,
    unsafe_allow_html=True,
)

if 'page' not in st.session_state:
    st.session_state.page = "home"
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}
if 'eligibility' not in st.session_state:
    st.session_state.eligibility = None

if st.session_state.page == "home":
    st.markdown('<div class="header">Welcome to Credit Assessment 🎉</div>', unsafe_allow_html=True)
    st.markdown(
        '<img class="banner-image" src="https://i.pinimg.com/736x/4e/4a/0f/4e4a0fd9eea22ca4cfa832823d210971.jpg" alt="Banner Image" />',
        unsafe_allow_html=True,
    )
    st.markdown('<div class="subheader">"Your Trusted Companion for Quick and Accurate Loan Eligibility Evaluation"</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.write("### How It Works")
        st.write(
            """
            1. **Provide Your Details**: Fill out a simple form with your information.
            2. **Submit the Form**: Let our AI model evaluate your data.
            3. **Get Instant Results**: See if you're eligible for a loan right away.
            """
        )
        st.image("https://www.iifl.com/files/iifl_insights/images/Pre-qualified-Personal-Loans-Check-Eligibility-and-Process-750.png", use_container_width=True)
    with col2:
        st.write("### Financial Empowerment")
        st.write(
            """
            Our platform is designed to empower you with accurate and reliable
            financial insights. Whether it's a personal loan or a business venture,
            we help you make informed decisions for a brighter future.
            """
        )
        st.image("https://www.prosper.com/wp-content/uploads/2021/08/image.png", use_container_width=True)

    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("Get Started Now"):
        st.session_state.page = "form"
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "form":
    st.write("---")
    st.header("Credit Assessment Form")
    st.write("Fill out the form below to check your loan eligibility.")

    person_age = st.number_input("Age", min_value=18, max_value=100, value=22)
    person_income = st.number_input("Income (₹)", min_value=0, step=1000, value=59000)
    person_home_ownership = st.selectbox("Home Ownership", ["RENT", "OWN", "MORTGAGE"])
    person_emp_length = st.slider("Employment Term (years)", min_value=0.0, max_value=60.0, value=15.5)
    loan_intent = st.selectbox("Loan Intent", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "DEBTCONSOLIDATION"])
    loan_amnt = st.number_input("Loan Amount (₹)", min_value=0, step=100, value=10000)
    loan_int_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=50.0, step=0.1, value=16.02)
    loan_percentage_of_income = st.slider("Loan Percentage of Income", min_value=0.0, max_value=1.0, step=0.01, value=0.59)
    cb_person_default_on_file = st.selectbox("Default on File", ["Y", "N"])
    cb_person_cred_length = st.slider("Credit History Length (years)", min_value=0.0, max_value=30.0, value=5.0)

    form_data = {
        "person_age": person_age,
        "person_income": person_income,
        "person_home_ownership": person_home_ownership,
        "person_emp_length": person_emp_length,
        "loan_intent": loan_intent,
        "loan_amnt": loan_amnt,
        "loan_int_rate": loan_int_rate,
        "loan_percent_income": loan_percentage_of_income,
        "cb_person_default_on_file": cb_person_default_on_file,
        "cb_person_cred_length": cb_person_cred_length,
    }

    st.session_state.form_data = form_data

    if st.button("Check Eligibility"):
        url = 'http://127.0.0.1:5000/predict'  # Your Flask API URL
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(url, data=json.dumps(form_data), headers=headers)
            if response.status_code == 200:
                prediction = response.json()
                st.session_state.eligibility = int(prediction.get("eligibility", 0))  # Convert to integer
                st.session_state.page = "result"
            else:
                st.error(f"Error: {response.json().get('error', 'An unknown error occurred.')}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

elif st.session_state.page == "result":
    st.write("---")
    st.header("Eligibility Results")

    eligibility = st.session_state.eligibility
    if eligibility == 1:
        st.success("Congratulations! You are eligible for a loan. 🎉")
    else:
        st.error("Unfortunately, you are not eligible for a loan at this time. 😞")

    st.write("### Form Details:")
    st.json(st.session_state.form_data)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Go to Form"):
            st.session_state.page = "form"
    with col2:
        if st.button("Go to Home"):
            st.session_state.page = "home"

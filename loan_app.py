import streamlit as st

st.title("Credit Assessment Form")

st.sidebar.header("Applicant Details")

person_age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=22)
person_income = st.sidebar.number_input("Income (₹)", min_value=0, step=1000, value=59000)
person_home_ownership = st.sidebar.selectbox(
    "Home Ownership", ["RENT", "OWN", "MORTGAGE"]
)
person_emp_length = st.sidebar.slider(
    "Employment Term (years)", min_value=0.0, max_value=60.0, value=15.5
)
loan_intent = st.sidebar.selectbox(
    "Loan Intent", ["PERSONAL", "EDUCATION", "MEDICAL", "VENTURE", "DEBTCONSOLIDATION"]
)
loan_grade = st.sidebar.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F"])
loan_amnt = st.sidebar.number_input("Loan Amount (₹)", min_value=0, step=100, value=10000)
loan_int_rate = st.sidebar.slider(
    "Interest Rate (%)", min_value=0.0, max_value=50.0, step=0.1, value=16.02
)
loan_percentage_of_income = st.sidebar.slider(
    "Loan Percentage of Income",min_value=0.0,max_value=1.0,step=0.01,value=0.59
)
cb_person_default_on_file = st.sidebar.selectbox(
    "Default on File", ["Y", "N"]
)
cb_person_cred_length = st.sidebar.slider(
    "Credit History Length (Years)", min_value=0, max_value=50, value=3
)

if st.sidebar.button("Submit"):
    st.header("Submitted Loan Applicant Details")
    st.write({
        "Age": person_age,
        "Income": person_income,
        "Home Ownership": person_home_ownership,
        "Employment Length": person_emp_length,
        "Loan Intent": loan_intent,
        "Loan Grade": loan_grade,
        "Loan Amount": loan_amnt,
        "Interest Rate": loan_int_rate,
        "Loan Percentage of Income": loan_percentage_of_income,
        "Default on File": cb_person_default_on_file,
        "Credit History Length": cb_person_cred_length,
    })
    st.success("Details submitted successfully!")
else:
    st.info("Please complete the form and click submit.")

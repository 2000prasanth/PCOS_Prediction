import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Load the model
model = load('best_model1.pkl')

def predict_outcome(input_data):
    # Convert input data into a DataFrame
    input_df = pd.DataFrame([input_data], columns=feature_names)
    # Predict
    prediction = model.predict(input_df)
    return prediction

# Page configuration
st.set_page_config(page_title="PCOS Prediction", layout="wide")

st.title("PCOS Prediction Tool")

# Define the feature names
feature_names = [' Age (yrs)', 'Weight (Kg)', 'Height(Cm) ', 'Pulse rate(bpm) ',
                 'RR (breaths/min)', 'Hb(g/dl)', 'Cycle(R/I)', 'Cycle length(days)',
                 'Marraige Status (Yrs)', 'Pregnant(Y/N)', 'No. of aborptions',
                 'I    beta-HCG(mIU/mL)', 'II    beta-HCG(mIU/mL)', 'FSH(mIU/mL)',
                 'LH(mIU/mL)', 'Hip(inch)', 'Waist(inch)', 'TSH (mIU/L)', 'AMH(ng/mL)',
                 'PRL(ng/mL)', 'Vit D3 (ng/mL)', 'PRG(ng/mL)', 'RBS(mg/dl)',
                 'Weight gain(Y/N)', 'hair growth(Y/N)', 'Skin darkening (Y/N)',
                 'Hair loss(Y/N)', 'Pimples(Y/N)', 'Fast food (Y/N)',
                 'Reg.Exercise(Y/N)', 'BP _Systolic (mmHg)', 'BP _Diastolic (mmHg)',
                 'Follicle No. (L)', 'Follicle No. (R)', 'Avg. F size (L) (mm)',
                 'Avg. F size (R) (mm)', 'Endometrium (mm)']

# Create input fields for each feature
inputs = {}
for feature in feature_names:
    # Determine if the input should be a number or a binary choice
    if "Y/N" in feature:
        inputs[feature] = st.selectbox(f"{feature}", ['Yes', 'No'], format_func=lambda x: '1' if x == 'Yes' else '0')
    else:
        inputs[feature] = st.number_input(f"{feature}", value=0.0)

# Button to make prediction
if st.button("Predict"):
    # Convert binary inputs from Yes/No to 1/0
    binary_features = [key for key in inputs if "Y/N" in key]
    for bf in binary_features:
        inputs[bf] = 1 if inputs[bf] == 'Yes' else 0

    # Make prediction
    prediction = predict_outcome(inputs)
    # Display the prediction
    st.write("Prediction: PCOS" if prediction[0] == 1 else "Prediction: No PCOS")


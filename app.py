import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import time
import base64

# ---- Config & setting page icon and title ----
app_icon = Image.open("logo.png")
st.set_page_config(page_title="Plant Nutrition", page_icon=app_icon, layout="centered")

# ---- Hiding the menu and streamlit footer note ----
hide_menu = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_menu, unsafe_allow_html=True)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('next.jpg') 


st.markdown("<h1 style='text-align: center;'>--Predictions of Plant Nutrition-- </h1>", unsafe_allow_html=True)



# import model
models = pickle.load(open("pipeline.pkl", "rb"))

st.markdown("<h4 style='text-align: left;'>Please Input Features to Predict : </h4>", unsafe_allow_html=True)


# user input
with st.form(key='form_parameters'):
    v1 = st.slider(label='What is the number of V1 ? ', min_value=227.285714, max_value=1000.0, value=389.892437, step=0.01)
    v2 = st.slider(label='What is the number of V2 ? ', min_value=178.800000, max_value=1000.0, value=237.442677, step=0.01)
    v3 = st.slider(label='What is the number of V3 ? ', min_value=348.933333, max_value=1000.0, value=480.573041, step=0.01)
    v4 = st.slider(label='What is the number of V4 ? ', min_value=313.733333, max_value=1000.0, value=394.109622, step=0.01)
    v5 = st.slider(label='What is the number of V5 ? ', min_value=373.333333, max_value=1000.0, value=487.316520, step=0.01)
    v6 = st.slider(label='What is the number of V6 ? ', min_value=189.200000, max_value=1000.0, value=251.450820	, step=0.01)
    v7 = st.slider(label='What is the number of V7 ? ', min_value=586.266667, max_value=1000.0, value=714.737926, step=0.01)
    v8 = st.slider(label='What is the number of V8 ? ', min_value=3725.666667, max_value=6000.0, value=4456.913233, step=0.01)
    sample_type = st.selectbox(label='Select the sample type', options=['lab 1', 'lab 2'])
    
    submitted = st.form_submit_button('Predict')

if submitted:
        # --- showing progress bar ---
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i+1)

# convert into dataframe
data = pd.DataFrame({'v1': [v1],
                'v2': [v2],
                'v3': [v3],
                'v4':[v4],
                'v5': [v5],
                'v6': [v6],
                'v7': [v7],
                'v8': [v8],
                'sample_type': [sample_type]})


# model predict
pred = models.predict(data).tolist()[0]
predround = round(pred,2)

# interpretation

st.markdown("<h3 style='text-align: left;'>The prediction result of the nutritional value of plants is: </h3>",unsafe_allow_html=True)
st.write(predround)
st.markdown("<h5 style='text-align: center;'>Please check your input on the table </h5>", unsafe_allow_html=True)

data

st.write(' The prediction results from the data entered by the user are as follows :',predround, '\n These predictions may change at any time according to changes in the number of each input feature.')
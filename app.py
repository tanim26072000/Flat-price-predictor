import streamlit as st
import pandas as pd
import pickle

st.title('Flat price predictor within Dhaka')
model = pickle.load(open('ridgemodel.pkl', 'rb'))
df = pd.read_csv('cleaned_data.csv')
location = st.selectbox('type your desired location:',
                        sorted(df['Location'].unique()))
bed = st.text_input("Enter required no. of bedroom:")
bath = st.text_input("Enter required no. of bathroom:")
size = st.text_input("Enter required size:")

if st.button('Predict'):
    bed, bath, size = map(float, [bed, bath, size])
    test = {'Location': location, 'Bed': bed, 'Bath': bath, 'Area': size}
    x_test = pd.DataFrame(test, index=[0])
    prediction = model.predict(x_test)
    p_int = int(prediction[0])
    crore = p_int//10000000
    lakh = p_int % 10000000
    lakh = lakh//100000
    s = f'the price of a flat with desired features in desired location can be almost'
    s1 = ''
    s2 = ''
    if (crore > 0):
        s1 = f' {crore} crore(s)'
        s = s+s1
    if (lakh > 0):
        s2 = f' {lakh} lakh(s)'
        s = s+s2
    st.write(s)

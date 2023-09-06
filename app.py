import streamlit as st
import pandas as pd
import pickle

st.title('Flat rent predictor within Dhaka')
model = pickle.load(open('ridgemodel.pkl', 'rb'))
df = pd.read_csv('cleaned_data.csv')
bed, bath, size = 0, 0, 0
location = st.selectbox('type your desired location:',
                        df['Location'].unique())
bed = st.text_input("Enter required no. of bedroom:")
bath = st.text_input("Enter required no. of bathroom:")
size = st.text_input("Enter required size (in sqft):")


if st.button('Predict'):
    if (bed == 0):
        st.write("No. of bed can't be empty")
        exit()
    if (bath == 0):
        st.write("No. of bath can't be empty")
        exit()
    if (size == 0):
        st.write("size can't be empty")
        exit()
    st.write(bed)
    bed, bath, size = map(float, [bed, bath, size])
    test = {'Location': location, 'Bed': bed, 'Bath': bath, 'Area': size}
    x_test = pd.DataFrame(test, index=[0])
    prediction = model.predict(x_test)
    p_int = int(prediction[0])
    crore = p_int//100000
    lakh = p_int % 100000
    lakh = lakh//1000
    s = f'The rent of a flat with desired features in desired location can be around'
    s1 = ''
    s2 = ''
    if (crore > 0):
        s1 = f' {crore} lakh(s)'
        s = s+s1
    if (lakh > 0):
        s2 = f' {lakh} Thousand(s)'
        s = s+s2
    st.write(s)

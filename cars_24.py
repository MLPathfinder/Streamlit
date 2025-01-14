import streamlit as st
import pickle

st.title('Car Price Prediction App')

encode_dict = {
    'Fuel': {'DIESEL': 1, 'PETROL': 2, 'CNG': 3, 'LPG': 4},
    'Drive': {'Manual': 1, 'Automatic': 2},
    'Type': {'HatchBack': 1, 'Sedan': 2, 'SUV': 3, 'Lux_SUV': 4, 'Lux_sedan': 5}
}


model = pickle.load(open('car_price_model.pkl', 'rb'))

st.subheader('Please enter the details of the car')
year_value = st.slider('Manufacturing Year', min_value=1990, max_value=2023, value = 2018, step = 1)
distance = st.number_input('Distance Travelled (in km)', min_value=0, max_value=1000000, value = 50000, step = 1000)
owner = st.selectbox('Number of Owners', [1, 2, 3, 4])
fuel_type = st.selectbox('Fuel Type', ['DIESEL', 'PETROL', 'CNG', 'LPG'])
drive = st.selectbox('Drive Type', ['Manual', 'Automatic'])
car_type = st.selectbox('Car Type', ['HatchBack', 'Sedan', 'SUV', 'Lux_SUV', 'Lux_sedan'])

def model_predict(year, distance, owner, fuel, drive, car_type):
    fuel = encode_dict['Fuel'][fuel]
    drive = encode_dict['Drive'][drive]
    car_type = encode_dict['Type'][car_type]
    price = model.predict([[year, distance, owner, fuel, drive, car_type]])
    return price


if st.button('Predict Price'):
    price = model_predict(year_value, distance, owner, fuel_type, drive, car_type)
    st.success(f'The predicted price of the car is {price[0]} lakhs')   
else:
    st.write('Click on the button to get the price prediction')




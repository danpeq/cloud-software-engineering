import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Datos de Anuncio de venta de autos')

car_data = pd.read_csv('./vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir grafico de dispersion') # crear otro botón

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

casilla_button = st.checkbox('Construir boton casilla de verificación') #crear botón

if casilla_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de casilla de verificación')
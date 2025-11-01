import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(
    "https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv"
)


# Título y descripción de la app
st.title("Análisis Descriptivo de Vehículos")
st.write(
    "Esta aplicación permite explorar un dataset de vehículos, proporcionando estadísticas y visualizaciones interactivas."
)

st.dataframe(df.describe())

st.dataframe(df)

filtro_marca = df.groupby('Brand')['Price'].mean()
st.dataframe(filtro_marca)
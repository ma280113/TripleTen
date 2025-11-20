import pandas as pd
import streamlit as st

df = pd.read_csv('https://raw.githubusercontent.com/anfagudelogo-tpt/datasets/refs/heads/main/car_price_dataset.csv')
st.dataframe(df)
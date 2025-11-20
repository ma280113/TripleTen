import streamlit as st

st.title("🚀 Mi primera app con Streamlit")
st.header("Subtítulo o sección principal")
st.subheader("Sección secundaria")
st.text("Texto normal o descripción")
st.markdown("**Markdown** también es soportado 💪")

import pandas as pd

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Marta'],
    'Edad': [25, 30, 22],
    'Ciudad': ['Bogotá', 'Medellín', 'Cali']
})

st.dataframe(df)          # Mostrar tabla interactiva
st.table(df.head())       # Mostrar tabla estática
st.json({"key": "value"}) # Mostrar JSON


import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(100)

# Gráficos integrados
st.line_chart(data)
st.bar_chart(np.abs(data))
st.area_chart(data)

# Gráficos personalizados
fig, ax = plt.subplots()
ax.hist(data, bins=20)
st.pyplot(fig)
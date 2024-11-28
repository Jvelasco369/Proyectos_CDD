#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Título y descripción principal
st.title("Jonathan Velasco - CV Interactivo")
st.markdown("""
### Arquitecto de Soluciones de Datos e Inteligencia Artificial  
Bienvenido a mi CV interactivo. Aquí podrás explorar mi experiencia profesional, certificaciones y algunos ejemplos de visualizaciones que reflejan mi capacidad en análisis de datos, inteligencia de negocios y más.
""")

# Sección: Acerca de mí
st.header("Acerca de mí")
st.write("""
Soy un profesional en Inteligencia de Negocios con experiencia en liderar proyectos de analítica avanzada, transformación digital y soluciones basadas en datos. Me especializo en:
- Diseño de arquitecturas de datos y analítica.
- Gestión de proyectos bajo metodologías PMP.
- Ciencia de datos e inteligencia artificial aplicadas.
""")

# Experiencia profesional
st.header("Experiencia Profesional")
st.subheader("Consultor Especializado – Andrade & Vázquez (2024 - Actualidad)")
st.write("""
Diseño de arquitecturas analíticas y gestión de proyectos para sectores gubernamentales y privados. Liderazgo en transformación digital y estrategias de gobierno de datos.
""")

st.subheader("Lead Business Intelligence Consultant – Microsoft (2023 - 2024)")
st.write("""
Lideré proyectos de analítica avanzada, optimización de flujos de trabajo y reportes globales, implementando técnicas avanzadas de inteligencia artificial.
""")

# Gráfica interactiva
st.header("Visualización de datos: Ejemplo público")
st.markdown("""
A continuación, se muestra una gráfica interactiva basada en datos abiertos que demuestra habilidades en análisis de datos y visualización.
""")

# Cargar datos de ejemplo
@st.cache
def load_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Procesar datos
data_filtered = data[data["location"].isin(["Mexico", "United States", "Canada"])]
fig = px.line(
    data_filtered,
    x="date",
    y="total_vaccinations",
    color="location",
    title="Progresión de vacunación COVID-19 (Ejemplo público)"
)

# Mostrar gráfica
st.plotly_chart(fig)

# Certificaciones
st.header("Certificaciones")
st.write("""
- Ingeniería de Datos con Microsoft Azure  
- Certificación Profesional en Ciencia de Datos – IBM  
- Inteligencia Artificial – CertNexus  
- Gestión de Proyectos – Google  
""")

# Contacto
st.header("Contacto")
st.write("""
📧 **Correo:** yisaivelasco@gmail.com  
📞 **Teléfono:** 5526982673  
🌐 **GitHub:** [Perfil en GitHub](https://github.com/tu_usuario)
""")


# In[ ]:





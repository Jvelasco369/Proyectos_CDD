#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install yfinance')


# In[2]:


import yfinance as yf
import pandas as pd

# Crear un objeto Ticker para GameStop (símbolo: GME)
gme = yf.Ticker("GME")

# Descargar los datos históricos (por ejemplo, para los últimos 5 años)
historial = gme.history(period="5y")

# Mostrar los primeros datos para verificar
print(historial.head())

# Guardar el DataFrame en un archivo CSV
historial.to_csv("gme_historial.csv")
print("Los datos de GameStop se han guardado en 'gme_historial.csv'.")


# In[ ]:





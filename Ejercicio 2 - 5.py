#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd

# Símbolo de GameStop
symbol = "GME"

# Descargar datos históricos de GameStop
gme_data = yf.download(symbol, start="2015-01-01", end="2023-12-31")

# Mostrar los primeros datos
print(gme_data.head())

# Guardar los datos en un archivo CSV (opcional)
gme_data.to_csv("GME_price_history.csv")

# Visualización de datos en DataFrame
gme_data


# In[ ]:





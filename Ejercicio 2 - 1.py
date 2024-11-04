#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install yfinance


# In[2]:


import yfinance as yf
import pandas as pd


# In[3]:


# Descargar datos de Tesla utilizando yfinance
tesla = yf.Ticker("TSLA")

# Extraer datos históricos (ejemplo: último año)
datos_historicos = tesla.history(period="1y")

# Mostrar los primeros registros para verificar la extracción
print(datos_historicos.head())


# In[4]:


# Guardar los datos históricos en un archivo CSV
datos_historicos.to_csv("tesla_historical_data.csv")


# In[5]:


import matplotlib.pyplot as plt

# Visualizar el precio de cierre de Tesla durante el último año
plt.figure(figsize=(10, 5))
plt.plot(datos_historicos.index, datos_historicos['Close'], label='Precio de Cierre')
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre (USD)')
plt.title('Precio de Cierre de Tesla en el Último Año')
plt.legend()
plt.grid()
plt.show()


# In[6]:


pip install requests
pip install beautifulsoup4


# In[7]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar datos de Tesla utilizando yfinance
tesla = yf.Ticker("TSLA")

# Extraer datos históricos (ejemplo: último año)
datos_historicos = tesla.history(period="1y")

# Mostrar los primeros registros para verificar la extracción
print(datos_historicos.head())

# Guardar los datos históricos en un archivo CSV
datos_historicos.to_csv("tesla_historical_data.csv")

# Visualizar el precio de cierre de Tesla durante el último año
plt.figure(figsize=(10, 5))
plt.plot(datos_historicos.index, datos_historicos['Close'], label='Precio de Cierre')
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre (USD)')
plt.title('Precio de Cierre de Tesla en el Último Año')
plt.legend()
plt.grid()
plt.show()


# In[ ]:





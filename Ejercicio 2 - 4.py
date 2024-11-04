#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests beautifulsoup4')


# In[2]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de ingresos de GameStop en Macrotrends
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Realizar la solicitud HTTP
response = requests.get(url)
if response.status_code == 200:
    print("Solicitud exitosa")
else:
    print("Error en la solicitud")

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Extraer la tabla de ingresos
table = soup.find('table', {'class': 'historical_data_table'})

# Extraer las filas de la tabla
rows = table.find_all('tr')

# Listas para almacenar los datos
years = []
revenues = []

# Iterar sobre las filas para extraer año e ingresos
for row in rows[1:]:  # Saltamos la primera fila de encabezado
    cols = row.find_all('td')
    if len(cols) > 1:
        year = cols[0].text.strip()
        revenue = cols[1].text.strip()
        years.append(year)
        revenues.append(revenue)

# Crear un DataFrame con los datos
data = pd.DataFrame({
    'Year': years,
    'Revenue': revenues
})

# Mostrar los primeros datos para verificar
print(data.head())

# Guardar el DataFrame en un archivo CSV
data.to_csv("gamestop_revenue.csv", index=False)
print("Los datos de ingresos de GameStop se han guardado en 'gamestop_revenue.csv'.")


# In[3]:


import requests
from bs4 import BeautifulSoup

# URL de ingresos de GameStop en Macrotrends
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Realizar la solicitud HTTP
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
if response.status_code == 200:
    print("Solicitud exitosa")
    # Revisar el contenido HTML recibido
    print(response.text[:500])  # Imprime los primeros 500 caracteres del HTML
else:
    print("Error en la solicitud")

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar y revisar todas las tablas para identificar la correcta
tables = soup.find_all('table')
print(f"Cantidad de tablas encontradas: {len(tables)}")

# Imprimir clases de tablas para ver cuál es la correcta
for idx, table in enumerate(tables):
    print(f"Tabla {idx} tiene las siguientes clases: {table.get('class')}")

# Una vez que identifiques la tabla correcta, ajusta el código original


# In[ ]:





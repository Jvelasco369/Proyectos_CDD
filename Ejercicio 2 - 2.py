#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install requests
pip install beautifulsoup4


# In[2]:


get_ipython().system('pip install requests')
get_ipython().system('pip install beautifulsoup4')


# In[3]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[4]:


# URL de ingresos de Tesla en Macrotrends
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Realizar la solicitud HTTP
response = requests.get(url)
if response.status_code == 200:
    print("Solicitud exitosa")
else:
    print("Error en la solicitud")

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')


# In[5]:


import requests
from bs4 import BeautifulSoup

# URL de ingresos de Tesla en Macrotrends
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Definir encabezados de agente de usuario
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Realizar la solicitud HTTP
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    print("Solicitud exitosa")
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
else:
    print("Error en la solicitud")


# In[6]:


# Buscar la tabla que contiene los datos de ingresos
tabla_ingresos = soup.find_all('table', {'class': 'historical_data_table table'})

# Si la tabla existe
if len(tabla_ingresos) > 0:
    tabla = tabla_ingresos[0]

    # Extraer las filas de la tabla
    filas = tabla.find_all('tr')

    # Almacenar los datos en una lista
    ingresos = []

    for fila in filas:
        celdas = fila.find_all('td')
        if len(celdas) > 0:
            fecha = celdas[0].text.strip()
            ingreso = celdas[1].text.strip()
            ingresos.append([fecha, ingreso])

    # Crear un DataFrame de Pandas con los ingresos
    df_ingresos = pd.DataFrame(ingresos, columns=['Fecha', 'Ingresos'])
    print(df_ingresos)

    # Guardar en un archivo CSV
    df_ingresos.to_csv('ingresos_tesla.csv', index=False)
else:
    print("No se encontró la tabla de ingresos.")


# In[7]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de ingresos de Tesla en Macrotrends
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Realizar la solicitud HTTP
response = requests.get(url)
if response.status_code == 200:
    print("Solicitud exitosa")
else:
    print("Error en la solicitud")

# Parsear el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Buscar la tabla que contiene los datos de ingresos
tabla_ingresos = soup.find_all('table', {'class': 'historical_data_table table'})

# Si la tabla existe
if len(tabla_ingresos) > 0:
    tabla = tabla_ingresos[0]

    # Extraer las filas de la tabla
    filas = tabla.find_all('tr')

    # Almacenar los datos en una lista
    ingresos = []

    for fila in filas:
        celdas = fila.find_all('td')
        if len(celdas) > 0:
            fecha = celdas[0].text.strip()
            ingreso = celdas[1].text.strip()
            ingresos.append([fecha, ingreso])

    # Crear un DataFrame de Pandas con los ingresos
    df_ingresos = pd.DataFrame(ingresos, columns=['Fecha', 'Ingresos'])
    print(df_ingresos)

    # Guardar en un archivo CSV
    df_ingresos.to_csv('ingresos_tesla.csv', index=False)
else:
    print("No se encontró la tabla de ingresos.")


# In[8]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de ingresos de Tesla en Macrotrends
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Realizar la solicitud HTTP a la página web
response = requests.get(url)
if response.status_code == 200:
    print("Solicitud exitosa")
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar la tabla de datos de ingresos
    table = soup.find('table', {'class': 'historical_data_table'})
    if table:
        # Extraer las filas de la tabla
        rows = table.find_all('tr')
        
        # Listas para almacenar los datos
        years = []
        revenues = []
        
        # Iterar sobre las filas y extraer los datos
        for row in rows[1:]:  # Omitimos la primera fila (encabezados)
            cols = row.find_all('td')
            if len(cols) == 2:  # Comprobar que haya dos columnas (año y ingreso)
                year = cols[0].text.strip()
                revenue = cols[1].text.strip()
                years.append(year)
                revenues.append(revenue)
        
        # Crear un DataFrame con los datos extraídos
        data = pd.DataFrame({'Año': years, 'Ingresos': revenues})
        
        # Mostrar el DataFrame
        print(data)
    else:
        print("Tabla de datos no encontrada")
else:
    print("Error en la solicitud")


# In[9]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL de ingresos de Tesla en Macrotrends
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Definir las cabeceras, incluyendo un User-Agent para simular un navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

# Realizar la solicitud HTTP a la página web
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Solicitud exitosa")
    # Parsear el contenido HTML
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Buscar la tabla de datos de ingresos
    table = soup.find('table', {'class': 'historical_data_table'})
    if table:
        # Extraer las filas de la tabla
        rows = table.find_all('tr')
        
        # Listas para almacenar los datos
        years = []
        revenues = []
        
        # Iterar sobre las filas y extraer los datos
        for row in rows[1:]:  # Omitimos la primera fila (encabezados)
            cols = row.find_all('td')
            if len(cols) == 2:  # Comprobar que haya dos columnas (año y ingreso)
                year = cols[0].text.strip()
                revenue = cols[1].text.strip()
                years.append(year)
                revenues.append(revenue)
        
        # Crear un DataFrame con los datos extraídos
        data = pd.DataFrame({'Año': years, 'Ingresos': revenues})
        
        # Mostrar el DataFrame
        print(data)
    else:
        print("Tabla de datos no encontrada")
else:
    print("Error en la solicitud")


# In[ ]:





import streamlit as st
import pandas as pd 
from openpyxl import load_workbook

#Configuración de la página
st.set_page_config(
    page_title="Nacimientos en Colombia DANE",
    page_icon="📈",
    layout="wide")

#Titulo y descripción de la pagina
st.title("Nacimientos en Colombia (2014-2025) ")
st.write(
    "Este diagrama de líneas muestra la evolución de los nacimientos en Colombia durante los últimos 10 años:")
st.divider()

#Ruta del archivo Excel
archivo = "datos/nacimientos_colombia_2014_2025.xlsx"

# Cargar el archivo Excel
wb = load_workbook(archivo, data_only=True)
ws = wb.active

# Crear una lista para almacenar los datos y separar los encabezados de las filas
datos = list(ws.values)
encabezados = datos[0]  # Primera fila como encabezados
filas = datos[1:]  # Resto de las filas como datos

# Crear un DataFrame de pandas con los datos
df = pd.DataFrame(filas, columns=encabezados)
df = df[["Año", "Número de Nacimientos"]]

# Asegurar que sean números
df["Año"] = pd.to_numeric(df["Año"], errors="coerce")
df["Número de Nacimientos"] = pd.to_numeric(df["Número de Nacimientos"], errors="coerce")

#Gráfico de líneas con Streamlit
st.line_chart(df, x="Año", y="Número de Nacimientos", width="stretch")
st.divider()

# Pie de página
st.caption("Fuente de datos: Departamento Administrativo Nacional de Estadística (DANE)")
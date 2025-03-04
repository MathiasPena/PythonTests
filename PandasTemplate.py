import pandas as pd
import numpy as np

# CREAR DATAFRAMES
data = {
    "id": [1, 2, 3, 4, 5],
    "nombre": ["Ana", "Luis", "Pedro", "Sofia", "Juan"],
    "edad": [25, 30, np.nan, 22, 40],
    "salario": [3000, 4000, 5000, np.nan, 7000],
    "departamento": ["IT", "HR", "IT", "Sales", "HR"]
}
df = pd.DataFrame(data)

# EXPLORAR DATAFRAME
print(df.head())       # Primeras filas
print(df.info())       # Información general
print(df.describe())   # Estadísticas generales
print(df.columns)      # Nombres de columnas
print(df.dtypes)       # Tipos de datos

# SELECCIÓN DE DATOS
print(df["nombre"])      # Columna específica
print(df[["nombre", "edad"]])  # Varias columnas
print(df.loc[1])         # Fila específica
print(df.iloc[0:3])      # Primeras 3 filas

# FILTRADO DE DATOS
print(df[df["edad"] > 25])  # Filtrar por condición
print(df[(df["edad"] > 25) & (df["departamento"] == "IT")])  # Filtrar con varias condiciones

# LIMPIEZA DE DATOS
df2 = df.dropna(subset=["edad"])  # Eliminar filas con NaN en "edad"
df["salario"].fillna(df["salario"].mean(), inplace=True)  # Reemplazar NaN con media
df["edad"] = df["edad"].astype(int)  # Convertir tipo de dato

# ORDENAR Y AGRUPAR
df.sort_values(by="salario", ascending=False, inplace=True)  # Ordenar por salario
print(df.groupby("departamento")["salario"].mean())  # Salario promedio por departamento

# CREAR, MODIFICAR Y ELIMINAR COLUMNAS
df["impuesto"] = df["salario"] * 0.10  # Nueva columna con impuestos
df["nombre_completo"] = df["nombre"] + " Pérez"  # Concatenar strings
df2 = df.drop(columns=["impuesto"])  # Eliminar columna

# JOINS Y CONCATENACIÓN
df2 = pd.DataFrame({
    "id": [3, 4, 5, 6],
    "proyecto": ["A", "B", "C", "D"]
})
df_merged = pd.merge(df, df2, on="id", how="left")  # Left Join

# FUNCIONES Y APLICACIONES
df["bono"] = df["salario"].apply(lambda x: x * 0.05)  # Aplicar función a columna
df["departamento"] = df["departamento"].replace({"IT": "Tecnología", "HR": "Recursos Humanos"})  # Reemplazo valores

# EXPORTAR
df.to_csv("datos_procesados.csv", index=False)  # Guardar como CSV

print(df)

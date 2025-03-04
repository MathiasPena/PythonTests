# Importaciones Esenciales
import pandas as pd
import numpy as np
import os
import logging
import json
import psycopg2  # Para conectar con PostgreSQL
from sqlalchemy import create_engine
from datetime import datetime
from multiprocessing import Pool

# Configuración de Logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Cargar Datos desde Diferentes Fuentes
def load_data():
    # CSV
    df_csv = pd.read_csv("data.csv")
    
    # JSON
    df_json = pd.read_json("data.json")
    
    # Excel
    df_excel = pd.read_excel("data.xlsx", sheet_name="Sheet1")
    
    # Base de datos (PostgreSQL)
    engine = create_engine("postgresql://user:password@localhost:5432/mydb")
    df_sql = pd.read_sql("SELECT * FROM tabla", con=engine)
    
    return df_csv, df_json, df_excel, df_sql

# Transformaciones de Datos
def transform_data(df):
    # Eliminar valores nulos
    df.dropna(inplace=True)

    # Renombrar columnas
    df.rename(columns={"old_col": "new_col"}, inplace=True)

    # Crear nuevas columnas
    df["total"] = df["precio"] * df["cantidad"]

    # Filtrar datos
    df = df[df["total"] > 100]

    # Convertir formatos de fecha
    df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d")

    return df

# Guardar Datos
def save_data(df, format="csv"):
    if format == "csv":
        df.to_csv("output.csv", index=False)
    elif format == "json":
        df.to_json("output.json", orient="records")
    elif format == "parquet":
        df.to_parquet("output.parquet")

# Cargar Datos en PostgreSQL
def load_to_postgres(df, table_name):
    engine = create_engine("postgresql://user:password@localhost:5432/mydb")
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)

# Procesamiento en Paralelo
def process_chunk(chunk):
    chunk["new_col"] = chunk["col"] * 2  # Ejemplo de transformación
    return chunk

def parallel_processing(df):
    num_partitions = 4  # Número de divisiones
    pool = Pool(num_partitions)
    df_split = np.array_split(df, num_partitions)
    df = pd.concat(pool.map(process_chunk, df_split))
    pool.close()
    pool.join()
    return df

# Flujo ETL Completo
def etl_pipeline():
    logging.info("Cargando datos...")
    df_csv, df_json, df_excel, df_sql = load_data()

    logging.info("Transformando datos...")
    df_csv = transform_data(df_csv)

    logging.info("Procesamiento en paralelo...")
    df_csv = parallel_processing(df_csv)

    logging.info("Guardando datos...")
    save_data(df_csv, format="parquet")

    logging.info("Cargando datos a PostgreSQL...")
    load_to_postgres(df_csv, "final_table")

    logging.info("ETL finalizado con éxito!")

# Ejecutar ETL
if __name__ == "__main__":
    etl_pipeline()

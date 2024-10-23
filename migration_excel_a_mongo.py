import pandas as pd
from pymongo import MongoClient

# Ruta al archivo Excel
ruta_excel = "/home/cm7chael/Descargas/personas.xls"

# Nombre de la hoja en el archivo Excel
nombre_hoja = "persona"

# Leer el archivo Excel usando pandas
df = pd.read_excel(ruta_excel, sheet_name=nombre_hoja)

# Conectar a MongoDB
cliente = MongoClient("mongodb://localhost:27017/")  # Ajusta la URI si es necesario
db = cliente["prueba"]
coleccion = db["personas"]

# Convertir el DataFrame de pandas a una lista de diccionarios
data_dict = df.to_dict("records")

# Insertar los datos en la colección de MongoDB
coleccion.insert_many(data_dict)

print(f"Se han insertado {len(data_dict)} registros en la base de datos.")

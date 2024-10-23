# Migración de Datos de Excel a MongoDB

Este proyecto permite migrar datos de un archivo Excel a una base de datos MongoDB utilizando Python.

## Requisitos

- Python 3.6 o superior
- MongoDB instalado y en funcionamiento

## Librerías instaladas

El proyecto utiliza las siguientes librerías de Python:

- `pandas`: Para la manipulación de datos y la lectura del archivo Excel.
- `openpyxl`: Para leer archivos Excel en formato `.xlsx`.
- `pymongo`: Para la conexión y operación con MongoDB.
- `xlrd`: Para leer archivos Excel en formato `.xls`.

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio

2. **Crear un entorno virtual:**
  python3 -m venv mi_entorno

3. **Activar el entorno virtual:**
  source mi_entorno/bin/activate

4. **Instalar las dependencias:**
  pip install pandas openpyxl pymongo xlrd



## Ejecución

1. **Activa el entorno virtual (si no está activo):**
  source mi_entorno/bin/activate

2. **Ejecuta el script:**
  python migration_excel_a_mongo.py


3. **Desactivar el entorno virtual**
deactivate

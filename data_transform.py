import pandas as pd
import os

# Ruta del archivo CSV intermedio
archivo_csv = 'produccion.csv'

try:
     # Verificar si el archivo existe
    if not os.path.exists(archivo_csv):
        raise FileNotFoundError(f"El archivo {archivo_csv} no existe.")
    
    # Leer el archivo CSV
    data = pd.read_csv(archivo_csv)
    
    # Ordenar los datos por nombre
    data_ordenada = data.sort_values(by='Fecha')
    
    # Exportar a Excel
    archivo_excel = 'produccion_ordenada.xlsx'
    data_ordenada.to_excel(archivo_excel, index=False)
    
    print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")
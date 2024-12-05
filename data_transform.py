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
    
    # Eliminar filas con valores nulos
    data_limpia = data.dropna()
    
    # Eliminar filas duplicadas
    data_limpia = data_limpia.drop_duplicates()
    
    # Ordenar los datos por fecha
    data_ordenada = data_limpia.sort_values(by='Fecha')
    
    # Exportar a Excel
    archivo_excel = 'produccion_ordenada_limpia.xlsx'
    data_ordenada.to_excel(archivo_excel, index=False)
    
    print(f"Datos transformados exitosamente a {archivo_excel}")
except Exception as e:
    print(f"Error al transformar los datos: {e}")

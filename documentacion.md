# Documentación del Proyecto

## Introducción
Este proyecto tiene como objetivo la transformación y limpieza de datos de producción en una planta, automatizando el procesamiento y generando un archivo Excel ordenado y limpio para el análisis.

El proyecto aborda la problemática de la inconsistencia en los datos almacenados manualmente o en formatos como Excel, que a menudo sufren modificaciones sin control de versiones y errores en su calidad.

---

## Estructura del Proyecto
El proyecto incluye los siguientes archivos:
- **`data_transform.py`**: Script principal que realiza las operaciones de transformación de datos.
- **`produccion.csv`**: Archivo de entrada con los datos de producción.
- **`produccion_ordenada_limpia.xlsx`**: Archivo generado tras la transformación.

---

## Problemática Resuelta
La producción y calidad manual dificultaban:
1. Controlar las modificaciones de los datos.
2. Eliminar errores como duplicados y valores nulos.
3. Centralizar y organizar la información para análisis rápido.

El script soluciona estos problemas al automatizar la transformación y aplicar control de versiones mediante Git.

---

## Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de cumplir con los siguientes requisitos:

1. **Instalar Python 3.x**:
   Descarga e instala desde [python.org](https://www.python.org/downloads/).
   
2. **Librerías Necesarias**:
   - `pandas`
   - `os`

   Instálalas con:
   ```bash
   pip install pandas

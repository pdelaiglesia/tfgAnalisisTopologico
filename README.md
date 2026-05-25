# Análisis Topológico de Datos - TFG

En este repositorio presento el código fuente y la memoria de mi Trabajo Fin de Grado en Ingeniería Informática. El proyecto se centra en aplicar técnicas de Análisis Topológico de Datos (TDA) para estudiar la evolución de la polarización política en Estados Unidos.

Para ello, hemos utilizado los datos de la encuesta American National Election Studies (ANES), analizando cómo cambia la topología del espacio de opinión pública sobre la pol. Hemos podido observar la evolución dividiendo el análisis en tres fases acumulativas: institucional, eje político y partidos políticos.
## Estructura del repositorio

* `código/preprocesamiento.py`: Script encargado de la extracción y limpieza de datos. Selecciona las 8 variables de interés del archivo crudo, elimina los códigos de error o respuestas nulas y normaliza los valores para generar el archivo limpio.
* `código/tda.py`: Script principal que ejecuta el pipeline de homología persistente. A partir de los datos procesados, calcula los complejos de Vietoris-Rips y genera diagramas de persistencia e imágenes de persistencia vectorizadas.
* `Memoria_tfg.pdf`: Documento completo con la memoria del Trabajo Fin de Grado.

## Requisitos y dependencias

Para poder ejecutar los scripts correctamente, es necesario contar con las siguientes librerías instaladas en Python:

* `pandas`
* `numpy`
* `matplotlib`
* `seaborn`
* `ripser`
* `persim`
* `scikit-learn`

## Instrucciones de uso

1.  **Preparación de los datos**: Asegúrate de tener el archivo original de datos de ANES (`anes_timeseries_cdf_csv_20220916.csv`) en el mismo directorio de ejecución.
2.  **Preprocesamiento**: Ejecuta el primer script para limpiar y estandarizar los datos. Este paso es obligatorio para generar el archivo `anes_para_tda.csv`.
    ```bash
    python preprocesamiento.py
    ```
3.  **Análisis Topológico**: Una vez extraídos los datos limpios, ejecuta el algoritmo de TDA.
    ```bash
    python tda.py
    ```
    Al terminar la ejecución, el programa creará automáticamente las carpetas `graficos_individuales`, `graficos_evolucion` y `graficos_completos_por_anio`, donde se guardarán todas las representaciones gráficas y mapas de calor resultantes del análisis.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Comenzamos Preprocesamiento")

# Seleccionamos variables: Las 8 mencionadas y el Año
columnas_deseadas = [
    'VCF0004','VCF0428', 'VCF0429', 'VCF9005','VCF0210', 'VCF0211', 'VCF0212','VCF0218', 'VCF0224'
]
#Cargamos el CSV y seleccionamos las columnas que queremos
df_raw = pd.read_csv(
    'anes_timeseries_cdf_csv_20220916.csv',
    usecols=columnas_deseadas,
    low_memory=False
)
#Cambiamos el nombre de la columna del año por "YEAR"
df_raw = df_raw.rename(columns={'VCF0004': 'YEAR'})
variables_tda = ['VCF0428', 'VCF0429', 'VCF9005', 'VCF0210', 'VCF0211', 'VCF0212', 'VCF0218', 'VCF0224']
#Dejamos las columnas en el formato que deseamos
for col in df_raw.columns:
    df_raw[col] = pd.to_numeric(df_raw[col], errors='coerce')

# Normalización
# Convertimos los códigos de error por NA
df_cleaned = df_raw.replace([98, 99], np.nan)

# Eliminamos filas incompletas
df_cleaned = df_cleaned.dropna(subset=variables_tda)

# Normalizamos las columnas a 0-1
df_tda = df_cleaned.copy()
df_tda[variables_tda] = df_tda[variables_tda] / 97.0

print(f"Filas: {len(df_tda)}")

# Creamos los gráficos de la comparación de datos crudos a limpios
sns.set_theme(style="whitegrid")
fig, axs = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Comparativa de Datos: Antes y Después del Preprocesamiento', fontsize=16, fontweight='bold')

# Gráfico de datos crudos
sns.boxplot(data=df_raw[variables_tda], ax=axs[0])
axs[0].set_title('Datos Originales')
axs[0].set_ylabel('Valor 0-99')
axs[0].tick_params(axis='x', rotation=45)

# Gráfico de datos limpios
sns.boxplot(data=df_tda[variables_tda], ax=axs[1])
axs[1].set_title('Datos Preprocesados para TDA de 0-1')
axs[1].set_ylabel('Valor Normalizado 0.0-1.1')
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('Comparativa_Preprocesamiento.png', dpi=300)

# Guardamos el csv limpio
df_tda.to_csv('anes_para_tda.csv', index=False)
print("CSV limpia guardada como 'anes_para_tda.csv'")
print("Preprocesamiento finalizado")
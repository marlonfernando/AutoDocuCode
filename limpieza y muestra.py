import pandas as pd

# Load all the files to inspect the content and the structure
file_paths = [
    '/mnt/data/python_train_13_part_1.xlsx',
    '/mnt/data/python_train_13_part_2.xlsx',
    '/mnt/data/python_train_13_part_3.xlsx',
    '/mnt/data/python_train_13_part_4.xlsx',
    '/mnt/data/python_train_13_part_5.xlsx',
    '/mnt/data/python_train_13_part_6.xlsx',
    '/mnt/data/python_train_13_part_7.xlsx',
    '/mnt/data/python_train_13_part_8.xlsx',
    '/mnt/data/python_train_13_part_9.xlsx',
    '/mnt/data/python_train_13_part_10.xlsx',
    '/mnt/data/python_train_13_part_11.xlsx',
    '/mnt/data/python_train_13_part_12.xlsx',
    '/mnt/data/python_train_13_part_13.xlsx',
    '/mnt/data/python_train_13_part_14.xlsx',
    '/mnt/data/python_train_13_part_15.xlsx',
    '/mnt/data/python_train_13_part_16.xlsx',
    '/mnt/data/python_train_13_part_17.xlsx'
]

# Initialize a list to store the dataframes
dfs = []

# Load each file and append to the list
for path in file_paths:
    df = pd.read_excel(path)
    dfs.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Display the first few rows and summary of the combined dataframe
combined_df_info = combined_df.info()
combined_df_sample = combined_df.head()

combined_df_info, combined_df_sample

from math import ceil
from statsmodels.stats.proportion import proportion_confint

# Parameters
population_size = 22178  # Total population size
confidence_level = 0.95  # 95% confidence level
margin_of_error = 0.05  # 5% margin of error
std_dev = 0.5  # Standard deviation for proportion, most conservative estimate

# Calculate the sample size
sample_size = ceil((1.96**2 * std_dev * (1 - std_dev)) / (margin_of_error**2))

# Adjust sample size for finite population
adjusted_sample_size = ceil(sample_size / (1 + ((sample_size - 1) / population_size)))

adjusted_sample_size

# Filtrar los fragmentos que tienen documentación en el formato estándar en la columna 'docstring'
# Un ejemplo de formato estándar podría ser presencia de ciertas palabras clave como '@param', '@return', etc.

# Definir un patrón básico que podría identificar una docstring con formato estándar
pattern = r'@param|@return|@throws|@see|:param|:return|Args:|Returns:|Raises:'

# Filtrar las filas que contienen este patrón en la columna 'docstring'
filtered_df = combined_df_full[combined_df_full['docstring'].str.contains(pattern, case=False, na=False)]

# Obtener el número de fragmentos después de filtrar
filtered_count = filtered_df.shape[0]
filtered_count

# Extraer una muestra aleatoria de 366 fragmentos del dataframe filtrado
sample_df = filtered_df.sample(n=366, random_state=42)

# Guardar la muestra en un archivo Excel
sample_df.to_excel('/mnt/data/muestra_filtrada_366.xlsx', index=False)

sample_df.head()


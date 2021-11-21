# author Frederik

# Namespaces
import pandas as pd
from matplotlib import pyplot as plt

# Importere data
df = pd.read_csv('StudentsPerformance.csv')
df = df.rename(columns={'test preparation course': 'testprep', 'parental level of education': 'p_edu'})
print(df.head())

# Exportere data
df.to_csv('StudentsPerformanceCleaned.csv')
# author Frederik

import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')
df = df.rename(columns={'test preparation course': 'testprep'})
print(df.head())

df.to_csv('StudentsPerformanceCleaned.csv')
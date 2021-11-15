# author Frederik

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('StudentsPerformance.csv')

sns.kdeplot(df[df.gender == 'female']['math score'], shade=True, label='female')
sns.kdeplot(df[df.gender == 'male']['math score'], shade=True, label='male')
sns.color_palette('pastel')

plt.title('Math Score - Male vs. Female')
plt.xlabel('Math Score')
plt.ylabel('Probability Density')
plt.legend()
plt.show()
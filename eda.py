# author Frederik

# Namespaces
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import scipy.stats as ss

# Plotte indstillinger
plt.rc("font", family=["Helvetica", "Arial"]) # skifter skrifttype
plt.rc("axes", labelsize=16)   # skriftstørrelse af `xlabel` og `ylabel`
plt.rc("xtick", labelsize=16, top=True, direction="in")  # skriftstørrelse af ticks og viser ticks øverst
plt.rc("ytick", labelsize=16, right=True, direction="in")
plt.rc("axes", titlesize=16)
plt.rc("legend", fontsize=16)

# Importere data
df = pd.read_csv('StudentsPerformanceCleaned.csv')
print(df.head())

# Definere funktioner
def calc_pop_mean(data=[], size=100, count=1000): # bootstrap
    means = []
    for i in range(count):
        means.append(np.random.choice(data, size=size, replace=True))
    return np.mean(means)

# Subplots
labels = ['reading score','math score','writing score']
fig, ax = plt.subplots(3, 1, figsize=(8,14))

# Plotte kde-plots
for i, l in enumerate(labels):
    sns.kdeplot(df[df.testprep == 'none'][l], shade=True, label='none', ax=ax[i])
    sns.kdeplot(df[df.testprep == 'completed'][l], shade=True, label='completed', ax=ax[i])
    ax[i].set_xlabel(l)
    ax[i].set_ylabel('Probability Density')
    ax[i].legend()

# Indstillinger for plot
ax[0].set_title('Testpreperation proportions')
plt.subplots_adjust(wspace=2)
plt.tight_layout()
sns.color_palette('pastel')
plt.show()

# One-Sample T-Tests
read_none = df[df.testprep == 'none']['reading score']
read_pop_mean = calc_pop_mean(read_none, size=1000, count=1000)
tstat, pval_r = ss.ttest_1samp(df['reading score'], read_pop_mean)

math_none = df[df.testprep == 'none']['math score']
math_pop_mean = calc_pop_mean(read_none, size=1000, count=1000)
tstat, pval_m = ss.ttest_1samp(df['math score'], math_pop_mean)

write_none = df[df.testprep == 'none']['writing score']
write_pop_mean = calc_pop_mean(write_none, size=1000, count=1000)
tstat, pval_w = ss.ttest_1samp(df['writing score'], write_pop_mean)

# Printing results from One-Sample T-Tests
sig_level = 0.05
print('-------------------------------------')
print('Reading Score: Forskel er ' + ('signifikant' if pval_r < sig_level else 'ikke signifikant'))
print('-------------------------------------')
print('Math Score: Forskel er ' + ('signifikant' if pval_m < sig_level else 'ikke signifikant'))
print('-------------------------------------')
print('Writing Score: Forskel er ' + ('signifikant' if pval_w < sig_level else 'ikke signifikant'))
print('-------------------------------------')
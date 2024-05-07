
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# pH vs Potability
df = pd.read_csv('water_potability.csv')


bars = [0, 2, 4, 6, 8, 10, 12, 14]
labels = ['1-2', '3-4', '5-6', '7-8', '9-10', '11-12', '13-14']

potable = df[df['Potability'] == 1]

potable['Levels'] = pd.cut(potable['ph'], bins=bars,
                           labels=labels, include_lowest=True)
count = potable['Levels'].value_counts().reindex(labels, fill_value=0)

fig = plt.figure(figsize=(10, 8))
count.plot(kind='bar', color='lightblue')
plt.xlabel('pH Levels')
plt.ylabel('Counts of Potable Water')
plt.savefig('pictures/ph_bargraph.png')
plt.close(fig)

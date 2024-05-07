import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('water_potability.csv')

potable = df[df['Potability'] == 1]
not_potable = df[df['Potability'] == 0]

columns = df.columns[:-1]
potability = df.columns[-1]


for i in range(len(df.columns) - 1):

    fig = plt.figure()

    plt.scatter(potable[potability], potable[columns[i]], color='blue')
    plt.scatter(not_potable[potability], not_potable[columns[i]], color='red')
    plt.xlabel('Potability')
    plt.ylabel(columns[i])
    plt.xticks([0, 1])
    plt.savefig(f'pictures/{columns[i]}Potability.png')
    plt.close(fig)

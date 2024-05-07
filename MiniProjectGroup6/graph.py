
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# pH vs Potability
df = pd.read_csv('phVsPotability.txt')

plt.figure(figsize=(10, 6))

potable = df[df['Potability'] == 1]
not_potable = df[df['Potability'] == 0]

plt.scatter(potable['Potability'], potable['ph'],
            color='blue', label='Drinkable')

plt.scatter(not_potable['Potability'], not_potable['ph'],
            color='red', label='Drinkable')

plt.xlabel('Potability')
plt.ylabel('pH Levels')
plt.title('pH Levels and Potability')

plt.savefig('phPotability.png')

# Solids vs Conductivity
df2 = pd.read_csv('solidVsConductivity.txt')

plt.figure(figsize=(10, 6))


solids = df2['Solids']
conductivity = df2['Conductivity']

plt.scatter(solids, conductivity,)

plt.xlabel('Solids')
plt.ylabel('Conductivity')
plt.title('Solids vs Conductivity')

plt.savefig('solidsConductivity.png')

# Solids vs Turbidity
df3 = pd.read_csv('solidVsTurbidity.txt')

plt.figure(figsize=(10, 6))

turbidity = df3['Turbidity']

plt.scatter(solids, turbidity)

plt.xlabel('Solids')
plt.ylabel('Turbidity')
plt.title('Solids vs Turbidity')
plt.savefig('solidsTurbidity.png')

plt.show()

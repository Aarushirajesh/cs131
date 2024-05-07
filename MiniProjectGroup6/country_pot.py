import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('NonPotabilityRatio/NonPotabilityRatio.txt',
                 header=None, names=['Country', 'Non Pot'])

df_first = df[df['Non Pot'] <= 0.5]
df_second = df[(df['Non Pot'] >= 0.6)]

plt.figure(figsize=(15, 8))  # Increase figure size
plt.scatter(df_first['Country'], df_first['Non Pot'],
            color='green')

plt.xticks(rotation=90)

plt.yticks([0, 0.3, 0.5, 0.7, 1])
plt.xlabel('Country')
plt.ylabel('Non-Potable Ratio')
plt.title('Scatter Plot of Country vs. Non-potable Ratio by City Count')

plt.tight_layout()

plt.savefig('pictures/NonPotabilityRatio_0-0.5.png')
plt.close()


plt.figure(figsize=(15, 8))

plt.scatter(df_second['Country'], df_second['Non Pot'],
            color='pink')
plt.xticks(rotation=90)
plt.yticks([0, 0.3, 0.5, 0.7, 1])
plt.xlabel('Country')
plt.ylabel('Non-Potable Ratio')
plt.title('Scatter Plot of Country vs. Non-potable Ratio by City Count')

plt.tight_layout()

plt.savefig('pictures/NonPotabilityRatio_0.5-1.png')
plt.close()

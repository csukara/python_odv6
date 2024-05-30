import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


num_points = 1000
x_koordinat = np.random.randint(0, 1000, size=num_points)
y_koordinat = np.random.randint(0, 1000, size=num_points)


data = pd.DataFrame({'X': x_koordinat, 'Y': y_koordinat})

data.to_excel('koordinatlar.xlsx', index=False)

data = pd.read_excel('koordinatlar.xlsx')

x_koordinat = data['X']
y_koordinat = data['Y']


izgara_boyutu = 50
colors = list(mcolors.TABLEAU_COLORS.values())


plt.figure(figsize=(10, 10))


for i in range(0, 1000, izgara_boyutu):
    for j in range(0, 1000, izgara_boyutu):
        x_mask = (x_koordinat >= i) & (x_koordinat < i + izgara_boyutu)
        y_mask = (y_koordinat >= j) & (y_koordinat < j + izgara_boyutu)
        mask = x_mask & y_mask
        color = colors[(i // izgara_boyutu + j // izgara_boyutu) % len(colors)]
        plt.scatter(x_koordinat[mask], y_koordinat[mask], s=10, color=color)


plt.xlabel('X koordinat')
plt.ylabel('Y koordinat')
plt.grid(True)
plt.show()

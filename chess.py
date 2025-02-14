# Задача:
# Создайте шахматную доску размером 8×8, где чёрные клетки обозначены числом 1, а белые — 0.
# Укажите координаты клетки, где находится ферзь, например, [4,4].
# Определите клетки, которые атакует ферзь (в строке, столбце и диагоналях).
# Визуализация: Используйте тепловую карту (imshow), чтобы показать шахматную доску. Отметьте положение ферзя и атакуемые клетки цветами.
import matplotlib.pyplot as plt
import numpy as np
data = np.array([[1,0,1,0,1,0,1,0],
                 [0,1,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,0],
                 [0,1,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,0],
                 [0,1,0,1,0,1,0,1],
                 [1,0,1,0,1,0,1,0],
                 [0,1,0,1,0,1,0,1]] )
n = np.array([0,1,2,3,4,5,6,7])
x = int(input()) - 1
y = 8 - int(input())
fig, ax = plt.subplots()
print(x,y)
plt.xticks(n, labels=[f"{i}" for i in ['A','B','C','D','E','F','G','H']])
plt.yticks(n, labels=[f"{i}" for i in range(8,0, -1)])
circle = plt.Circle((x, y), 0.4, color= "red")
ax.add_patch(circle)
ax.plot([0,7], [y,y], color='red')
ax.plot( [x,x],[0,7], color='red')
plt.plot([0, 7], [y - x, y + 7 - x], color='red')
plt.plot([0, 7], [y + x, y + x - 7], color='red')
plt.imshow(data, cmap='binary')
plt.show()
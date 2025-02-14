# Описание задачи:
# Робот начинает своё движение из точки (0,0) на координатной плоскости. Его маршрут задаётся массивом из 100 случайных значений, где:1 — движение вверх.2 — движение вниз.3 — движение вправо.4 — движение влево.
# Ваша задача:
# Сымитировать маршрут робота, используя случайные числа.
# Найти конечное положение робота.
# Построить путь робота на графике (соединяя все пройденные точки).
# Подсчитать, сколько шагов робот сделал в каждую сторону.
# Определить расстояние от начальной точки до конечной.
import matplotlib.pyplot as plt
import numpy as np
data = np.random.randint(1, 5, 100)
x = np.zeros(100)
y = np.zeros(100)
Up = 0
Down = 0
Right = 0
Left = 0
fig,ax = plt.subplots()
for i in range(99):
    if data[i] == 1:
        x[i + 1] = x[i]
        y[i + 1] = y[i] + 1
        Up += 1
    elif data[i] == 2:
        x[i + 1] = x[i]
        y[i + 1] = y[i] - 1
        Down += 1
    elif data[i] == 3:
        x[i + 1] = x[i] + 1
        y[i + 1] = y[i]
        Right += 1
    elif data[i] == 4:
        x[i + 1] = x[i] - 1
        y[i + 1] = y[i]
        Left += 1
ax.plot(x, y, color='green')
plt.grid(True)
plt.subplots_adjust(left=0.1, bottom=0.35)
stats = (f"Шагов влево {Left}  "
              f"Шагов вправо {Right}\n"
f"Шагов вниз {Down}   "
f"Шагов вверх {Up} \n"
f"Конечная позиция - {int(x[99]),int(y[99])} Расстояние от стартовой позиции - {round((x[99]**2 + y[99]**2)**0.5),2}")
stats_ax = fig.add_axes([0.1, 0.1, 0.6, 0.1])
stats_ax.axis('off')
stats_box = stats_ax.text(0, 1, stats,
                fontsize=10, verticalalignment='top')

ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
plt.title('Маршрут робота')
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.show()
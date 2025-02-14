# Задача:
# Создайте массив из 365 случайных чисел, представляющих дневную температуру (например, от −10 до 35).
# Найдите:
# Среднюю температуру за год.
# Количество дней с температурой выше 25.
# Самую длинную последовательность дней, когда температура была ниже 0.
# Визуализируйте:
# Линейный график температуры по дням.
# Гистограмму распределения температуры.
# Подсветку "холодных" и "жарких" дней на линейном графике.
import matplotlib.pyplot as plt
import numpy as np
nums = np.linspace(1, 365, 365)
days = np.random.randint(-10, 36, 365)
print(f'Средняя температура за год: {round(days.mean(),1)}')

days25 = days[days>25]
print(f'Количество дней с температурой выше 25: {len(days25)}')

kmas = np.array([])
k = 1
for i in range(364):
    if days[i] < 0 and days[i+1] < 0:
        k += 1
    else:
        kmas = np.append(kmas, k)
        k = 1
kmas = np.append(kmas, k)

print(f'Самая длинная последовательность дней, когда температура была ниже 0: {kmas.max()}')
temp = np.linspace(-10, 35, 46)
tnum = np.unique(days, return_counts=True)

fig, axs = plt.subplots(2, 1, figsize=(20, 6))

axs[0].plot(nums, days, color='green')
plt.grid(True)
axs[0].set_xlim(0, 366)
axs[0].set_ylim(-15, 40)
axs[0].set_title("График температуры по дням")
axs[0].set_xlabel("Дни")
axs[0].set_ylabel("Температура")

for i in range(365):
    if days[i] <= 0:
        circle = plt.Circle((i+1, days[i]), 0.8, color="blue")
        axs[0].add_patch(circle)
    else:
        circle = plt.Circle((i+1, days[i]), 0.8, color="red")
        axs[0].add_patch(circle)

bar_data = axs[1].bar(temp, tnum[1])
axs[1].bar_label(bar_data)
axs[1].set_title("Распределение температуры")
axs[1].set_xlabel("Температура")
axs[1].set_ylabel("Кол-во дней")
plt.tight_layout()
plt.show()


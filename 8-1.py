import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap
import matplotlib.ticker as ticker
with open("settings.txt", 'r') as settings:
    tmp = [float(i) for i in settings.read().split('\n')]

arr = np.loadtxt("data.txt", dtype=float)
arr *= (3.3/255)  #перевод в вольты показаний
arr_time=np.array([i*tmp[0] for i in range(arr.size)])

fig, ax = plt.subplots(figsize=(10,8), dpi=400)
ax.axis([arr.min(), arr_time.max()+1, arr.min(), arr.max()+0.2])
#ax.plot(arr)
ax.set_title('процесс заряда и разряда конденсатора в RC цепи', fontsize=12, color='red', loc = 'center')

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.xaxis.set_minor_formatter(ticker.FuncFormatter(lambda arr_time, _: f'{arr_time:.2f}'))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax.yaxis.set_minor_formatter(ticker.FuncFormatter(lambda arr_time, _: f'{arr_time:.2f}'))

ax.tick_params(axis='both',which='major',labelsize=5)
ax.tick_params(axis='both',which='minor',labelsize=2)

ax.set_ylabel("напряжение, В", fontsize=9)
ax.set_xlabel("время, 10^(-2) с", fontsize=9)

ax.grid(which='major', color = 'black', linestyle = '-')
ax.minorticks_on()
ax.grid(which='minor', color = 'gray', linestyle = '-')

ax.plot(arr_time, arr, c='green', linewidth=0.5, label = 'V(t)')
ax.scatter(arr_time[0:arr.size:20], arr[0:arr.size:20], marker = '.', c = 'blue', s=5)

ax.legend(shadow = False, loc = 'right', fontsize = 5)

fig.savefig("test.png")
fig.savefig("test.svg")
plt.show()
print(arr)  

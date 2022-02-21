from cv2 import log
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b):
    return a * np.exp(-b * x) + 5.69

times = np.array([5, 60, 300, 1200])
times = [5, 60, 300, 1200]
log_times = np.log(times)
xdata = log_times
ydata = np.array([19.42, 9.29, 6.61, 5.69])

plt.scatter(xdata, ydata, color = 'r')

popt, pcov = curve_fit(func, xdata, ydata)

plt.plot(xdata, func(xdata, *popt), 'r', label='Power Curve: a=%5.3f, b=%5.3f' % tuple(popt))

plt.axhline(y = 5.69, color = 'b', linestyle = '--', label = 'Critical Power: 5.69')

plt.xlabel('$Log_{10}$ of Time (seconds)')
plt.ylabel('Power (W)')
plt.title(label = "Women's Word Champion Sprinter")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b):
    return a * np.exp(-b * x) + 6.40

#a = 45, b = 0.5

times = [5, 60, 300, 1200]
log_times = np.log(times)
xdata = log_times
ydata = np.array([24.04, 11.05, 7.60, 6.40])

plt.scatter(xdata, ydata, color = 'r')

popt, pcov = curve_fit(func, xdata, ydata)

plt.plot(xdata, func(xdata, *popt), 'r', label='Power Curve: a=%5.3f, b=%5.3f' % tuple(popt))

plt.axhline(y = 6.40, color = 'b', linestyle = '--', label = 'Critical Power: 6.40')

plt.xlabel('$Log_{10}$ of Time (seconds)')
plt.ylabel('Power (W/kg)')
plt.title(label = "Men's Word Champion Sprinter")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b):
    return a * np.exp(-b * x) + CP

#a = 45, b = 0.5

times = [5, 60, 300, 3600]
log_times = np.log(times)
xdata = log_times

# World class
# ydata = np.array([19.42, 9.29, 6.61, 5.69])
# CP = 5.69

# Average
ydata = np.array([12.95, 6.57, 3.83, 3.23])
CP = 3.23

plt.scatter(xdata, ydata, color = 'r')

popt, pcov = curve_fit(func, xdata, ydata)

plt.plot(xdata, func(xdata, *popt), 'r', label='Power Curve: a=%5.3f, b=%5.3f' % tuple(popt))

plt.axhline(y = CP, color = 'b', linestyle = '--', label = f'Critical Power: {CP}')
plt.gca().set_ylim([0, 30])
plt.xlabel('$Log_{10}$ of Time (seconds)')
plt.ylabel('Power (W/kg)')

# World class title
# plt.title(label = "Women's Word Champion Sprinter")

# Avergae title
plt.title(label = "Women's Average Sprinter")
plt.legend()
plt.show()
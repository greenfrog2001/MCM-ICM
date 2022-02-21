import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def func(x, a, b):
    return a * np.exp(-b * x) + CP

#a = 45, b = 0.5

times = [5, 60, 300, 3600]
log_times = np.log(times)
xdata = log_times

# # World class
ydata = np.array([24.04, 11.05, 7.60, 6.40])
CP = 6.40

# Average
# ydata = np.array([15.88, 8.05, 4.50, 3.73])
# CP = 3.73

plt.scatter(xdata, ydata, color = 'r')

popt, pcov = curve_fit(func, xdata, ydata)

plt.plot(xdata, func(xdata, *popt), 'r', label='Power Curve: a=%5.3f, b=%5.3f' % tuple(popt))

plt.axhline(y = CP, color = 'b', linestyle = '--', label = f'Critical Power: {CP}')
plt.gca().set_ylim([0, 30])
plt.xlabel('$Log_{10}$ of Time (seconds)')
plt.ylabel('Power (W/kg)')

# World class title
plt.title(label = "Men's Word Champion Sprinter")

# Avergae title
# plt.title(label = "Men's Average Sprinter")
plt.legend()
plt.show()
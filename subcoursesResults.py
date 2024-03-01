# Tokyo
# power_list = [375.89889495126266, 851.4900231155128, 471.56306119915496, 462.23352469193225, 478.9535843037134, 460.24263226703647, 429.2465010633033, 418.4803896976139, 420.53069203014473, 421.7569504795852]
# time_list = [10.0273024081356, 19.426977278364127, 27.14519875522955, 38.18231529658415, 41.97744430825304, 51.38297385089412, 62.59974188331201, 75.63626251556853, 89.10658508077019, 93.45890545703723]

# Own Design
power_list = [385.7478500759531, 652.2223360099846, 556.5041179350184, 439.38378918959774, 470.19575116020314, 433.92479395347783, 413.0450244718594, 257.2338188145037, 398.33173198236943, 349.9406880706131, 380.14233541248655, 373.9579949276393]
time_list = [11.76770011870405, 18.157826686200636, 37.86294365616367, 48.40242215683415, 71.81009364750662, 103.01193918924325, 118.61245636599344, 140.8844060178255, 145.5931665782988, 154.06469549437006, 165.58155151651818, 176.79386619265057]

from cProfile import label
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

plt.scatter(time_list, power_list, color = 'r')
plt.plot(time_list, power_list, color = 'r', label = 'Power usage')
for i in range(len(power_list)):
    plt.hlines(y=power_list[i], xmin=time_list[i]-5, xmax=time_list[i]+5, color='r')

CP = 351
plt.axhline(y = CP, color = 'b', linestyle = '--', label = f'Critical Power: {CP}')

# popt, pcov = curve_fit(func, xdata, ydata)

# plt.plot(xdata, func(xdata, *popt), 'r', label='Power Curve: a=%5.3f, b=%5.3f' % tuple(popt))

# plt.axhline(y = CP, color = 'b', linestyle = '--', label = f'Critical Power: {CP}')
# plt.gca().set_ylim([0, 30])
plt.xlabel('Time (seconds)')
plt.ylabel('Power (W)')

# World class title
plt.title(label = "Word Champion's Power Usage")

# Avergae title
# plt.title(label = "Men's Average Sprinter")

# Clear xticks
plt.gca().axes.get_xaxis().set_ticks([])

plt.legend()
plt.show()
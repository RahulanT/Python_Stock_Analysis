from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
import numpy as np

# Generate random data.
data_x = np.arange(start = 0, stop = 25, step = 1, dtype='int')
data_y = np.random.random(25)*6
 
# Find peaks(max).
peak_indexes = argrelextrema(data_y, np.greater)
peak_indexes = peak_indexes[0]



# Find valleys(min).
valley_indexes = argrelextrema(data_y, np.less)
valley_indexes = valley_indexes[0]
 
# Plot main graph.
(fig, ax) = plt.subplots()
ax.plot(data_x, data_y)
 
# Plot peaks.
peak_x = peak_indexes
peak_y = data_y[peak_indexes]
ax.plot(peak_x, peak_y, marker='o', linestyle='dashed', color='green', label="Peaks")


plt.show()
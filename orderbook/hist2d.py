import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
"""https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist2d.html
https://stackoverflow.com/questions/59186769/how-to-plot-time-series-heatmap-with-python"""

# example data
x = np.linspace(0, 10, 10000)
y = 0.5*x+np.random.randn(10000)

# make a custom colormap with transparency
ncolors = 256
color_array = plt.get_cmap('YlOrRd')(range(ncolors))
color_array[:, -1] = np.linspace(0, 1, ncolors)
cmap = LinearSegmentedColormap.from_list(name='YlOrRd_alpha', colors=color_array)

plt.hist2d(x, y, bins=[15, 30], cmap=cmap, edgecolor='white')
plt.show()
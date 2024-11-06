# Libraries
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import integrate
from scipy.optimize import curve_fit
from matplotlib import colors as mcolors

# Plot parameters
plt.rcParams.update({
    'lines.linewidth': 2,     # linewidth
    'text.usetex': True,      # LaTeX font
    'font.family': 'serif',   # Serif family
    'font.size': 16,          # font size
    'axes.titlesize': 18,     # title size
    'axes.grid': True,        # grid
    'grid.linestyle': "-.",   # grid style
})

# We open all the files
data = [ pd.read_csv(f'm{i}.csv', header = None) for i in range(1, 24) ]
# We concatenate all the files
concatenated_data = pd.concat(data, ignore_index = True)

# Histogram 
bins = np.linspace(0, 0.8, 200)
figure = concatenated_data.set_index(3)[4].hist(bins = bins, figsize = (20, 4))
plt.savefig('histogram.pdf', dpi = 300)

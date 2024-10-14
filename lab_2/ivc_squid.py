# UNDER CONSTRUCTION
# Measurement of the Current-Voltage Characteristic (IVC) of the Superconducting Quantum Interference Device (SQUID)

# Libraries
import numpy as np
from pandas import pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

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


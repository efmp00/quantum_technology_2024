# Libraries
import numpy as np
from pandas import *
import matplotlib.pyplot as plt
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

# === Files ===
data = read_csv('240626_Nice2968_dark_2024-09-10--05-00-47_no_laser.txt', sep = '\t')

# Parameters
BC = data["BC"]  # Bias Current
V4 = data["BV4"] # Voltage
V5 = data["BV5"] # Voltage
V8 = data["BV8"] # Voltage

# Counts normalized
V4_normalized = V4
V5_normalized = V5 
V8_normalized = V8 

# Plot
# plt.figure(figsize = (10, 4.5))
plt.plot(BC, V4, 'r-', label = r'Detector 4')
plt.plot(BC, V5, 'b-', label = r'Detector 5')
plt.plot(BC, V8, 'g-', label = r'Detector 8')
plt.plot(22.25 * np.ones(len(BC)), V8, 'r--', label = r'$22.25 \: \mu \mathrm{A}$')
plt.plot(32.25 * np.ones(len(BC)), V8, 'b--', label = r'$32.25 \: \mu \mathrm{A}$')
plt.plot(25.25 * np.ones(len(BC)), V8, 'g--', label = r'$25.25 \: \mu \mathrm{A}$')

plt.title(r'Bias current vs Voltage (no photon)')
plt.xlabel(r'Bias current ($\mu \mathrm{A}$)')
plt.ylabel(r'Voltage ($\mathrm{V}$)')
plt.legend(loc = 'upper left', borderpad = 0.2)
plt.tight_layout()
plt.savefig('voltage_no_photon.pdf')
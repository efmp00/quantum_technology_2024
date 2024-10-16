# Libraries
import os
import numpy as np
import matplotlib.pyplot as plt
#
from pandas import *
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

# Files
data_ivc = read_csv('SDS00004.csv')

# Physical parameters
Rb = 10           # resistence              (Ω)
f_ext = 44e9      # frequency             (GHz)
V1_gain = 1e4     # voltage gain            (V)
V2_gain = 1e3     # voltage gain            (V)
Phi_0 = 2.07e-15  # flux quantum  (Wb or V • s)

# Parameters
t = data_ivc["TIME"] 
V_ch1, V_ch2 = data_ivc["CH1"], data_ivc["CH2"] # voltages (V)

# Current and voltage
I = V_ch2 / (V2_gain * Rb)
V = V_ch1 / V1_gain

# Plot
plt.title(r'IVC of a SQUID irradiated at $44 \: \mathrm{GHz}$')
plt.plot(1e6 * V, 1e6 * I, color = 'blue', markersize = 1)
plt.xlabel(r'Voltage ($\mu \mathrm{V}$)')
plt.ylabel(r'Current ($\mu \mathrm{A}$)')

# Shapiro steps
steps = np.arange(-3, 4) * Phi_0 * f_ext
plt.vlines(1e6 * steps, 1e6 * min(V), 1e6 * max(V), linestyles = "dashed", linewidth = 2,
           color = 'tomato', label = r'$\overline{V}_{n} = n \Phi_{0} f_{\mathrm{ext}}$')

plt.tight_layout()
plt.legend(loc = 'upper left', borderpad = 0.2)
plt.savefig('third_experiment.pdf')

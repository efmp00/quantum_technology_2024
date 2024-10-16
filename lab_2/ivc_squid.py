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
data_ivc = read_csv('SDS00002.csv')

# Physical parameters
Rb = 10           # resistence    (Ω)
V1_gain = 1e4     # voltage gain  (V)
V2_gain = 1e3     # voltage gain  (V)

# Files
data_ivc = read_csv('SDS00002.csv')

# Parameters
t = data_ivc["TIME"] 
V_ch1, V_ch2 = data_ivc["CH1"], data_ivc["CH2"] # voltages (V)

# Parameters
Rb = 10 # Ohms Ω
V1_gain = 1e4
V2_gain = 1e3

# Current
I = V_ch2 / (V2_gain * Rb)
V = V_ch1 / V1_gain

"""
Theory model for the voltage. Here, we exclude all the elements where the normalized 
current is less than 1, which would lead to undesired complex values.
"""
def V_model(I, I_c, R):
    i = I/I_c
    result = np.where(abs(i) > 1, np.sign(i) * R * I_c * np.sqrt(i ** 2 - 1), 0)
    return result

"""
Curve fitting
"""
# Initial guess for the parameters (Ic, R)
initial_guess = [1e-6, 10]

# Perform the curve fit
popt, pcov = curve_fit(V_model, I, V, p0=initial_guess)

# Extract the fitted parameters
Ic_fitted, R_fitted = popt
print(f"Fitted Ic: {Ic_fitted} A")
print(f"Fitted R: {R_fitted} Ohms")

# Plot
plt.figure(figsize = (16, 5.5))

# Signal vs time
plt.subplot(1, 2, 1)
plt.title(r'Signals vs time')
plt.plot(1e3 * t, V_ch1, color = 'deepskyblue', markersize = 1, label = r'$V$ monitor')
plt.plot(1e3 * t, V_ch2, color = 'darkorange', markersize = 1, label = r'$I$ monitor')
plt.xlabel(r'Time ($\mu \mathrm{s}$)')
plt.ylabel(r'Voltage ($\mathrm{V}$)')
plt.legend(loc = 'upper left', borderpad = 0.2)

# Plot the data and the fitted curve
plt.subplot(1, 2, 2)
plt.title(r"SQUID IVC")
plt.scatter(1e6 * V, 1e6 * I, label = 'Data', color = 'dodgerblue', s = 1)
plt.plot(1e6 * V_model(I, *popt), 1e6 * I, color = 'darkorange', label = 'Fit')
plt.xlabel(r"Voltage ($\mu \mathrm{V}$)")
plt.ylabel(r"Current ($\mu \mathrm{A})$")
plt.legend(loc = 'upper left', borderpad = 0.2)
#
plt.tight_layout()
plt.gcf()
plt.savefig('first_experiment.pdf')

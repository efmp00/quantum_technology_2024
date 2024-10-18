# Libraries
import os
import numpy as np
import matplotlib.pyplot as plt
#
from pandas import *
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

# Files
data_ivc = read_csv('SDS00003.csv')

# Physical parameters
Rb = 10           # resistence              (Ω)
f_ext = 44e9      # frequency             (GHz)
V1_gain = 1e4     # voltage gain            (V)
V2_gain = 1e3     # voltage gain            (V)
Phi_0 = 2.07e-15  # flux quantum  (Wb or V • s)

# Parameters
t = data_ivc["TIME"] 
V_ch1, V_ch2 = data_ivc["CH1"], data_ivc["CH2"] # voltages (V)

# Current
I = V_ch2 / (V2_gain * Rb)
V = V_ch1 / V1_gain

# == Signals vs time ===
# Parameters
t = data_ivc["TIME"] 
V_ch1, V_ch2 = data_ivc["CH1"], data_ivc["CH2"] # voltages (V)

plt.title(r'Signals vs. time')
plt.plot(1e3 * t, 10 * V_ch1, color = '#2166AB', markersize = 1, label = r'$V$ monitor $\times 10$')
plt.plot(1e3 * t, V_ch2, color = '#E31A1C', markersize = 1, label = r'$I$ monitor')
plt.xlabel(r"Time ($\mathrm{ms}$)")
plt.ylabel(r"SQUID Voltage ($\mathrm{\mu V})$")
plt.legend(loc = 'upper left', borderpad = 0.2)
#
plt.tight_layout()
plt.savefig('second_experiment_1.pdf')
plt.close()

# === Cosine fit ===
# Cosine function for the fit
def cosine_func(I, amplitude, frequency, phase, offset):
    return offset + amplitude * np.cos(frequency * I + phase)

# Current and voltage extremums
I_cos = I[I.argmin() : I.argmax()] 
V_cos = V[I.argmin() : I.argmax()]

# Initial guesses
initial_guesses = np.array([-3e-6, 6e4, 0, -3e-6])

# Curve fit
p_opt, p_conv = curve_fit(cosine_func, I_cos, V_cos, initial_guesses)
p_err = np.sqrt(np.diag(p_conv)) # standard error

# Cosine function with fitted values
cosine_fit = cosine_func(I_cos, p_opt[0], p_opt[1], p_opt[2], p_opt[3])

# Mutual inductance
mutual_inductance = p_opt[1] / (2 * np.pi)
mutual_inductance_error = 2.67 * p_err[1] * (Phi_0 / (2 * np.pi))

# Magnetic flux
flux = mutual_inductance * I_cos

# Data 
print("Fit parameters:", p_opt)
print("Errors in parameters:", p_err)
print("Mutual inductance:", mutual_inductance * Phi_0)
print("Mutual inductance error:", mutual_inductance_error)

# Plot
plt.plot(1e6 * I_cos, 1e6 * V_cos, '.', markersize = 1, color = '#2166AB', label = 'Data')
plt.plot(1e6 * I_cos, 1e6 * cosine_fit, color = '#4DB04A', label = 'Fit')
plt.xlabel(r"$\Phi / \Phi_{0}$")
plt.ylabel(r"SQUID Voltage ($\mathrm{\mu V}$)")
plt.tight_layout()
plt.legend(loc = 'lower left', borderpad = 0.2)
plt.savefig('second_experiment_22.pdf', dpi = 300)

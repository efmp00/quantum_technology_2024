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
    'font.size': 20,          # font size
    'axes.titlesize': 24,     # title size
    'axes.grid': True,        # grid
    'grid.linestyle': "-.",   # grid style
})

# === No photon ===
# 1) 240626_Nice2968_dark_2024-09-10--05-00-47_no_laser.txt
data_no_photon = read_csv('240626_Nice2968_dark_2024-09-10--05-00-47_no_laser.txt', sep = '\t')

# Parameters
BC_no_photon = data_no_photon["BC"]  # Bias Current
C4_no_photon = data_no_photon["C4"]  # Detector 4 counts
C5_no_photon = data_no_photon["C5"]  # Detector 5 counts
C8_no_photon = data_no_photon["C8"]  # Detector 8 counts

# Counts normalized
C4_no_photon_normalized = C4_no_photon / C4_no_photon.max()
C5_no_photon_normalized = C5_no_photon / C5_no_photon.max()
C8_no_photon_normalized = C8_no_photon / C8_no_photon.max()

# === 850 nm ===
# 3) 240626_Nice2968_dark_2024-09-10--05-13-51_850nm.txt
data_850nm = read_csv('240626_Nice2968_dark_2024-09-10--05-13-51_850nm.txt', sep = '\t')

# Parameters
BC_850nm = data_850nm["BC"]  # Bias Current
C4_850nm = data_850nm["C4"]  # Detector 4 counts
C5_850nm = data_850nm["C5"]  # Detector 5 counts
C8_850nm = data_850nm["C8"]  # Detector 8 counts

# Counts normalized
C4_850nm_normalized = C4_850nm / C4_850nm.max()
C5_850nm_normalized = C5_850nm / C5_850nm.max()
C8_850nm_normalized = C8_850nm / C8_850nm.max()

# === 1550 nm ===
# 5) 240626_Nice2968_dark_2024-09-10--05-35-48_1550nm
data_1550nm = read_csv('240626_Nice2968_dark_2024-09-10--05-00-47_no_laser.txt', sep = '\t')

# Parameters
BC_1550nm = data_1550nm["BC"]  # Bias Current
C4_1550nm = data_1550nm["C4"]  # Detector 4 counts
C5_1550nm = data_1550nm["C5"]  # Detector 5 counts
C8_1550nm = data_1550nm["C8"]  # Detector 8 counts

# Counts normalized
C4_1550nm_normalized = C4_1550nm / C4_1550nm.max()
C5_1550nm_normalized = C5_1550nm / C5_1550nm.max()
C8_1550nm_normalized = C8_1550nm / C8_1550nm.max()

# Plot
plt.figure(figsize = (24, 5.5))

plt.subplot(1, 3, 1)
plt.plot(BC_no_photon, C4_no_photon_normalized, 'r-', label = r'Detector 4')
plt.plot(BC_no_photon, C5_no_photon_normalized, 'b-', label = r'Detector 5')
plt.plot(BC_no_photon, C8_no_photon_normalized, 'g-', label = r'Detector 8')
plt.title(r'No photon')
plt.ylabel(r'Photon count (normalized)')
plt.legend(loc = 'upper right', borderpad = 0.2)

plt.subplot(1, 3, 2)
plt.plot(BC_850nm, C4_850nm_normalized, 'r-', label = r'Detector 4')
plt.plot(BC_850nm, C5_850nm_normalized, 'b-', label = r'Detector 5')
plt.plot(BC_850nm, C8_850nm_normalized, 'g-', label = r'Detector 8')
plt.title(r'$\lambda = 850 \: \mathrm{nm}$')
plt.xlabel(r'Bias current')
plt.legend(loc = 'upper right', borderpad = 0.2)

plt.subplot(1, 3, 3)
plt.plot(BC_1550nm, C4_1550nm_normalized, 'r-', label = r'Detector 4')
plt.plot(BC_1550nm, C5_1550nm_normalized, 'b-', label = r'Detector 5')
plt.plot(BC_1550nm, C8_1550nm_normalized, 'g-', label = r'Detector 8')
plt.title(r'$\lambda = 1550 \: \mathrm{nm}$')
plt.legend(loc = 'upper right', borderpad = 0.2)

plt.suptitle(r'Bias current vs photon count (normalized) for different cases', size = 24)
plt.tight_layout()
plt.gcf()
plt.savefig('bias_current_vs_photon_count.pdf')

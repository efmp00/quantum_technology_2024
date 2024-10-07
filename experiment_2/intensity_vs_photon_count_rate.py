# I need to create a class to reduce the amount of code. 
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

# === Detector 4 ===
# Files 0.50 dbm
data_50dbm_1 = read_csv('2024-09-02--14-35-08_850nm_05dbm_1.txt', sep = '\t')
data_50dbm_2 = read_csv('2024-09-02--14-35-08_850nm_05dbm_2.txt', sep = '\t')
data_50dbm_3 = read_csv('2024-09-02--14-35-08_850nm_05dbm_3.txt', sep = '\t')
data_50dbm_4 = read_csv('2024-09-02--14-35-08_850nm_05dbm_4.txt', sep = '\t')

# Data
C4_50dbm_1 = data_50dbm_1["C3"]
C4_50dbm_2 = data_50dbm_2["C3"]
C4_50dbm_3 = data_50dbm_3["C3"]
C4_50dbm_4 = data_50dbm_4["C3"]

# Append the data from all files into one DataFrame or Series
C4_50dbm_combined = concat([C4_50dbm_1, C4_50dbm_2, C4_50dbm_3, C4_50dbm_4])

# Compute the mean of the combined data
C4_50dbm_mean = C4_50dbm_combined.mean()
C4_50dbm_std = C4_50dbm_combined.std()
print(f"Mean Photon Count Rate for C4 at 0.5 dBm: {C4_50dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C4 at 0.5 dBm: {C4_50dbm_std}")

# Files 0.72 dbm
data_72dbm_1 = read_csv('2024-09-10--06-05-51_850nm_72dbm_1.txt', sep = '\t')
data_72dbm_2 = read_csv('2024-09-10--06-09-13-850nm_72dbm_2.txt', sep = '\t')
data_72dbm_3 = read_csv('2024-09-10--06-11-850nm_72dbm_3.txt', sep = '\t')
data_72dbm_4 = read_csv('2024-09-10--06-15-09-850nm_72dbm_4.txt', sep = '\t')

# Data
C4_72dbm_1 = data_72dbm_1["C3"]
C4_72dbm_2 = data_72dbm_2["C3"]
C4_72dbm_3 = data_72dbm_3["C3"]
C4_72dbm_4 = data_72dbm_4["C3"]

# Append the data from all files into one DataFrame or Series
C4_72dbm_combined = concat([C4_72dbm_1, C4_72dbm_2, C4_72dbm_3, C4_72dbm_4])

# Compute the mean of the combined data
C4_72dbm_mean = C4_72dbm_combined.mean()
C4_72dbm_std = C4_72dbm_combined.std()
print(f"Mean Photon Count Rate for C4 at 0.72 dBm: {C4_72dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C4 at 0.72 dBm: {C4_72dbm_mean}")

# Files 0.968 dbm
data_968dbm_1 = read_csv('2024-09-10--06-18-56-850nm_968dbm_1.txt', sep = '\t')
data_968dbm_2 = read_csv('2024-09-10--06-20-45-850nm_968dbm_2.txt', sep = '\t')
data_968dbm_3 = read_csv('2024-09-10--06-22-42-850nm_968dbm_3.txt', sep = '\t')
data_968dbm_4 = read_csv('2024-09-10--06-28-27-850nm_968dbm_4.txt', sep = '\t')

# Data
C4_968dbm_1 = data_968dbm_1["C3"]
C4_968dbm_2 = data_968dbm_2["C3"]
C4_968dbm_3 = data_968dbm_3["C3"]
C4_968dbm_4 = data_968dbm_4["C3"]

# Append the data from all files into one DataFrame or Series
C4_968dbm_combined = concat([C4_968dbm_1, C4_968dbm_2, C4_968dbm_3, C4_968dbm_4])

# Compute the mean of the combined data
C4_968dbm_mean = C4_968dbm_combined.mean()
C4_968dbm_std = C4_968dbm_combined.std()
print(f"Mean Photon Count Rate for C4 at 0.968 dBm: {C4_968dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C4 at 0.968 dBm: {C4_968dbm_mean}")

# Files 1.204 dbm
data_1204dbm_1 = read_csv('2024-09-10--06-30-45-850nm_1204dbm_1.txt', sep = '\t')
data_1204dbm_2 = read_csv('2024-09-10--06-32-37-850nm_1204dbm_2.txt', sep = '\t')
data_1204dbm_3 = read_csv('2024-09-10--06-34-56-850nm_1204dbm_3.txt', sep = '\t')
data_1204dbm_4 = read_csv('2024-09-10--06-36-31-850nm_1204dbm_4.txt', sep = '\t')

# Data
C4_1204dbm_1 = data_1204dbm_1["C3"]
C4_1204dbm_2 = data_1204dbm_2["C3"]
C4_1204dbm_3 = data_1204dbm_3["C3"]
C4_1204dbm_4 = data_1204dbm_4["C3"]

# Append the data from all files into one DataFrame or Series
C4_1204dbm_combined = concat([C4_1204dbm_1, C4_1204dbm_2, C4_1204dbm_3, C4_1204dbm_4])

# Compute the mean of the combined data
C4_1204dbm_mean = C4_1204dbm_combined.mean()
C4_1204dbm_std = C4_1204dbm_combined.std()
print(f"Mean Photon Count Rate for C4 at 1.204 dBm: {C4_1204dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C4 at 1.204 dBm: {C4_1204dbm_std}")

# === Plot ===
# Conversion from dbm to mW
I1, I2, I3, I4 = 10 ** (-0.500 / 10), 10 ** (-0.720 / 10),  10 ** (-0.968 / 10),  10 ** (-1.204 / 10)
intensity = np.array([I4, I3, I2, I1])

mean_photon_count_c4 = np.array([C4_1204dbm_mean, C4_968dbm_mean, C4_72dbm_mean, C4_50dbm_mean])

# === Detector 5 ===
C5_50dbm_1 = data_50dbm_1["C4"]
C5_50dbm_2 = data_50dbm_2["C4"]
C5_50dbm_3 = data_50dbm_3["C4"]
C5_50dbm_4 = data_50dbm_4["C4"]

# Append the data from all files into one DataFrame or Series
C5_50dbm_combined = concat([C5_50dbm_1, C5_50dbm_2, C5_50dbm_3, C5_50dbm_4])

# Compute the mean of the combined data
C5_50dbm_mean = C5_50dbm_combined.mean()
C5_50dbm_std = C5_50dbm_combined.std()
print(f"Mean Photon Count Rate for C5 at 0.5 dBm: {C5_50dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C5 at 0.5 dBm: {C5_50dbm_std}")

# Files 0.72 dbm
data_72dbm_1 = read_csv('2024-09-10--06-05-51_850nm_72dbm_1.txt', sep = '\t')
data_72dbm_2 = read_csv('2024-09-10--06-09-13-850nm_72dbm_2.txt', sep = '\t')
data_72dbm_3 = read_csv('2024-09-10--06-11-850nm_72dbm_3.txt', sep = '\t')
data_72dbm_4 = read_csv('2024-09-10--06-15-09-850nm_72dbm_4.txt', sep = '\t')

# Data
C5_72dbm_1 = data_72dbm_1["C4"]
C5_72dbm_2 = data_72dbm_2["C4"]
C5_72dbm_3 = data_72dbm_3["C4"]
C5_72dbm_4 = data_72dbm_4["C4"]

# Append the data from all files into one DataFrame or Series
C5_72dbm_combined = concat([C5_72dbm_1, C5_72dbm_2, C5_72dbm_3, C5_72dbm_4])

# Compute the mean of the combined data
C5_72dbm_mean = C5_72dbm_combined.mean()
C5_72dbm_std = C5_72dbm_combined.std()
print(f"Mean Photon Count Rate for C5 at 0.72 dBm: {C5_72dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C5 at 0.72 dBm: {C5_72dbm_std}")

# Files 0.968 dbm
data_968dbm_1 = read_csv('2024-09-10--06-18-56-850nm_968dbm_1.txt', sep = '\t')
data_968dbm_2 = read_csv('2024-09-10--06-20-45-850nm_968dbm_2.txt', sep = '\t')
data_968dbm_3 = read_csv('2024-09-10--06-22-42-850nm_968dbm_3.txt', sep = '\t')
data_968dbm_4 = read_csv('2024-09-10--06-28-27-850nm_968dbm_4.txt', sep = '\t')

# Data
C5_968dbm_1 = data_968dbm_1["C4"]
C5_968dbm_2 = data_968dbm_2["C4"]
C5_968dbm_3 = data_968dbm_3["C4"]
C5_968dbm_4 = data_968dbm_4["C4"]

# Append the data from all files into one DataFrame or Series
C5_968dbm_combined = concat([C5_968dbm_1, C5_968dbm_2, C5_968dbm_3, C5_968dbm_4])

# Compute the mean of the combined data
C5_968dbm_mean = C5_968dbm_combined.mean()
C5_968dbm_std = C5_968dbm_combined.std()
print(f"Mean Photon Count Rate for C5 at 0.968 dBm: {C5_968dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C5 at 0.968 dBm: {C5_968dbm_std}")

# Files 1.204 dbm
data_1204dbm_1 = read_csv('2024-09-10--06-30-45-850nm_1204dbm_1.txt', sep = '\t')
data_1204dbm_2 = read_csv('2024-09-10--06-32-37-850nm_1204dbm_2.txt', sep = '\t')
data_1204dbm_3 = read_csv('2024-09-10--06-34-56-850nm_1204dbm_3.txt', sep = '\t')
data_1204dbm_4 = read_csv('2024-09-10--06-36-31-850nm_1204dbm_4.txt', sep = '\t')

# Data
C5_1204dbm_1 = data_1204dbm_1["C4"]
C5_1204dbm_2 = data_1204dbm_2["C4"]
C5_1204dbm_3 = data_1204dbm_3["C4"]
C5_1204dbm_4 = data_1204dbm_4["C4"]

# Append the data from all files into one DataFrame or Series
C5_1204dbm_combined = concat([C5_1204dbm_1, C5_1204dbm_2, C5_1204dbm_3, C5_1204dbm_4])

# Compute the mean of the combined data
C5_1204dbm_mean = C5_1204dbm_combined.mean()
C5_1204dbm_std = C5_1204dbm_combined.std()
print(f"Mean Photon Count Rate for C5 at 1.204 dBm: {C5_1204dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C5 at 1.204 dBm: {C5_1204dbm_std}")

# === Plot ===
mean_photon_count_c5 = np.array([C5_1204dbm_mean, C5_968dbm_mean, C5_72dbm_mean, C5_50dbm_mean])

# === Detector 8 ===
C8_50dbm_1 = data_50dbm_1["C7"]
C8_50dbm_2 = data_50dbm_2["C7"]
C8_50dbm_3 = data_50dbm_3["C7"]
C8_50dbm_4 = data_50dbm_4["C7"]

# Append the data from all files into one DataFrame or Series
C8_50dbm_combined = concat([C8_50dbm_1, C8_50dbm_2, C8_50dbm_3, C8_50dbm_4])

# Compute the mean of the combined data
C8_50dbm_mean = C8_50dbm_combined.mean()
C8_50dbm_std = C8_50dbm_combined.std()
print(f"Mean Photon Count Rate for C8 at 0.5 dBm: {C8_50dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C8 at 0.5 dBm: {C8_50dbm_std}")

# Files 0.72 dbm
data_72dbm_1 = read_csv('2024-09-10--06-05-51_850nm_72dbm_1.txt', sep = '\t')
data_72dbm_2 = read_csv('2024-09-10--06-09-13-850nm_72dbm_2.txt', sep = '\t')
data_72dbm_3 = read_csv('2024-09-10--06-11-850nm_72dbm_3.txt', sep = '\t')
data_72dbm_4 = read_csv('2024-09-10--06-15-09-850nm_72dbm_4.txt', sep = '\t')

# Data
C8_72dbm_1 = data_72dbm_1["C7"]
C8_72dbm_2 = data_72dbm_2["C7"]
C8_72dbm_3 = data_72dbm_3["C7"]
C8_72dbm_4 = data_72dbm_4["C7"]

# Append the data from all files into one DataFrame or Series
C8_72dbm_combined = concat([C8_72dbm_1, C8_72dbm_2, C8_72dbm_3, C8_72dbm_4])

# Compute the mean of the combined data
C8_72dbm_mean = C8_72dbm_combined.mean()
C8_72dbm_std = C8_72dbm_combined.std()
print(f"Mean Photon Count Rate for C8 at 0.72 dBm: {C8_72dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C8 at 0.72 dBm: {C8_72dbm_std}")

# Files 0.968 dbm
data_968dbm_1 = read_csv('2024-09-10--06-18-56-850nm_968dbm_1.txt', sep = '\t')
data_968dbm_2 = read_csv('2024-09-10--06-20-45-850nm_968dbm_2.txt', sep = '\t')
data_968dbm_3 = read_csv('2024-09-10--06-22-42-850nm_968dbm_3.txt', sep = '\t')
data_968dbm_4 = read_csv('2024-09-10--06-28-27-850nm_968dbm_4.txt', sep = '\t')

# Data
C8_968dbm_1 = data_968dbm_1["C7"]
C8_968dbm_2 = data_968dbm_2["C7"]
C8_968dbm_3 = data_968dbm_3["C7"]
C8_968dbm_4 = data_968dbm_4["C7"]

# Append the data from all files into one DataFrame or Series
C8_968dbm_combined = concat([C8_968dbm_1, C8_968dbm_2, C8_968dbm_3, C8_968dbm_4])

# Compute the mean of the combined data
C8_968dbm_mean = C8_968dbm_combined.mean()
C8_968dbm_std = C8_968dbm_combined.std()
print(f"Mean Photon Count Rate for C8 at 0.968 dBm: {C8_968dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C8 at 0.968 dBm: {C8_968dbm_std}")

# Files 1.204 dbm
data_1204dbm_1 = read_csv('2024-09-10--06-30-45-850nm_1204dbm_1.txt', sep = '\t')
data_1204dbm_2 = read_csv('2024-09-10--06-32-37-850nm_1204dbm_2.txt', sep = '\t')
data_1204dbm_3 = read_csv('2024-09-10--06-34-56-850nm_1204dbm_3.txt', sep = '\t')
data_1204dbm_4 = read_csv('2024-09-10--06-36-31-850nm_1204dbm_4.txt', sep = '\t')

# Data
C8_1204dbm_1 = data_1204dbm_1["C7"]
C8_1204dbm_2 = data_1204dbm_2["C7"]
C8_1204dbm_3 = data_1204dbm_3["C7"]
C8_1204dbm_4 = data_1204dbm_4["C7"]

# Append the data from all files into one DataFrame or Series
C8_1204dbm_combined = concat([C8_1204dbm_1, C8_1204dbm_2, C8_1204dbm_3, C8_1204dbm_4])

# Compute the mean of the combined data
C8_1204dbm_mean = C8_1204dbm_combined.mean()
C8_1204dbm_std = C8_1204dbm_combined.std()
print(f"Mean Photon Count Rate for C8 at 1.204 dBm: {C8_1204dbm_mean}")
print(f"Standard Deviation of Photon Count Rate for C8 at 1.204 dBm: {C8_1204dbm_std}")

# === Plot ===
mean_photon_count_c8 = np.array([C8_1204dbm_mean, C8_968dbm_mean, C8_72dbm_mean, C8_50dbm_mean])

# plt.figure(figsize = (10, 4.5))
# plt.plot(intensity, mean_photon_count_c4 / 0.01, 'r', label = 'Detector 4')
# plt.plot(intensity, mean_photon_count_c5 / 0.01, 'b', label = 'Detector 5')
plt.plot(intensity, mean_photon_count_c8 / 0.01, 'g', label = 'Detector 8')

plt.xlabel(r'Intensity ($\mathrm{mW}$)')
plt.ylabel(r'Mean photon count rate ($\mathrm{Hz}$)')
plt.legend()
plt.tight_layout()
plt.gcf()
# plt.savefig('intensity_photon_count_C4.pdf')
# plt.savefig('intensity_photon_count_C5.pdf')
plt.savefig('intensity_photon_count_C8.pdf')

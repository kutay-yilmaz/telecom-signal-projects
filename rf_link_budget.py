import numpy as np
import matplotlib.pyplot as plt

# --- RF LINK BUDGET CALCULATOR ---
# Wireless Communication Project

# 1. PARAMETERS
# Frequencies to compare: 900 MHz (GSM) and 2100 MHz (LTE)
freq_gsm = 900
freq_lte = 2100

# Distance: From 0.1 km to 20 km (100 points)
distance = np.linspace(0.1, 20, 100)

# 2. CALCULATION
# Path Loss Formula (FSPL) for GSM
# Formula: 20*log(d) + 20*log(f) + 32.44
path_loss_gsm = 20 * np.log10(distance) + 20 * np.log10(freq_gsm) + 32.44

# Path Loss for LTE
path_loss_lte = 20 * np.log10(distance) + 20 * np.log10(freq_lte) + 32.44

# Received Power Calculation
# Rx = Tx Power + Gains - Path Loss
tx_power = 43  # 20 Watts in dBm
gain = 18      # Antenna Gain

rx_gsm = tx_power + gain - path_loss_gsm
rx_lte = tx_power + gain - path_loss_lte

# 3. PLOTTING
plt.figure(figsize=(10, 6))

# Plot GSM Line
plt.plot(distance, rx_gsm, 'b', linewidth=2, label='GSM (900 MHz)')

# Plot LTE Line
plt.plot(distance, rx_lte, 'r', linewidth=2, label='LTE (2100 MHz)')

# Sensitivity Threshold (Phone limit)
plt.axhline(y=-100, color='gray', linestyle='--', label='Min Signal Limit')

plt.title('Signal Strength vs Distance')
plt.xlabel('Distance (km)')
plt.ylabel('Received Power (dBm)')
plt.grid(True)
plt.legend()

plt.show()

print("Calculation finished.")

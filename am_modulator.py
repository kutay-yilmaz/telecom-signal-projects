import numpy as np
import matplotlib.pyplot as plt

# --- AM SIGNAL MODULATION SIMULATOR ---
# Telecommunication Engineering Project

# 1. PARAMETERS
# Time axis from 0 to 1 second
t = np.linspace(0, 1, 1000)

# Frequencies (Hz)
fc = 100  # Carrier Frequency (High Speed)
fm = 5    # Message Frequency (Low Speed / Audio)
m = 1.0   # Modulation Index

# 2. SIGNAL CALCULATION
# Create Carrier Wave
carrier = np.cos(2 * np.pi * fc * t)

# Create Message Wave
message = np.cos(2 * np.pi * fm * t)

# Modulation Formula: (1 + m * message) * carrier
am_signal = (1 + m * message) * carrier

# 3. PLOTTING
plt.figure(figsize=(10, 8))

# Plot 1: Message Signal
plt.subplot(3, 1, 1)
plt.plot(t, message, 'g', linewidth=2)
plt.title('Message Signal (Audio Input)')
plt.grid(True, alpha=0.5)

# Plot 2: Carrier Signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier, 'b', alpha=0.7)
plt.title('Carrier Signal (Transport Wave)')
plt.grid(True, alpha=0.5)

# Plot 3: Result (AM Signal)
plt.subplot(3, 1, 3)
plt.plot(t, am_signal, 'r', linewidth=2)
plt.title('AM Modulated Signal (Output)')
plt.xlabel('Time (seconds)')
plt.grid(True, alpha=0.5)

plt.tight_layout()
plt.show()

print("Modulation complete.")

import numpy as np
import matplotlib.pyplot as plt

# --- FFT SPECTRUM ANALYZER ---
# Signal Processing Project

# 1. CREATE SIGNAL WITH NOISE
# Sampling Frequency (1000 Hz)
fs = 1000
t = np.linspace(0, 1, fs)

# Two Signals mixed together: 50 Hz and 120 Hz
clean_signal = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t)

# Add Random Noise
noise = np.random.normal(0, 0.5, len(t))
noisy_signal = clean_signal + noise

# 2. APPLY FFT (FAST FOURIER TRANSFORM)
n = len(t)
# Frequency Axis
freqs = np.fft.fftfreq(n, d=1/fs)

# FFT Calculation
fft_values = np.fft.fft(noisy_signal)
fft_magnitude = np.abs(fft_values)

# 3. PLOTTING
plt.figure(figsize=(12, 6))

# Plot 1: Time Domain (Noisy Signal)
plt.subplot(1, 2, 1)
plt.plot(t[:100], noisy_signal[:100]) # First 0.1 seconds
plt.title('Time Domain (Signal + Noise)')
plt.xlabel('Time (s)')
plt.grid(True)

# Plot 2: Frequency Domain (Spectrum)
plt.subplot(1, 2, 2)
# Show only positive frequencies (0-500Hz)
plt.plot(freqs[:n//2], fft_magnitude[:n//2], color='purple')
plt.title('Frequency Domain (FFT Result)')
plt.xlabel('Frequency (Hz)')
plt.xlim(0, 200) # Zoom into 0-200 Hz range
plt.grid(True)

plt.show()

print("FFT Analysis complete.")

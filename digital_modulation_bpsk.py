import numpy as np
import matplotlib.pyplot as plt
# BPSK DIGITAL MODULATION
def bpsk_simulation():
    bits = [1, 0, 1, 1, 0, 1, 0, 0]
    duration = 1.0
    fs = 100
    t = np.linspace(0, duration, int(fs*duration))
    carrier_freq = 2
    full_signal = []
    for bit in bits:
        if bit == 1:
            phase = 0
            signal = np.cos(2 * np.pi * carrier_freq * t + phase)
        else:
            phase = np.pi
            signal = np.cos(2 * np.pi * carrier_freq * t + phase)
        full_signal.extend(signal)
    plt.figure(figsize=(12, 4))
    plt.step(range(len(bits)), bits, where='post', label='Bits', color='red')
    plt.plot(np.linspace(0, len(bits), len(full_signal)), full_signal, label='Signal')
    plt.grid(True)
    plt.legend()
    plt.show()
    print(f"Transmitted Bits: {bits}")
if __name__ == "__main__":
    bpsk_simulation()

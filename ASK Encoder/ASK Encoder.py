import numpy as np
import matplotlib.pyplot as plt

def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def ask_modulation(binary_data, bit_duration=1, amplitude=1):
    time = np.linspace(0, len(binary_data) * bit_duration, len(binary_data) * 100)
    signal = np.array([amplitude if bit == '1' else 0 for bit in binary_data])
    signal_expanded = np.repeat(signal, 100)  # Smooth representation
    return time, signal_expanded

# Get input message
message = input("Enter message: ")
binary_data = text_to_binary(message)

# Modulate signal
time, signal = ask_modulation(binary_data)

# Plot the ASK Signal
plt.figure(figsize=(10, 4))
plt.plot(time, signal, linewidth=2)
plt.title("ASK Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Print encoded binary
print(f"Binary data: {binary_data}")
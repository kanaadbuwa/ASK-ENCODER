import numpy as np

def read_waveform_from_file(filename):
    """Read amplitude values from a file (CSV or TXT)."""
    try:
        data = np.loadtxt(filename, delimiter=',')  # For CSV (numerical amplitude values)
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def binary_to_text(binary_data):
    """Convert binary string to ASCII text."""
    try:
        chars = [chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)]
        return ''.join(chars)
    except ValueError:
        print("Invalid binary format!")
        return None

# User selects input type
input_type = input("Enter 'binary' for binary input or 'waveform' for waveform file: ").strip().lower()

if input_type == "binary":
    binary_data = input("Enter binary data (e.g., 01001000 01101001): ").replace(" ", "")
    decoded_message = binary_to_text(binary_data)
    if decoded_message:
        print(f"Decoded Message: {decoded_message}")

elif input_type == "waveform":
    file_path = input("Enter waveform file path (CSV/TXT): ").strip()
    received_waveform = read_waveform_from_file(file_path)
    if received_waveform is not None:
        print(f"Loaded waveform data: {received_waveform}")
    else:
        print("Failed to load waveform data.")
        exit(1)  # Exit with an error code

else:
    print("Invalid input type! Please enter either 'binary' or 'waveform'.")
# **ASK Modulation CLI Tool**
This project provides a **Command-Line Interface (CLI) tool** for encoding and decoding messages using **Amplitude Shift Keying (ASK)** modulation.

## **Overview of ASK Modulation**
**Amplitude Shift Keying (ASK)** is a digital modulation technique where the **amplitude of a carrier wave** is varied to represent binary data:
- **Binary '1'** is represented by a high amplitude signal.
- **Binary '0'** is represented by a low or zero amplitude signal.
- The carrier frequency remains unchanged, only the amplitude varies.

### **Applications of ASK**
ASK modulation is widely used in:
- **Radio Frequency Identification (RFID)** systems.
- **Optical communication**, such as fiber optics.
- **Infrared remote controls** and data transmission.
- **Morse code transmission using On-Off Keying (OOK)**, a simple form of ASK.

## **Features of the Tool**
- **ASK Encoder**: Converts text into ASK-modulated waveform.
- **ASK Decoder**: Decodes ASK-modulated signals and binary sequences.
- **Waveform Input Support**: Reads amplitude data from CSV/TXT files.
- **Binary Input Support**: Directly decodes user-provided binary sequences.

## **Installation**
Ensure you have **Python 3.x** installed. Install dependencies using:

```bash
pip install numpy matplotlib serial
```

## **Usage**
### **Encoding a Message (ASK Modulation)**
Run:

```bash
python ask_encoder.py
```

Enter your message when prompted. The tool will:
- Convert the message to binary.
- Generate an ASK-modulated waveform.
- Display the waveform visually.

### **Decoding an ASK Signal**
Run:

```bash
python ask_decoder.py
```

Choose one of the input options:
1. **Binary Input**: Enter binary data (e.g., `01001000 01101001`).
2. **Waveform Input**: Provide a CSV/TXT file containing amplitude values.

## **Example Usage**
#### **Encoding Example**
```bash
$ python ask_encoder.py
Enter message: HELLO
Binary data: 01001000 01000101 01001100 01001100 01001111
(ASK waveform will be displayed)
```

#### **Decoding Example**
```bash
$ python ask_decoder.py
Enter 'binary' for raw binary input or 'waveform' for waveform file: binary
Enter binary data: 01001000 01000101 01001100 01001100 01001111
Decoded Message: HELLO
```

## **Use Cases of This Tool**
- **Educational Purposes**: Understanding digital modulation techniques.
- **Communication Systems**: Testing ASK encoding/decoding for research.
- **Signal Processing**: Analyzing ASK-modulated signals from hardware.
- **Embedded Systems**: Generating ASK signals for transmission using microcontrollers.

## **Future Improvements**
- **Real-time data acquisition** from an oscilloscope.
- **Hardware integration** for direct ASK signal transmission/reception.
- **Noise filtering** for robust signal decoding.

## **Contributing**
Feel free to contribute via pull requests or report issues.

## **License**
This project is licensed under **MIT License**.


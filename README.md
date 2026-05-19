# BCI Mouse Control System

An advanced Brain-Computer Interface (BCI) system that translates EEG signals into real-time mouse movements using Machine Learning.

## 🚀 Overview

This project provides a complete pipeline for controlling a computer cursor using EEG (Electroencephalography) data. It captures raw brainwave data from a serial-connected device, processes it, trains a Random Forest classifier, and enables real-time interaction through custom hardware.

## ✨ Features

- **Real-time Prediction**: Low-latency signal processing for fluid mouse control.
- **Custom Data Collection**: Integrated script to build your own EEG datasets.
- **Machine Learning Integration**: Uses `scikit-learn`'s Random Forest for robust classification of signals.
- **Directional Control**: Support for four primary directions: UP, DOWN, LEFT, and RIGHT.

## 🛠️ System Architecture

1.  **Data Acquisition**: Raw EEG data is streamed via Serial (COM port) from an EEG sensor (e.g., ThinkGear, OpenBCI, or custom Arduino-based sensors).
2.  **Feature Engineering**: Signals are windowed and buffered for consistent model input.
3.  **Classification**: A pre-trained `RandomForestClassifier` identifies the intended direction.
4.  **Human-Interface Emulation**: `pyautogui` translates predictions into OS-level mouse events.

## 📋 Prerequisites

### Hardware
- EEG Sensor with Serial output (default: `COM3` at `115200` baud).
- Microcontroller (Arduino, ESP32, etc.) to interface with the sensor.

### Software
- Python 3.8+
- Required Libraries:
  ```bash
  pip install pyserial numpy pandas scikit-learn joblib pyautogui
  ```

## 🚀 Getting Started

### 1. Data Collection
Before you can control the mouse, you must train the system on your own brainwave patterns.
```bash
python collect_eeg_data.py
```
- Follow the on-screen prompts.
- Focus on the intended direction when prompted.
- This will generate `eeg_dataset.csv`.

### 2. Model Training
Train the Random Forest model using your recorded data.
```bash
python train_model.py
```
- This script splits your data into training/testing sets and reports model accuracy.
- The trained model is saved as `eeg_model.pkl`.

### 3. Real-time Control
Launch the main application to start controlling your mouse.
```bash
python main.py
```

## ⚙️ Configuration

You can customize the settings in `main.py` and `collect_eeg_data.py`:

| Constant | Description | Default |
| :--- | :--- | :--- |
| `PORT` | The COM port for your EEG device | `COM3` |
| `BAUD` | Serial baud rate | `115200` |
| `WINDOW` | Number of samples per prediction | `200` |
| `SAMPLES` | Samples per training instance | `200` |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

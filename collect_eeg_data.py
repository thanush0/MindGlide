import serial
import numpy as np
import pandas as pd
import time

PORT = "COM3"
BAUD = 115200
SAMPLES = 200   # samples per training instance

ser = serial.Serial(PORT, BAUD, timeout=1)
ser.reset_input_buffer()

dataset = []

def record_action(label):

    print(f"\nPrepare for action: {label}")
    time.sleep(3)

    samples = []

    while len(samples) < SAMPLES:

        line = ser.readline().decode('ascii', errors='ignore').strip()

        if line.isdigit():
            samples.append(int(line))

    dataset.append(samples + [label])

    print("Recorded:", label)


actions = ["UP","DOWN","LEFT","RIGHT"]

for action in actions:

    for i in range(20):   # 20 samples per action
        record_action(action)

df = pd.DataFrame(dataset)
df.to_csv("eeg_dataset.csv", index=False)

print("Dataset saved: eeg_dataset.csv")
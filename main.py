import serial
import numpy as np
import joblib
import pyautogui

PORT = "COM3"
BAUD = 115200
WINDOW = 200

model = joblib.load("eeg_model.pkl")

ser = serial.Serial(PORT,BAUD,timeout=1)

buffer = []

while True:

    line = ser.readline().decode('ascii', errors='ignore').strip()

    if line.isdigit():

        buffer.append(int(line))

        if len(buffer) >= WINDOW:

            data = np.array(buffer).reshape(1,-1)

            prediction = model.predict(data)[0]

            print("Prediction:",prediction)

            if prediction == "UP":
                pyautogui.moveRel(0,-20)

            elif prediction == "DOWN":
                pyautogui.moveRel(0,20)

            elif prediction == "LEFT":
                pyautogui.moveRel(-20,0)

            elif prediction == "RIGHT":
                pyautogui.moveRel(20,0)

            buffer.clear()
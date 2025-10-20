# Cotton Bud Detection using OpenCV

This project demonstrates real-time detection of cotton buds using OpenCV and Python.  
It includes two versions of the code — one for pure webcam testing and another integrated with an ESP32 microcontroller for real-time robotic coordination.

---

## 🧩 Files Overview

### 1. `cotton_without_ESP32.py`
- Uses only a webcam.
- Detects circular shapes (cotton buds) in real-time.
- Draws a green circle around detected objects.
- Ideal for computer-vision testing.

### 2. `cotton_with_ESP32.py`
- Includes serial communication between Python and ESP32.
- Sends detected coordinates `(x, y)` of the cotton bud to the ESP32.
- Waits for acknowledgment (`ACK`) before continuing.

---

## ⚙️ Requirements
Install dependencies before running:

```bash
pip install opencv-python numpy pyserial


# Cotton Bud Detection using OpenCV

This project demonstrates real-time detection of cotton buds using OpenCV and Python.  
It includes two versions of the code — one for pure webcam testing and another integrated with an ESP32 microcontroller for real-time robotic coordination.

---

## 🧩 Files Overview

### 1. Webcam Version
📄 [cotton_without_ESP32.py](cotton_without_ESP32.py)

- Uses only a webcam.
- Detects circular shapes (cotton buds) in real-time.
- Draws a green circle around detected objects.
- Suitable for testing and debugging computer vision logic.

---

### 2. ESP32 Integrated Version
📄 [cotton_with_ESP32.py](cotton_with_ESP32.py)

- Uses serial communication (`pyserial`) to connect with ESP32.
- Sends detected `(x, y)` coordinates of cotton buds.
- Waits for acknowledgment (`ACK`) before processing the next frame.
- Designed for real-time robotic applications.

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install opencv-python numpy pyserial

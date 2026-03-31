import cv2
import numpy as np
import serial
import time

def find_cotton_bud(frame, ser):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        if len(approx) >= 5:
            (x, y), radius = cv2.minEnclosingCircle(contour)
            
            if radius > 40 and radius < 50:
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                coord_str = "({},{})".format(int(x), int(y))
                ser.write(coord_str.encode())
                print("Sent Cotton Bud Coordinates: {}".format(coord_str))
                
                # Wait for acknowledgment
                ack_received = False
                while not ack_received:
                    if ser.in_waiting > 0:
                        ack = ser.readline().decode().strip()
                        if ack == "ACK":
                            ack_received = True
                            print("Acknowledgment received")
                            break
    return frame # Return the frame after drawing the contour

# Initialize serial communication with ESP32
ser = serial.Serial('COM4', 9600) # Replace 'COMX' with your serial port
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    result_frame = find_cotton_bud(frame, ser)
    cv2.imshow('Cotton Bud Detection', result_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close serial connection
ser.close()
cap.release()
cv2.destroyAllWindows()

# https://medium.com/swlh/deploy-flask-applications-with-uwsgi-and-nginx-on-ubuntu-18-04-2a47f378c3d2
# Backend stuff
from Backend.onlyfans import tempstat as temps  # Self explanatory
from Backend.modbus import control as ct    # Modbus function
from Backend.params import *    # Register values
from flask import Flask, render_template, jsonify, request, Response    # Backend dev
import json # Data parser
import cv2  # Camera stream OpenCV
import ctypes as t  # Data types as specified in the spec file

app = Flask(__name__)

def gen_frames():
    """
    This is where the magic sauce of the camera is
    """
    
    path = '/dev/video0'
    # USB camera
    camera = cv2.VideoCapture(path)
    brightness = 1.0
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frames

        if success and path == '/dev/video0':   # Camera is online
            # Check the brightness of the image
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            brightness = round(hsv[...,2].mean(), 2)

        if brightness < 0.8 or (not success and path == '/dev/video0'): # Brightness is lower than specified threshold or camera could not be read straight from the port
            path = '/home/pi/Strato_Pi/myproject/static/offline.mp4'    # Alternative video will be played instead of the limitless darkness
            camera = cv2.VideoCapture(path)
            brightness = 1.0

        if not success and path == '/home/pi/Strato_Pi/myproject/static/offline.mp4':   # Once the alternative video has ended
            path = '/dev/video0'    # We'll try again with the original port
            camera = cv2.VideoCapture(path)
            
        if success: # Normal operation
            ret, buffer = cv2.imencode('.jpg', frame)   # Encode the image
            frame = buffer.tobytes()    # Convert to bytes
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # Feed the stream, frame by frame into the Camera stream page

@app.route('/video_feed')
def video_feed():
    """
    This function calls out the hardware frame generator function
    """
    
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api', methods=['GET'])
def api():
    """
    Read all motor data from the backend and send it as JSON to frontend
    """
    
    return jsonify({
        "motor0": {
            "power": t.c_int16(ct(MOTOR_1, READ, MOTOR_POWER, 1)[0]).value,
            "current": round(ct(MOTOR_1, READ, MOTOR_CURRENT, 1)[0]/10.0, 2),
            "voltage": round(ct(MOTOR_1, READ, MAINS_VOLTAGE, 1)[0]/10.0, 2),
            "frequency": round(t.c_int16(ct(MOTOR_1, READ, OUTPUT_FREQ, 1)[0]).value/10.0, 2),
            "speed": round(t.c_int16(ct(MOTOR_1, READ, OUTPUT_VEL, 1)[0]).value)
        },
        "motor1": {
            "power": t.c_int16(ct(MOTOR_2, READ, MOTOR_POWER, 1)[0]).value,
            "current": round(ct(MOTOR_2, READ, MOTOR_CURRENT, 1)[0]/10.0, 2),
            "voltage": round(ct(MOTOR_2, READ, MAINS_VOLTAGE, 1)[0]/10.0, 2),
            "frequency": round(t.c_int16(ct(MOTOR_2, READ, OUTPUT_FREQ, 1)[0]).value/10.0, 2),
            "speed": round(t.c_int16(ct(MOTOR_2, READ, OUTPUT_VEL, 1)[0]).value)
        },
        "motor2": {
            "power": t.c_int16(ct(MOTOR_3, READ, MOTOR_POWER, 1)[0]).value,
            "current": round(ct(MOTOR_3, READ, MOTOR_CURRENT, 1)[0]/10.0, 2),
            "voltage": round(ct(MOTOR_3, READ, MAINS_VOLTAGE, 1)[0]/10.0, 2),
            "frequency": round(t.c_int16(ct(MOTOR_3, READ, OUTPUT_FREQ, 1)[0]).value/10.0, 2),
            "speed": round(t.c_int16(ct(MOTOR_3, READ, OUTPUT_VEL, 1)[0]).value)
        }
    })

@app.route('/api', methods=['POST'])
def api_submit():
    """
    Upon interaction with sliders, should print motor voltage, not sure yet
    """
    
    if request.data:
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))
    print(d["motor"], d["value"])

    return "ok"

@app.route('/button_control', methods=['POST'])
def buttons_api():
    """
    Takes button states as JSON from frontend, parses them and sends out commands to the motors accordingly
    """
    
    if request.data:    # Request the data from frontend
        print('Data:' + str(request.data))  # Print data

    d = dict(json.loads(request.data.decode("utf-8")))  # Decode and parse data from JSON to dict
    print(d["name"])    # Print all button and its data as a continuous string

    name = d["name"][-2:]   # Extract button name
    motor_num = int(name[0])    # Extract motor number
    command = int(name[1])  # Extract command

    if command == 1:
        ct(motors[motor_num], WRITE, REF_SWITCH, W_MODBUS)  # Control motor through modbus
    if command == 2:
        ct(motors[motor_num], WRITE, REF_SWITCH, W_TERMINAL)    # Control motor through terminal
    if command == 3:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x0006)
    if command == 4:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x0080)
    if command == 5:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x000F)
    if command == 6:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x080F)
    if command == 7:    # Set motor states to stop and shutdown? Please check the registry values from Excel, TODO: [EXCEL]
        ct(MOTOR_1, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_2, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_3, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_1, WRITE, LOGIC_OUTPUTS, 0b10)
        ct(MOTOR_3, WRITE, LOGIC_OUTPUTS, 0b10)
    if command == 8:    # Similar to command 7, please check and improve, TODO: [EXCEL]
        ct(MOTOR_1, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_2, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_3, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_2, WRITE, LOGIC_OUTPUTS, 0b10)
        ct(MOTOR_3, WRITE, LOGIC_OUTPUTS, 0b10)
    if command == 9:    # Set frequency state to something, TODO: [EXCEL]
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x0002)

    return "ok"

@app.route('/motor_control', methods=['POST'])
def motors_api():
    """
    Prints out interactions with the motors, controls nothing
    """
    
    if request.data:
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))
    for i in d:
        print(i, d[i])

    return "ok"

@app.route('/frequency', methods=['POST'])
def freq_api():
    """
    Takes frequency slider values, parses them and sends commands to motors
    """
    
    if request.data:    # Print out the data
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))  # Decode data
    for i in d:
        print(i, d[i])  # Debug feature print

    value = float(d["value"])*10    # Hack, because frequencies are being read a bit differently in the manual

    name = d["id"][-1]  # Extract the motor name
    motor_num = int(name[0])    # And the motor number

    # Send command to motor
    k = ct(motors[motor_num], WRITE, SET_FREQ, int(value))
    print(k)    # Print the status
    return "ok"

@app.route('/speed', methods=['POST'])
def speed_api():
    """
    Takes RPM slider values, parses them and sends commands to motors
    """
    
    if request.data:    # Print out the data
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))  # Decode it
    for i in d:
        print(i, d[i])  # Debug print

    value = int(d["value"]) # Extract the RPM value
    name = d["id"][-1]  # Motor name
    motor_num = int(name[0])    # Motor number

    # Send command
    ct(motors[motor_num], WRITE, SET_SPEED, value)

    return "ok"

@app.route('/')
def control():
    """
    Render the page
    """
    
    return render_template('control.html')

@app.route('/docs')
def docs():
    """
    Render the page
    """
    
    return render_template('documentation.html')

@app.route('/live_feed')
def camera():
    """
    Render the page
    """
    
    return render_template('cam.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

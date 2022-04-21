# https://medium.com/swlh/deploy-flask-applications-with-uwsgi-and-nginx-on-ubuntu-18-04-2a47f378c3d2
# Backend stuff
from Backend.onlyfans import tempstat
from Backend.modbus import control as ct
from Backend.params import *
from flask import Flask, render_template, jsonify, request, Response
import json
import cv2
import ctypes as t

app = Flask(__name__)

def gen_frames():
    path = '/dev/video0'
    # USB camera
    camera = cv2.VideoCapture(path)
    v = 1.0
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frames

        if success and path == '/dev/video0':
            # Check the brightness of the image
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            v = hsv[...,2].mean()
        elif (not success and path == '/dev/video0') or (v < 0.8):
            # Change stream to a video
            path = '/home/pi/Videos/info.mp4'
            camera = cv2.VideoCapture(path)
            #v = 1.0
        elif (not success and path == '/home/pi/Videos/info.mp4'):
            # Try changing back to camera
            path = '/dev/video0'
            camera = cv2.VideoCapture(path)
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/video_feed')
def video_feed():
    # Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api', methods=['GET'])
def api():
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
    if request.data:
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))
    print(d["motor"], d["value"])

    return "ok"

@app.route('/button_control', methods=['POST'])
def buttons_api():
    if request.data:
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))
    print(d["name"])

    name = d["name"][-2:]
    motor_num = int(name[0])
    command = int(name[1])

    if command == 1:
        ct(motors[motor_num], WRITE, REF_SWITCH, W_MODBUS)
    if command == 2:
        ct(motors[motor_num], WRITE, REF_SWITCH, W_TERMINAL)
    if command == 3:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x0006)
    if command == 4:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x0080)
    if command == 5:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x000F)
    if command == 6:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x080F)
    if command == 7:
        ct(MOTOR_1, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_2, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_3, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_1, WRITE, LOGIC_OUTPUTS, 0b10)
        ct(MOTOR_3, WRITE, LOGIC_OUTPUTS, 0b10)
    if command == 8:
        ct(MOTOR_1, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_2, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_3, WRITE, LOGIC_OUTPUTS, 0b00)
        ct(MOTOR_2, WRITE, LOGIC_OUTPUTS, 0b10)
        ct(MOTOR_3, WRITE, LOGIC_OUTPUTS, 0b10)
    if command == 9:
        ct(motors[motor_num], WRITE, CTR_W_FREQ, 0x0002)

    return "ok"

@app.route('/motor_control', methods=['POST'])
def motors_api():
    if request.data:
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))
    for i in d:
        print(i, d[i])

    return "ok"

@app.route('/frequency', methods=['POST'])
def freq_api():
    if request.data:
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))
    for i in d:
        print(i, d[i])

    value = float(d["value"])*10

    name = d["id"][-1]
    motor_num = int(name[0])

    # Send command
    ct(motors[motor_num], WRITE, SET_FREQ, int(value))

    return "ok"

@app.route('/speed', methods=['POST'])
def speed_api():
    if request.data:
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))
    for i in d:
        print(i, d[i])

    value = int(d["value"])
    name = d["id"][-1]
    motor_num = int(name[0])

    # Send command
    ct(motors[motor_num], WRITE, SET_SPEED, value)

    return "ok"

@app.route('/')
def control():
    return render_template('control.html')

@app.route('/docs')
def docs():
    return render_template('documentation.html')

@app.route('/live_feed')
def camera():
    return render_template('cam.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

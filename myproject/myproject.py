# https://medium.com/swlh/deploy-flask-applications-with-uwsgi-and-nginx-on-ubuntu-18-04-2a47f378c3d2
import time
import random
# import raspi cpu params
#from gpiozero import CPUTemperature
# Flask for web-dev
from flask import Flask, render_template, jsonify, request, Response
import json
import cv2

app = Flask(__name__)

def cpu_temp():
    return round(random.random()*100, 2)

# USB camera
#camera = cv2.VideoCapture(0)#'/dev/video0')
path = '/home/pi/Videos/info.mp4'
#path = '/dev/video0'

def gen_frames():
    camera = cv2.VideoCapture(path)
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frames

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
            "current": cpu_temp(),
            "voltage": cpu_temp(),
            "frequency": cpu_temp(),
            "speed": cpu_temp()
        },
        "motor1": {
            "current": cpu_temp(),
            "voltage": cpu_temp(),
            "frequency": cpu_temp(),
            "speed": cpu_temp()
        },
        "motor2": {
            "current": cpu_temp(),
            "voltage": cpu_temp(),
            "frequency": cpu_temp(),
            "speed": cpu_temp()
        }       
    })

@app.route('/api', methods=['POST'])
def api_submit():
    if request.data:
        print('Data:' + str(request.data))

    d = dict(json.loads(request.data.decode("utf-8")))
    print(d["motor"], d["value"])
    return "ok"

@app.route('/')
def home():
    return render_template('overview.html')

@app.route('/sys_control')
def control():
    return render_template('control.html')

@app.route('/docs')
def docs():
    return render_template('documentation.html')

@app.route('/live_feed')
def camera():
    return render_template('cam.html')

if __name__ == '__main__':
    app.run(port='0.0.0.0')

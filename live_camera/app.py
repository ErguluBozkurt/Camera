import cv2
from flask import Flask, render_template, Response, jsonify
from webcamvideostream import WebcamVideoStream
from thermalcamerastream import ThermalCameraStream
from flask_basicauth import BasicAuth
import random  

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'pi'
app.config['BASIC_AUTH_PASSWORD'] = 'pi'
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        if camera.stopped:
            break
        frame = camera.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        if jpeg is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
        else:
            print("frame is none")

@app.route('/video_feed')
def video_feed():
    return Response(gen(WebcamVideoStream().start()),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/thermal_feed')
def thermal_feed():
    return Response(gen(ThermalCameraStream().start()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_sensor_data')
def get_sensor_data():
    data = {
        'temperature': round(25 + random.uniform(-2, 2), 1),  # 25°C ± 2°C
        'pressure': round(1013 + random.uniform(-5, 5), 2),  # 1013 hPa ± 5
        'altitude': round(50 + random.uniform(-10, 10), 2),  # 50m ± 10m
        'euler': {
            'yaw': round(random.uniform(0, 360), 2),
            'pitch': round(random.uniform(-90, 90), 2),
            'roll': round(random.uniform(-180, 180), 2)
        },
        'acceleration': {
            'x': round(random.uniform(-2, 2), 3),
            'y': round(random.uniform(-2, 2), 3),
            'z': round(random.uniform(-2, 2), 3)
        },
        'linear_acceleration': {
            'x': round(random.uniform(-2, 2), 3),
            'y': round(random.uniform(-2, 2), 3),
            'z': round(random.uniform(-2, 2), 3)
        },
        'quaternion': {
            'w': round(random.uniform(-1, 1), 3),
            'x': round(random.uniform(-1, 1), 3),
            'y': round(random.uniform(-1, 1), 3),
            'z': round(random.uniform(-1, 1), 3)
        },
        'angular_velocity': {
            'x': round(random.uniform(-180, 180), 2),
            'y': round(random.uniform(-180, 180), 2),
            'z': round(random.uniform(-180, 180), 2)
        },
        'gravity': round(random.uniform(9.5, 9.9), 3), 
        'distance': round(random.uniform(5, 500), 3) 
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, threaded=True)

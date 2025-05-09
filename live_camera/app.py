import cv2
from flask import Flask, render_template, Response
from webcamvideostream import WebcamVideoStream
from flask_basicauth import BasicAuth

app = Flask(__name__)

# Basic Auth ayarları
app.config['BASIC_AUTH_USERNAME'] = 'kullanici'  # Kullanıcı adı
app.config['BASIC_AUTH_PASSWORD'] = 'sifre'      # Şifre
app.config['BASIC_AUTH_FORCE'] = True           # Tüm sayfalarda zorunlu

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
        if frame is not None:
            ret, jpeg = cv2.imencode('.jpg', frame)
            if ret:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
        else:
            print("frame is none")

@app.route('/video_feed')
def video_feed():
    try:
        return Response(gen(WebcamVideoStream().start()), mimetype='multipart/x-mixed-replace; boundary=frame')
    except Exception as e:
        return "Video Akışı Hatası: " + str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

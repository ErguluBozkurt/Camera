from picamera2 import Picamera2
from threading import Thread
import numpy as np

class WebcamVideoStream:
    def __init__(self):
        print("init")
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
        self.picam2.start()
        self.frame = None
        self.stopped = False

    def start(self):
        print("start thread")
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        print("read")
        while not self.stopped:
            self.frame = self.picam2.capture_array()

    def read(self):
        return self.frame

    def stop(self):
        self.stopped = True

import cv2
import requests

class Client:

    def __init__(self, video_path):
        self.cap = cv2.VideoCapture(video_path)

    def _send_to_server(self, frame):
        im_encode = cv2.imencode(".jpg", frame)[1]
        current_file = {"file" : ("image.jpg", im_encode.tostring(), "image/jpeg")}
        print("sending")
        res = requests.post("http://localhost:5000", files = current_file)
        print(res.status_code)
        return res

    def run(self):

        running = True

        while running:
            ret , frame = self.cap.read()
            print(ret)

            if ret == False:
                running = False
                continue

            self._send_to_server(frame = frame)




def main():
    client = Client(video_path = 0)
    client.run()

if __name__ == "__main__":
    main()


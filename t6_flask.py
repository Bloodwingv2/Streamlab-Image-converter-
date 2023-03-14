import cv2
import numpy as np
from flask import Flask, request

app = Flask(__name__)
# img = gray = canny = img_contours = None

@app.route('/grayscale', methods=['POST'])
def grayscale():
    img_data = request.files['file'].read()
    img_data_np = np.fromstring(img_data, np.uint8)

    img = cv2.imdecode(img_data_np, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, result = cv2.imencode('.jpg', gray)

    return result.tobytes()

@app.route('/canny', methods=['POST'])
def edges():
    img_data = request.files['file'].read()
    img_data_np = np.fromstring(img_data, np.uint8)

    img = cv2.imdecode(img_data_np, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 50, 100)

    _, result = cv2.imencode('.jpg', canny)

    return result.tobytes()


@app.route('/contours', methods=['POST'])
def contours():
    img_data = request.files['file'].read()
    img_data_np = np.fromstring(img_data, np.uint8)

    img = cv2.imdecode(img_data_np, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 200, 250)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

    _, result = cv2.imencode('.jpg', img)

    return result.tobytes()

if __name__ == "__main__":
    app.run()
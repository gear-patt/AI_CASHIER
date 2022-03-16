from tensorflow.keras.models import load_model
loaded_model = load_model('real_model.h5')

import cv2
import numpy as np
def test_model(img): #img = file_name(str)
    img = cv2.imread(img)
    img = cv2.resize(img, (32, 32))
    img = img/255.0
    l = []
    l.append(img)
    l = np.asarray(l)
    prediction = np.argmax(loaded_model.predict(l))
    probability = loaded_model.predict(l)
    result = ''
    if prediction == 0:
        result = 'prediction: apple'
    elif prediction == 1:
        result = 'prediction: capsicum'
    elif prediction == 2:
        result = 'prediction: lemon'
    elif prediction == 3:
        result = 'prediction: orange'
    else:
        result = 'prediction: potato'
    print(probability)
    return result

import serial
import time

cam = cv2.VideoCapture(1)

cv2.namedWindow("test")
img_counter = 0
serialcomm = serial.Serial('/dev/cu.usbmodem14401', 9600)
serialcomm.timeout = 1

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    text = ""
    if k % 256 == 27:
        # ESC pressed
        # apple is 25 baht, banana is 20 baht, capsicum is 15 baht, corn is 10 baht, orange is 5 baht.
        text = "Done"
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        img_counter += 1
        result = test_model(img_name)
        if result == 'prediction: apple':
            text = "Apple 25"
        elif result == 'prediction: capsicum':
            text = "Capsicum 20"
        elif result == 'prediction: lemon':
            text = "Lemon 15"
        elif result == 'prediction: orange':
            text = "Orange 10"
        else:
            text = "Potato 5"
    if text == 'Done':
        break
    if text != '':
        print(text)
        serialcomm.write(text.encode())
        time.sleep(0.01)

serialcomm.close()

cam.release()

cv2.destroyAllWindows()
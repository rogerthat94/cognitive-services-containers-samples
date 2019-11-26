import cv2
import requests
import numpy as np
from pprint import pprint

face_uri = "http://localhost:5000/face/v1.0/detect?returnFaceAttributes=*"

pathToFileInDisk = r'<path to image>'

with open( pathToFileInDisk, 'rb' ) as f:
    data = f.read()
    headers = { "Content-Type": "image/jpeg" }

    response = requests.post(face_uri, headers=headers, data=data)
    faces = response.json()

    pprint(faces)

    np_data = np.fromstring(data, dtype=np.uint8)
    img = cv2.imdecode(np_data, cv2.IMREAD_COLOR)
    for face in faces:
        rectangle = face[u'faceRectangle']
        height = rectangle[u'height']
        left = rectangle[u'left']
        top = rectangle[u'top']
        width = rectangle[u'width']

        cv2.rectangle(img, (left, top), ((left + width), (top + height)), (123, 174, 54), 3)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

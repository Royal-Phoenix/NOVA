from pyzbar.pyzbar import decode
import numpy as np
import cv2


class Scanner:
    def __init__(self):
        cap, run = cv2.VideoCapture(0), False
        while not run:
            ret, frame = cap.read()
            run = self.decoder(frame)
            cv2.imshow('Image', frame)
            code = cv2.waitKey(10)
        self.data = run
    
    def decoder(self, image):
        barcode = decode(cv2.cvtColor(image,0))
        for obj in barcode:
            points = obj.polygon
            x, y, w, h = obj.rect
            pts = np.array(points, np.int32).reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)
            #barcodeData, barcodeType = obj.data.decode("utf-8"), obj.type
            #string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
            string = obj.data.decode('utf-8')
            cv2.putText(image, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            #print("Barcode: " + barcodeData + " | Type: " + barcodeType)
            return string

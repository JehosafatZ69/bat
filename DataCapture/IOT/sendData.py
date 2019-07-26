#!/usr/bin/python
import json
import RPi.GPIO as IO
import time
from firebase import firebase

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(4, IO.IN)

def doc(vl):
    if vl:
        Document = open('barCodeScanner.txt','r')
        barcode = Document.read()
        Document.close()
        return barcode
    else:
        Document = open('barCodeScanner.txt','w')
        Document.write('')
        Document.close()
        return

def send_data(barcode, temperature, humidity):
    hasCode = ''
    if barcode:
        hasCode = True
    else:
        hasCode = False
    data = {
        'code': barcode,
        'createdAt': time.time(),
        'did': 'Raspbian',
        'hasCode': hasCode,
        'temperature': temperature,
        'humidity': humidity
    }
    print("DATA:", data)
    fire = firebase.FirebaseApplication('https://a-fs-dev.firebaseio.com/')
    response = fire.post('/push', data)
    print('Respopnse', response)
    return

if __name__ == '__main__':
    sl = 0
    oldBarcode = 0
    try:
        while True:
            if(IO.input(4) == False):
                print("The presence ofFalse an object was detected")
                temperature, humidity = 1, 1

                barcode = doc(True)
                if barcode:

                    if (barcode == oldBarcode):
                        print("The barcode is repeated")

                    else:
                        oldBarcode = barcode
                        print("Barcode detected")
                        print("Barcode: ", oldBarcode)
                        send_data(oldBarcode, temperature, humidity)

                else:
                    print("No barcode was detected")
                    time.sleep(1)
                    sl = sl + 1
                    if sl >= 30:
                        print("The object does not have a barcode")
                        send_data('', temperature, humidity)
                        sl = 0
            else:
                print("Object not detected")
                doc(False)


    except KeyboardInterrupt:
        pass
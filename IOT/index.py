#!/usr/bin/python
import Adafruit_DHT as dht
import json
import RPi.GPIO as IO
import time
from firebase import firebase

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(22, IO.IN) ## GPIO 14 -> IR sensor as input {}=> orange = 5v, yellow = gnd, green = pin22

def dht22_reader():
    humidity, temperature = dht.read_retry(dht.DHT22, 27)
    humidity = round(humidity, 3)
    temperature = round(temperature)
    
    return (temperature, humidity)

def read_document():
    Document = open('barCodeScanner.txt','r')
    barcode = Document.read()
    Document.close()
    return barcode

def clean_document():
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
            if(IO.input(22) == False):
                print("The presence of an object was detected")
                temperature, humidity = dht22_reader()

                barcode = read_document()
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
                    time.sleep(30)
                    sl = sl + 1
                    if sl == 2:
                        print("The object does not have a barcode")
                        send_data('', temperature, humidity)
                        sl = 0
            else:
                print("Object not detected")
                clean_document()
                
            
    except KeyboardInterrupt:
        pass

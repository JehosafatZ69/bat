#!/usr/bin/python
import sys
import json
import time
from firebase import firebase
import Adafruit_DHT as dht

def barcode_reader():
    
    hid = {30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0'}

    hid2 = {4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M',
            17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y',
            29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ',
            45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':', 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'}

    fp = open('/dev/hidraw0', 'rb')

    ss = ""
    shift = False

    done = False

    while not done:

        ## Get the character from the HID
        buffer = fp.read(8)
        for c in buffer:
            if ord(c) > 0:

                ##  40 is carriage return which signifies
                ##  we are done looking for characters
                if int(ord(c)) == 40:
                    done = True
                    break;

                ##  If we are shifted then we have to
                ##  use the hid2 characters.
                if shift:

                    ## If it is a '2' then it is the shift key
                    if int(ord(c)) == 2:
                        shift = True

                    ## if not a 2 then lookup the mapping
                    else:
                        ss += hid2[int(ord(c))]
                        shift = False

                ##  If we are not shifted then use
                ##  the hid characters

                else:

                    ## If it is a '2' then it is the shift key
                    if int(ord(c)) == 2:
                        shift = True

                    ## if not a 2 then lookup the mapping
                    else:
                        ss += hid[int(ord(c))]
    t, h = dht22_reader()
    
    print("Codigo de barras", ss)
    data = {
        'code': ss,
        'createdAt': time.time(),
        'did': 'Raspbian',
        'hasCode': True,
        'temperature': t,
        'humidity': h
    }
    print("DATA: {}", data)
    fire = firebase.FirebaseApplication('https://a-fs-dev.firebaseio.com/')
    r = fire.post('/push', data)
    print('Respopnse', r)
    
    
    return ss

def dht22_reader():
    h,t = dht.read_retry(dht.DHT22, 27)
    h = round(h, 3)
    t = round(t)
    
    return (t, h)
    
if __name__ == '__main__':
    try:
        while True:
            barcode_reader()
            ##UPC_lookup(api_key,barcode_reader())
    except KeyboardInterrupt:
        pass


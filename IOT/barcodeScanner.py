#!/usr/bin/python
import sys
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

        buffer = fp.read(8)
        for c in buffer:
            if ord(c) > 0:

                if int(ord(c)) == 40:
                    done = True
                    break;
                
                if shift:
                    if int(ord(c)) == 2:
                        shift = True
                    else:
                        ss += hid2[int(ord(c))]
                        shift = False

                else:
                    
                    if int(ord(c)) == 2:
                        shift = True
                        
                    else:
                        ss += hid[int(ord(c))]
    
    
    return ss
    
if __name__ == '__main__':
    try:
        while True:
            bc = barcode_reader()
            print("REader Bar code", bc)
            barcode = open ('barCodeScanner.txt','w')
            barcode.write(bc)
            barcode.close()
            
    except KeyboardInterrupt:
        pass
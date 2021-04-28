"""
pyserial module MODIFIED
"""
import  serial
import time

def initConnection(portNo, baudRate):
    try:
        ser = serial.Serial(portNo, baudRate)
        print("Device Connected")
        return ser
    except:
        print("Not Connected")
def sendData(se, data, digits):
    myString = "$"
    for d in data:
        myString += str(d).zfill(digits)
        try:
            se.write(myString.encode())
            print(myString)
        except:
            print("Data transmision failed")



if __name__== "__main__":
    ser = initConnection("/dev/ttyUSB0", 9600)
    while True:
        sendData(ser, [0, 255], 3)
        time.sleep(1)
        #sendData(ser, [0, 0], 3)
        #time.sleep(1)

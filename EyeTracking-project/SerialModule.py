"""
pyserial module modified LED on/off or turn servo X/Y
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
    i = int(len(data))
    for d in data:
        myString += str(d).zfill(digits)
        i = i-1
        if i == 0:
            try:
                se.write(myString.encode())
                print(myString)
            except:
                print("Data transmision failed")



if __name__== "__main__":
    ser = initConnection("/dev/ttyUSB0", 9600)
    # while True:
    #      # sendData(ser, [50, 255], 3)  # test LED on/off
    #      sendData(ser, [50, 50], 3)  # test SERVO X/Y
    #      time.sleep(1)
    #      sendData(ser, [0, 0], 3)
    #      time.sleep(1)

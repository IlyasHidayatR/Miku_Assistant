import serial

data_serial = serial.Serial('COM9', 9600)

def getValue():
    data_serial.write(b'1')
    data = data_serial.readline().decode('ascii')
    return data

def onLamp(self):
    user_input = self
    if user_input == '1':
        print(getValue())
    elif user_input == '0':
        print(getValue())
    else:
        print("can't get value")
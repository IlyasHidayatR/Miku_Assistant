import serial

data_serial = serial.Serial('COM9', 9600)

def getValue():
    data_serial.write(b'1')
    data = data_serial.readline().decode('ascii')
    return data

def onLamp(self):
    user_input = self
    if user_input == 'a':
        print(getValue())
    elif user_input == 'b':
        print(getValue())
    elif user_input == 'c':
        print(getValue())
    else:
        print("can't get value")

    return user_input

def lockDoor(op):
    user_input = op
    if user_input == '2':
        print(getValue())
    else:
        print("can't get value")

    return user_input

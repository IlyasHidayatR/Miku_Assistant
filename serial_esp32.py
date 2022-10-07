import time
import urllib.request
import serial

# url for on and off LED and Lock Door dalam array
Elektronik = ["http://192.168.43.72/LED=ON", "http://192.168.43.72/LED=OFF", "http://192.168.43.72/LOCK=ON", "http://192.168.43.72/LOCK=OFF"]


# data_serial = serial.Serial('COM9', 9600)

# def getValue():
#     data_serial.write(b'1')
#     data = data_serial.readline().decode('ascii')
#     return data

def Operation(self):
    # user_input = self
    if self == 1:
        print("LED ON")
        try:
            LED_ON = urllib.request.urlopen(Elektronik[0])
            print(LED_ON)
            print("LED is ON")
        except Exception as e:
            print("Error")
    elif self == 2:
        print("LED OFF")
        try:
            LED_OFF = urllib.request.urlopen(Elektronik[1])
            print(LED_OFF)
            print("LED is OFF")
        except Exception as e:
            print("Error")
    elif self == 3:
        print("LOCK ON")
        try:
            LOCK_ON = urllib.request.urlopen(Elektronik[2])
            print(LOCK_ON)
            print("Lock Door is ON")
            # time.sleep(5)
            # r = requests.get(lockOFF_url)
            # print(r)
        except Exception as e:
            print("Error")
    elif self == 4:
        print("LOCK OFF")
        try:
            LOCK_OFF = urllib.request.urlopen(Elektronik[3])
            print(LOCK_OFF)
            print ("Lock Door is OFF")
        except Exception as e:
            print("Error")

    # if user_input == 'a':
    #     print(getValue())
    # elif user_input == 'b':
    #     print(getValue())
    # elif user_input == 'c':
    #     print(getValue())
    # else:
    #     print("can't get value")

    # return user_input


# if __name__ == '__main__':
#     while True:
#         user_input = int(input("Enter your option: "))
#         Operation(user_input)

import time
import requests
import serial

# url for on and off LED and Lock Door
ledON_url = "http://192.168.43.72/LED=ON"
ledOFF_url = "http://192.168.43.72/LED=OFF"
lockON_url = "http://192.168.43.72/LOCK=ON"
lockOFF_url = "http://192.168.43.72/LOCK=OFF"

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
            requests.get(ledON_url)
        except Exception as e:
            print("Error")
    elif self == 2:
        print("LED OFF")
        try:
            requests.get(ledOFF_url)
        except Exception as e:
            print("Error")
    elif self == 3:
        print("LOCK ON")
        try:
            requests.get(lockON_url)
            print("Lock Door is ON")
            # time.sleep(5)
            # r = requests.get(lockOFF_url)
            # print(r)
        except Exception as e:
            print("Error")
    elif self == 4:
        print("LOCK OFF")
        try:
            requests.get(lockOFF_url)
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

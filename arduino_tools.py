#control lock door selenoid with firmata
#import modules firmata and time
from pyfirmata import Arduino, util
import time
#set board to arduino uno
board = Arduino('COM8')

lamp = 12
lockdor = 8 #pin 8 sebagai output untuk selenoid lock door

#Fungsi untuk mengontrol selenoid lock door
def Operation(ops):
    if ops == 1:
        board.digital[lamp].write(1)
        print("Lamp On")
    elif ops == 2:
        board.digital[lamp].write(0)
        print("Lamp off")
    elif ops == 3:
        #buka lock door selama 5 detik kemudian tutup
        board.digital[lockdor].write(1)
        time.sleep(5)
        board.digital[lockdor].write(0)
    else:
        print("Can't get value")

# while True:
#     user_input = int(input("Enter your option: "))
#     Operation(user_input)
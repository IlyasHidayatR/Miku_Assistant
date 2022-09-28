#control lock door selenoid with firmata
#import modules firmata and time
from pyfirmata import Arduino, util
import time
#set board to arduino uno
board = Arduino('COM3')

lockdoor = 8 #pin 8 sebagai output untuk selenoid lock door

#Fungsi untuk mengontrol selenoid lock door
def lockdoor():
    #Buka selenoid lock door
    board.digital[lockdoor].write(1)
    time.sleep(3) #tunggu 3 detik
    #Tutup selenoid lock door
    board.digital[lockdoor].write(0)
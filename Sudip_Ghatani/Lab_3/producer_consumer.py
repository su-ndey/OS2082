import threading
import time
import random
from threading import Semaphore
buffer = []
empty = Semaphore (5)
full = Semaphore (0)
mutex = Semaphore (1)
def producer () :
    while True :
        item = random . randint (1 , 100)
        empty . acquire ()
        mutex . acquire ()
        buffer . append ( item )
        print (f" Produced : ␣ { item } " )
        mutex . release ()
        full . release ()
        time . sleep ( random . random () )

def consumer () :
    while True :
        full . acquire ()
        mutex . acquire ()
        item = buffer . pop (0)
        print ( f" Consumed : ␣ { item } " )
        mutex . release ()
        empty . release ()
        time . sleep ( random . random () )
threading . Thread ( target = producer ) . start ()
threading . Thread ( target = consumer ) . start ()
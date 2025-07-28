import threading
import time
mutex = threading . Semaphore (1)
rw_mutex = threading . Semaphore (1)
read_count = 0
shared_data = 0
def reader ( id ) :
    global read_count
    while True :
        mutex . acquire ()
        read_count += 1
        if read_count == 1:
         rw_mutex .acquire ()
        mutex . release ()
        print ( f" Reader ␣ { id } ␣ reads : ␣ { shared_data } " )
        time . sleep (1)
        mutex . acquire ()
        read_count -= 1
        if read_count == 0:
         rw_mutex . release ()
        mutex . release ()
        time . sleep (1)
def writer ( id ) :
    global shared_data
    while True :
        rw_mutex . acquire ()
        shared_data += 1
        print ( f" Writer ␣ { id } ␣ writes : ␣ { shared_data } " )
        rw_mutex . release ()
        time . sleep (2)
for i in range (2) :
    threading . Thread ( target = reader , args =( i +1 ,) ) . start ()
threading . Thread ( target = writer , args =(1 ,) ) . start ()
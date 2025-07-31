import threading
import time
forks = [ threading . Semaphore (1) for _ in range (5) ]
def philosopher ( i ) :
    left = forks [ i ]
    right = forks [( i +1) % 5]
    while True :
        print (f" Philosopher ␣ { i } ␣ is ␣ thinking " )
        time . sleep (1)
        left . acquire ()
        right . acquire ()
        print (f" Philosopher ␣ { i } ␣ is ␣ eating " )
        time . sleep (2)
        left . release ()
        right . release ()
for i in range (5) :
    threading . Thread ( target = philosopher , args =( i ,) ) . start ()
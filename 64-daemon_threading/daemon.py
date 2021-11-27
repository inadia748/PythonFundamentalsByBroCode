# ************************************************************
# Python daemon threads
# ************************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes


# Example 1

# Here, when you run this program, it will keep on counting the timer until the user enters something to exit them. But, it will keep on running the timer infinetly without giving a chance to the user to exit them. It is a non-daemon thread, meaning it will not go the user until it finishes its task. So, the counter has to be finished before it can go to the user for exiting the program. It is a non-daemon task in the background function timer().

'''
import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('Logged in for: ', count, "seconds")

x = threading.Thread(target = timer)
x.start()

# our main thread is asking user whether you want to exit and in the background there is a timer to see how long somebody is logged in.

answer = input('Do you wish to exit? ')

'''





# Example 2
# Here you introduce a daemon thread to exit the counter and go the user for exit the program. The user can easily input something to exit and the counter stops. While in the previous example, the counter was keep on going infinetly without giving a change to the user to exit.


import threading
import time

def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('Logged in for: ', count, "seconds")

x = threading.Thread(target = timer, daemon=True)
x.start()

# our main thread is asking user whether you want to exit and in the background there is a timer to see how long somebody is logged in.

answer = input('Do you wish to exit? ')
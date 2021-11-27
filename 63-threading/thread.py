# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading


'''
Thread is a separate flow of execution. Every thread has a task. Execution will be differenct in each thread. Example: spider is multitasking like flying thread, talk to aunt may thread, studying about octopus thread, talking to mj thread etc. These threads of spiderman must be done at the same time. It is doing concurrently. It is like multithreading. 

multithreading is using multiple threads in program or process.

The main importan application areas of multi threading:
1) multimedia graphics 2)animations 3) video games 4) web servers 5) application servers


'''



import threading 
import time


'''
print(threading.active_count()) #count the number of thread that are currently running at the background
print(threading.enumerate()) # the list of all threads that are running.
'''


#Example1: eat_breakfast(), drink_coffee() and study is being done sequentially.
'''
def eat_breakfast():
    time.sleep(3)
    print('You eat breakfast')

def drink_coffee():
    time.sleep(4)
    print('You drank coffee')

def study():
    time.sleep(5)
    print('You finish studying')


eat_breakfast()
drink_coffee()
study()
'''





# Example 2: We need to do it concurrently

'''

def eat_breakfast():
    time.sleep(3)
    print('You eat breakfast')

def drink_coffee():
    time.sleep(4)
    print('You drank coffee')

def study():
    time.sleep(5)
    print('You finish studying')


x = threading.Thread(target = eat_breakfast, args = ())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target = study, args = ())
z.start()


print(threading.active_count()) #count the number of thread that are currently running at the background
print(threading.enumerate()) # the list of all threads that are running.

#main thread is not in charge in executing these three functions. Three threads are created for these functions to work concurrently.
print(time.perf_counter()) # time taken by the main thread for its execution


'''



# 3. You want the main thread to wait after the three threads have executed its task


def eat_breakfast():
    time.sleep(3)
    print('You eat breakfast')

def drink_coffee():
    time.sleep(4)
    print('You drank coffee')

def study():
    time.sleep(5)
    print('You finish studying')


x = threading.Thread(target = eat_breakfast, args = ())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target = study, args = ())
z.start()

x.join()   
y.join()
z.join()

print(threading.active_count()) 

print(threading.enumerate()) 

print(time.perf_counter()) # time taken by the main thread for its execution

# you will notice that the main thread took more time than the codes in the above two examples because it has to wait for the three threads eat_breakfast, drink_coffee and study to finish executing their task.
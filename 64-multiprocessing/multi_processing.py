# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)



from multiprocessing import Process, cpu_count
import time


# we are seeing how long it takes to count from a 0 to billion in processes

def counter(num):
    count = 0
    while count < num:
        count +=1


#you need multiple process to reduce the time taken by it. So create another process named 'b' and then another 'c' to lessen its time.

def main():

    #a = Process(target=counter, args=(1000000000, ))

    print(cpu_count())
    a = Process(target=counter, args=(2500000, ))
    b = Process(target=counter, args=(2500000, ))
    c = Process(target=counter, args=(2500000, ))
    d = Process(target=counter, args=(2500000, ))

    a.start()
    b.start()
    c.start()
    d.start()

    print('Processing')

    a.join() # join is used for synchronization
    b.join()
    c.join()  
    d.join()

    print('Done')
    print('finished in: ', time.perf_counter(), 'seconds')



if __name__ == '__main__':
    main()


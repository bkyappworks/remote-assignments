import threading
from time import sleep

# import time 
# start = time.perf_counter() 

def do_job(number): 
    sleep(3)
    print(f"Job {number} finished")

# rewrite everything inside this main function and keep others untouched
def main():
    threads = []
    for t in range(1,6):
        t = threading.Thread(target = do_job, args = [t])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
main()
# finish = time.perf_counter()
# print(f'Finished in {round(finish-start, 2)} second(s)') 
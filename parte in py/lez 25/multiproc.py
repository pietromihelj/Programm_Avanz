import multiprocessing as mp
import os
import time



def f(n):
    time.sleep(2)
    print(f"{os.getpid()} ha ricevuto il valore numero {n}")


def main():
    procs = []
    for i in range(10):
        p = mp.Process(target=f, args=(i,))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()


if __name__ == '__main__':
    main()
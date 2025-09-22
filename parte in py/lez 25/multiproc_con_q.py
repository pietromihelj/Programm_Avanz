import multiprocessing as mp
import random

def make_random(q):
    q.put(random.random())
    
def sum1(q,i,n):
    q.put((i,n+1))

def main():
    lst = [1,2,3,4,5,6,7,8,9]
    q = mp.Queue()
    for i,x in enumerate(lst):
        p = mp.Process(target=sum1, args=(q,i,lst[i]))
        p.start()
    for i in enumerate(lst):
        print(f"ricevuto {q.get()}")
    
    for i in enumerate(lst):
        p.join()


if __name__ == '__main__':
    main()


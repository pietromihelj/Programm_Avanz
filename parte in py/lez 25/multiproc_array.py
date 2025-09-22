import multiprocessing as mp

def f(a,n):
    a[n] = n

def main():
    a =mp.Array('i',[0]*10)
    procs = []
    for i in range (10):
        p = mp.Process(target=f,args=(a,i))
        p.start()
    for p in procs:
        p.join()
    
    for i in range (10):
        print(f"argomento {i} = {a[i]}")

if __name__ == '__main__':
    main()
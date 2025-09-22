import multiprocessing as mp

def f(n):
    return n**2

def main():
    p = mp.Pool(processes=8)
    lst = p.map(f, range(10))
    p.close
    print(lst)
    

if __name__ == '__main__':
    main()
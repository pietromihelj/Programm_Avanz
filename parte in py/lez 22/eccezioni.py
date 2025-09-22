d = {}

try:
    d[10] = d[10]+1

except KeyError:
    print("catturato key error")
    d[10] = 0

class MyException(Exception):
    pass

class MyException_2(Exception):
    pass

try:
    raise MyException

except MyException:
    print("catturata la mia eccezione")

except Exception:
    print("catturata eccezione generica")

finally:
    print("eseguito comunque")


def f(x):
    if x<10:
        raise MyException
    else:
        return 5

def g(x):
    try: 
        f(x)
    except MyException as e:
        print("ho catturato {e}")
        e.add_note("rilanciata una seconda volta")
        raise
        

g(1)
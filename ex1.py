def acs(V1, V2, T):
    print(((V2 - V1) / T))
def decorator(f):
    def wrapper(V1, V2, T):
        f(V1, V2, T)
        print((V1 + V2)/ 2 * T)
    return wrapper

class ZeroTime(BaseException):
    pass

try:
    V1 = float(input())
    V2 = float(input())
    T = float(input())
    if T <= 0:
        raise ZeroTime("time mustn't be lower or equal zero")
except (ZeroTime, ValueError):
    print('Error in input')
else:
    acs = decorator(acs)
    acs(V1, V2, T)

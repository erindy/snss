

def fib(n):
    if n==0 or n==1:
        return n
    # memoization can be added
    return fib(n-1) + fib(n-2)


def fib_bottom_up(n):
    prev = 1    # fib(1)
    prevv = 0   # fib(0)

    for i in range(2, n+1):
        f_n = prev + prevv
        prevv = prev
        prev = f_n

    return f_n

if __name__=='__main__':
    print(fib_bottom_up(9))
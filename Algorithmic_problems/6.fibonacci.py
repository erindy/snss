import time
# f(n) = f(n-1) + f(n-2)
# f(n-1) = f(n-2) + f(n-3)
# .
# .
# f(1) = 2 # base case
# F(0) = 1 # base case


def fib_mem(n, cache={}):
    if n==2: return 2
    if n==1: return 1
    value = cache.get(n, None)
    if value:
        return value
    else:
        computed_value = fib_mem(n-1, cache) + fib_mem(n-2, cache)
        cache[n] = computed_value
        return computed_value


def fib(n):
    if n==2: return 2
    if n==1: return 1

    return fib(n-1) + fib(n-2)


def fib_bottom_up(n):
    prev = 2
    prevv = 1
    for i in range(3, n+1):
        sol = prev + prevv
        prevv = prev
        prev = sol
    return prev



if __name__=="__main__":
    # st = time.time()
    # print(fib(40))
    # et = time.time()
    #
    # print(f"execution time of fib: {et-st}")

    # st = time.time()
    # print(fib_mem(1000))
    # et = time.time()
    # print(f"execution time of fib: {et-st}")


    st = time.time()
    print(fib_bottom_up(1000))
    et = time.time()

    print(f"execution time of fib: {et - st}")
import random
def sort(A):
    for i in range(1,len(A)):
        insert(A, i, A[i])

def insert(A, idx, value):
    i = idx-1
    while i>= 0 and A[i] > value:
        A[i+1] = A[i]
        i = i-1

    A[i+1] = value





if __name__=='__main__':
    x = [random.randint(1,1000) for i in range(1000)]
    sort(x)



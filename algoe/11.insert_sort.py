def insert_sort(a):
    for i in range(len(a)):
        csort(a, i, a[i])

    return a

def csort(a, idx, current_value):
    i = idx-1
    while i>=0 and a[i]>current_value:
        a[i+1]=a[i]
        i -=1

    a[i+1] = current_value


if __name__=="__main__":
    a = [8, 5, 2, 9, 5, 6, 3]
    print(insert_sort(a))
a = [8,5,2,9,5,6,3]

def selection_sort(a):
    sub_idx = 0
    max_len = len(a)
    for i in range(max_len):


        # find smallest
        start = i
        smallest = start
        for j in range(start, max_len):
            if a[smallest] > a[j]:
                smallest = j

        # swap them
        print(a)
        a[start], a[smallest] = a[smallest], a[start]


    return a


if __name__=="__main__":
    print(selection_sort(a))




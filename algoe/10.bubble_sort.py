

def bubble_sort(a, max_length):
    swaped = False
    for i in range(max_length):
        if i+1 < max_length and a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            swaped = True

    return swaped


def main_bubble_sort(a):
    max_length = len(a)
    swaped = True
    while swaped and (max_length > 1):
        swaped = bubble_sort(a, max_length)
        max_length -= 1

    return a


if __name__=="__main__":
    a = [8, 5, 2, 9, 5, 6, 3]
    print(main_bubble_sort(a))
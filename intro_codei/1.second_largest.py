list1 = [1, 3, 4, 7, 0, 2, 5]
list2 = [1, 3, 5, 5, 0, 2]
list3 = []
list4 = [1,]

def second_largest(n):
    if len(n) < 2:
        return None

    max = 0
    second_max = 0
    for item in n:
        if item>max:
            second_max = max
            max=item
        elif item==max:
            max=item

        elif item<max and item>second_max:
            second_max = item
        else:
            pass

    return second_max


if __name__=="__main__":
    print(second_largest(list1))
    print(second_largest(list2))
    print(second_largest(list3))
    print(second_largest(list4))
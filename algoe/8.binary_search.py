array_bist =  [0 , 1, 21, 33, 45, 45, 61, 71, 72, 73]


# recursive
def binary_search_rec(array, search_item):
    array_len = len(array)
    if array_len == 1 and array[0]==search_item:
        return True
    if array_len == 1 and array[0]!=search_item:
        return False
    elif array_len==0:
        return False


    n_2 = array_len // 2

    if array[n_2] > search_item:
        res = binary_search_rec(array[:n_2], search_item)
    elif array[n_2] < search_item:
        res = binary_search_rec(array[n_2:], search_item)

    else:
        return True

    return res


def binary_search(array, search_item):
    array_len = len(array)

    n_2 = array_len//2

    while array_len > 1:

        if array[n_2] > search_item:
            array = array[:n_2]
        elif array[n_2]<search_item:
            array = array[n_2:]
        else:
            return True

        array_len = len(array)
        n_2 = array_len // 2

    if array[0] == search_item : return True

    return False


if __name__=='__main__':
    print(binary_search_rec(array_bist, 0))




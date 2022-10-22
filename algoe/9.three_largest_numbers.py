array_bist = [141, 1, 17, -7, -17, -37, 18, 541, 6,7,8]

def max_n_largest(array: list):
    n_array = 3*[None]

    for item in array:
        process_helper(item, n_array)

    return n_array


def process_helper(num, n_array):
    if n_array[2] is None or n_array[2]<num:
        shifter(num, n_array, 2)
    elif n_array[1] is None or n_array[1]<num:
        shifter(num, n_array, 1)
    elif n_array[0] is None or n_array[0]<num:
        shifter(num, n_array, 0)
    else:
        pass

    return n_array

def shifter(num, n_array, idx):

    for i in range(3):
        if idx == i:
            n_array[i] = num
        elif idx < i:
            pass
        else:
            n_array[i] = n_array[i+1]


if __name__ == '__main__':
    print(max_n_largest(array_bist))
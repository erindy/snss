array = [2,1,2,2,2,3,4,2]

def move_element_to_end(array, element):
    left  = 0
    right = len(array) - 1

    while left != right:
        if array[right] == element:
            right -= 1
        elif array[left] != element:
            left += 1

        else: #right != element and left == element:
            array[left], array[right] = array[right], array[left]
            right -= 1
            left += 1


    return array


if __name__=="__main__":
    print(move_element_to_end(array, 2))
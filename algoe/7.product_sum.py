test_array = [5,2, [7, -1], 3, [6, [-13, 8], 4]]


# O(n) time | O(d) space
def sum(array, depth=1):
    total_sum = 0
    for item in array:
        if type(item) is list:
            total_sum = total_sum + sum(item, depth+1)
        else:

            total_sum = total_sum + item

    return total_sum * depth


if __name__=='__main__':
    print(sum(test_array))
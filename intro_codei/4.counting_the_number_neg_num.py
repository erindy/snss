input = [[-4, -3, -1, 1],
         [-2, -2, 1, 2],
         [-1, 1, 2, 3],
         [1, 2, 4, 5]]

def count_negative_numbers(input)-> int:
    total_negatives = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if input[i][j] <0:
                total_negatives += 1

    return total_negatives


def count_negative_numbers_1(input) -> int:
    total_negatives = 0
    offset = 0
    for i in range(len(input)):
        for j in range(len(input)-1-offset, -1, -1):
            if input[i][j] <0:
                total_negatives = j + 1 + total_negatives
                offset = len(input)-j
                break

    return total_negatives


if __name__=="__main__":
    print(count_negative_numbers_1(input))

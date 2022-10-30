def find_duplicate(input_array):
    mapper = {}
    for number in input_array:
        exists = mapper.get(number, False)
        if exists:
            return number
        else:
            mapper[number] = True

    return False


def tortoise_hare():
    pass

if __name__=="__main__":
    print(find_duplicate([2,3,5,6,7,8,2]))
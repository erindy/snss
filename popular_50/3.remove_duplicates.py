def remove_duplicates(input_array: list) -> list:
    array_mapper = {}
    for item in input_array:
        array_mapper[item] = True

    return list(array_mapper.keys())




if __name__=="__main__":
    input_array = [3, 4, 5, 6, 7,7,8,9,43,1,3,4]
    print(remove_duplicates(input_array))
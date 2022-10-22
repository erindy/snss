input_list = [3,4,1,2,9]

def adds_10(input_list) -> tuple:

    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if j==i:
                continue

            if (input_list[i] + input_list[j]) == 10:
                return (input_list[i],input_list[j])

    print("None was found")

def adds_10_1(input_list):
    save_dict = {}
    for item in input_list:

        search_item = 10-item
        res = save_dict.get(search_item, None)
        if res!=None:
            return (item, search_item)
        save_dict[item] = 1




if __name__=="__main__":
    print(adds_10_1(input_list))



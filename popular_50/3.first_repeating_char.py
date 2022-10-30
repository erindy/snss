

def repeating_char(input_char):
    char_mapper = {}
    for char in input_char:
        exits = char_mapper.get(char, False)
        if not exits:
            char_mapper[char] = True
        else:
            return char

    return "\0"




if __name__=="__main__":
    print(repeating_char("testing"))
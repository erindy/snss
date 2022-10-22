input = [[0,1,0,0],
         [0,0,1,0],
         [0,0,0,0],
         [0,1,0,1],
         ]



def rooks_are_safe(input)->True:
    # get the size
    n_length = len(input)
    for i in range(n_length):
        found_horizontally = []
        for j in range(n_length):
            res = bool(input[i][j])
            if res:
                found_horizontally.append((i,j))
            if len(found_horizontally)>1:
                return True

    for i in range(n_length):
        found_vertically = []
        for j in range(n_length):
            res = bool(input[j][i])
            if res:
                found_vertically.append((j,i))
            if len(found_vertically)>1:
                return True

    return False




if __name__=="__main__":
    print(rooks_are_safe(input))
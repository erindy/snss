a = "3325"
b = "3325"

def larger_than(a, b):
    if (not a.isdecimal()) or (not b.isdecimal()):
        return False

    if len(a)>len(b):
        return True
    elif len(b)<len(a):
        return False
    else:
        for index in range(len(a)):
            if a[index]>b[index]:
                return True
            elif a[index]<b[index]:
                return False
            else:
                continue
        return False


if __name__=="__main__":
    print(larger_than(a, b))
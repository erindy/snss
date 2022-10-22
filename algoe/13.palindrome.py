a = "abcdcba"

def is_palindrome(a):
    left = 0
    right = len(a) - 1

    while left < right:
        if a[left] != a[right]:
            return False

        left += 1
        right -= 1

    return True


def is_pal_rec(a):
    if len(a) == 1: return True
    if len(a) == 0: return True

    first = a[0]
    last = a[-1]
    if first == last:
        return is_palindrome(a[1:-1])
    else:
        return False


if __name__=="__main__":
    print(is_pal_rec("abcdcba"))
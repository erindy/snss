
def merge_sort(A):
    # base case
    if len(A) < 2: return A

    mid = len(A)//2

    right = merge_sort(A[mid:]) # j
    left = merge_sort(A[:mid]) # i

    i = j = 0
    B = []

    while len(A)>len(B):
        if j >= len(right) or i < mid and left[i] < right[j]:
            B.append(left[i])
            i += 1
        elif j < len(right):
            B.append(right[j])
            j += 1

    return B


if __name__=="__main__":
    a = [2, 4, 1, 3, 6, 5]
    print(merge_sort(a))
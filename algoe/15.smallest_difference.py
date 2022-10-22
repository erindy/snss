
a = [-1, 5, 10, 20, 28,3]
b = [26, 134, 135, 15, 17]

# c = [3, 5, 7]
# b = [-1, 8, 9]

# take the largest in one array, compare it with the one in the other array, take the difference

# brute force

def smallest_brute_difference( a, b):
    # sort arrays first
    # assuming the sorting is done in nlogn
    min = 1000
    min_pair = ()
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if abs(a[i] - b[j]) < min:
                min_pair = (a[i], b[j])
                min = abs(a[i] - b[j])


    return min_pair

def smallest_difference(a, b):
    a.sort()
    print(a)
    b.sort()

    idx_a = 0
    idx_b = 0
    min = float("inf")
    min_pair = None

    while idx_a<len(a) and idx_b<len(b):
        dist = abs(a[idx_a] - b[idx_b])
        if dist>min:
            pass


        else:

            min_pair = [a[idx_a], b[idx_b]]
            min = dist

        if a[idx_a] < b[idx_b]:
            idx_a += 1
        elif a[idx_a] > b[idx_b]:
            idx_b += 1
        else:
            return [a[idx_a], b[idx_b]]


    return min_pair






if __name__ == "__main__":
    print(smallest_difference(a,b))
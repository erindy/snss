initial_array = [3,5,-4,8,11,1,-1,6]
target_sum = 10

# brute force
# complexity is O(n^2)
def brute_force(initial_array, target_sum):
    for item in initial_array:
        for item_2 in initial_array:
            if item_2==item:
                pass
            else:

                if target_sum == item_2 + item:
                    print(item, item_2)
                    return (item, item_2)


def hash_table_sol(initial_array, target_sum):

    hash_table = {}
    for item in initial_array:
        find_item = target_sum - item
        if item in hash_table.keys():
            return (find_item, item)
        else:
            hash_table[find_item] = item


# sorted example
#  initial_array = [3,5,-4,8,11,1,-1,6]


def hash_table_sol_1(initial_array, target_sum):
    hash_table = {}
    for item in initial_array:
        target_item = target_sum - item
        if target_item in hash_table.keys():
            return (item, target_item)
        else:
            hash_table[item] = True  # means that I have looked once for this item but not found anything


#  sorted_array = [-4, -1, 1, 3, 5, 6, 8, 11]
# move left pointer if I need to increase the sum
# move the right pointer i I need to decrease the sum
def sorting_sol(initial_array, target):
    initial_array.sort() # we would use a binary sort to obtain a complexity of nlogn
    l_pointer = 0
    len_array = len(initial_array)
    r_pointer = len_array -1
    while r_pointer>l_pointer:
        sum = initial_array[l_pointer] + initial_array[r_pointer]
        if sum == target:
            return (initial_array[l_pointer], initial_array[r_pointer])
        if sum > target:
            r_pointer -=1
        else:
            l_pointer += 1













def test_brute_force():
    res = brute_force(initial_array, target_sum)

def test_hash_table_sol():
    return hash_table_sol(initial_array, target_sum)

if __name__=='__main__':
    print(sorting_sol(initial_array, target_sum))

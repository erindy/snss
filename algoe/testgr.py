# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

import random, string

alpha= ['a', 'b', 'c', 'd', 'f', 'e', 'g', 'h', 'i', 'j']
def get_random_letter_excl(excluded_letter_prev, excluded_letter_next):
    letter = random.choice(alpha)
    if excluded_letter_prev == letter or excluded_letter_next == letter or letter == '0':
        letter = get_random_letter_excl(excluded_letter_prev, excluded_letter_next)
    else:
        return letter
    return letter


def solution(riddle):
    # write your code in Python 3.6
    new_letter_list = []
    for i in range(0, len(riddle)):
        if riddle[i] == '?':
            # do something
            # look at the previous result
            if i == 0:
                prev = ''
                rand = get_random_letter_excl(prev, riddle[i + 1])

                # riddle[i] = rand
                new_letter_list.append(rand)
                # print(new_letter_list)
            elif len(riddle) - 1 == i:
                rand = get_random_letter_excl(new_letter_list[-1], '')

                # riddle[i] = rand
                new_letter_list.append(rand)
                # print(new_letter_list)
            else:
                rand = get_random_letter_excl(new_letter_list[-1], riddle[i + 1])

                # riddle[i] = rand
                new_letter_list.append(rand)
                # print(new_letter_list)
            # look at the next
            # pick an alphanumeric letter
        else:
            new_letter_list.append(riddle[i])

    new_word = ''.join(new_letter_list)
    print(new_word)
    return new_word

def findLeastNumOfUniqueIntss( arr: list, k: int) -> int:
    mapper = {}
    for item in arr:
        res = mapper.get(item, 'empty')
        if res == 'empty':
            mapper[item] = 1
        else:
            mapper[item] += 1

    limit = 2
    k_count = 0
    find = False
    for limit in range(1, 100000):
        ranked = dict((k, v) for k, v in mapper.items() if v == limit)
        for key in ranked.keys():
            for j in range(0,ranked[key]):
                arr.remove(key)
                mapper[key] -= 1
                k_count += 1
                if k_count == k:
                    find = True
                    break
            if find == True:
                break
        if find == True:
            break

    final_list = dict((k, v) for k, v in mapper.items() if v > 0)
    total_count = len(final_list.keys())

    return total_count

def findLeastNumOfUniqueInts(arr: list, k: int) -> int:
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 0
        d[i] += 1
    l = list(d.values())
    l.sort()
    for i in range(len(l)):
        if l[i] <= k:
            k -= l[i]
            l[i] = -1
        else:
            break
    co = 0
    for i in l:
        if i != -1:
            co += 1
    return co

if __name__ == '__main__':
    print(findLeastNumOfUniqueInts(
[2,1,1,1,3,3,3], 3))


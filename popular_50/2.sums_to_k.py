a = [3, 4,6, 8]
def find_pair(a, k):
    dict_tracker = {}

    for item in a:

        corr_item = k - item
        if dict_tracker.get(corr_item, False):
            return (item, corr_item)

        else:
            dict_tracker[item] = True

    return False

if __name__=="__main__":
    print(find_pair(a, 41))
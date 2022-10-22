from binarytree import build

# def helper_rec(root):
#     # base case
#     if (root.left == None) and (root.right == None):
#         return root.value
#
#
#     # recursive call
#     if (root.left != None) and (root.right != None):
#         res_sum = helper_rec(root.left) + helper_rec(root.right) + root.value
#     elif (root.left != None) and (root.right == None):
#         res_sum = helper_rec(root.left) + root.value
#     elif (root.left == None) and (root.right != None):
#         res_sum = helper_rec(root.right) + root.value
#     else: 
#         print("unexpected path")
#
#
#     return res_sum

def helper_rec(root, sum, sum_list):
    if (root.left is None) and (root.right is None):
        sum = sum + root.value
        sum_list.append(sum)

    if (root.right is None) and (root.left is not None):
        sum = sum + root.value
        helper_rec(root.left, sum, sum_list)
    elif (root.right is not None) and (root.left is None):
        sum = sum + root.value
        helper_rec(root.right, sum, sum_list)

    elif (root.right is not None) and (root.left is not None):
        sum = sum + root.value
        helper_rec(root.right, sum, sum_list)
        helper_rec(root.left, sum, sum_list)

    return sum_list






def run():
    values = [1,2,3,4,5,6,7,8,9,10]
    root = build(values)
    print(root)

    print("my solution is: ", helper_rec(root, 0, []))


if __name__=='__main__':
    run()
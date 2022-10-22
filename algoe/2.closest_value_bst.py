from binarytree import tree, bst, heap
from binarytree import build


def find_closest_value_bst(tree, target):
    distance = float("inf")

    closest = helper_closest(tree, target, distance)
    return closest


def helper_closest(node, target, distance):
    if node is None:
        return distance + target


    new_distance = abs(target - node.value)
    if new_distance >= distance:
        pass
    elif new_distance < distance:
        distance = new_distance
    else:
        # base case
        return node.value

    # base case


    if node.value == target:
        # closest = node.value
        # closest_pointer = closest
        return node.value
    elif node.value > target:
        # update the value if needed
        # new_distance = abs(closest - node.value)
        return helper_closest(node.left, target, distance)
    elif node.value < target:
        return helper_closest(node.right, target, distance)




# new solution
def findClosestValueInBst(tree, target):
    return findClosestHelper(tree, target, float( "inf"))

def findClosestHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target-closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosestHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestHelper(tree.right, target, closest)
    else:
        return closest


def findClosestIt(tree, target):
    return findClosestItHelper(tree, target, float('inf'))

def findClosestItHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            return  closest

if __name__ == "__main__":
    # bt = BT()
    # bt.insert(10)
    # bt.insert(5)
    # bt.insert(15)
    # bt.insert(2)
    # bt.insert(5)
    # bt.insert(1)
    # bt.insert(13)
    # bt.insert(22)
    # bt.insert(14)

    values = [10, 5, 15, 2, 5, 13, 14, 11,  22,  1]
    root = build(values)
    print(root)

    print("algo solution: ", findClosestValueInBst(root, 12))
    print("my solution: ", find_closest_value_bst(root, 12))





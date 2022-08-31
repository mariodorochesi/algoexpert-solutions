def recursive_search(tree, target, closest_value):

    # Base case when there is no left or right node
    if tree is None:
        return closest_value

    if abs(target - tree.value) < abs(target - closest_value):
        closest_value = tree.value

    if target > tree.value:
        return recursive_search(tree.right, target, closest_value)
    elif target < tree.value:
        return recursive_search(tree.left, target, closest_value)
    return closest_value

def findClosestValueInBst(tree, target):

    return recursive_search(tree, target, float('inf'))


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

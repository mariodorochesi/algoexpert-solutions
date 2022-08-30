def twoNumberSum(array, target_sum):
    complement_set = set()
    for i in array:
        if i in complement_set:
            return [i, target_sum-i]
        complement_set.add(target_sum - i)
    return []

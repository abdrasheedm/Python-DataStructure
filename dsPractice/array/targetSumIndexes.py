nums = [1, 3, 5, 6, 7]
target = 8


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_indices = set() # Dictionary to store the indices of elements

    for num in nums:
        compliment = target - num
        if compliment in num_indices:
            return [nums.index(compliment), nums.index(num)]
        num_indices.add(num)
print(twoSum(nums, target))
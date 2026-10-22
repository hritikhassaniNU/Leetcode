def twoSum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):

            total = nums[i] + nums[j]

            if total == target:
                return [i, j]

    return []
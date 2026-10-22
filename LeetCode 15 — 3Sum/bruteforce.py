def threeSum(nums):
    unique = set()
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    triplet = tuple(sorted([
                        nums[i], nums[j], nums[k]
                    ]))

                    unique.add(triplet)

    return [list(t) for t in sorted(unique)]


nums = [-1, 0, 1, 2, -1, -4]

print(threeSum(nums))
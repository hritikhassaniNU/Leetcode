def threeSum(nums):
    result = set()
    n = len(nums)

    for i in range(n - 2):
        seen = set()

        for j in range(i + 1, n):
            needed = -nums[i] - nums[j]

            if needed in seen:
                triplet = tuple(sorted(
                    [nums[i], nums[j], needed]
                ))
                result.add(triplet)

            seen.add(nums[j])

    return [list(t) for t in sorted(result)]
def longestConsecutive(nums):
    longest = 0

    for num in nums:
        current = num
        length = 0

        while current in nums:
            length += 1
            current += 1

        longest = max(longest, length)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
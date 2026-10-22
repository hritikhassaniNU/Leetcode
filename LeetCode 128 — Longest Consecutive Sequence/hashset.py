def longestConsecutive(nums):
    numbers = set(nums)
    longest = 0

    for num in numbers:

        # Only start at the beginning of a sequence
        if num - 1 not in numbers:
            current = num
            length = 1

            # Keep searching for the next number
            while current + 1 in numbers:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


nums = [100, 4, 200, 1, 3, 2]

print(longestConsecutive(nums))
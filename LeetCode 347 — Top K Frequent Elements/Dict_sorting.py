def topKFrequent(nums, k):
    counts = {}

    # Step 1: Count frequencies
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Step 2: Sort by frequency
    pairs = sorted(
        counts.items(),
        key=lambda pair: pair[1],
        reverse=True
    )

    # Step 3: Select top k numbers
    result = []

    for i in range(k):
        result.append(pairs[i][0])

    return result


nums = [1, 1, 1, 2, 2, 3]
print(topKFrequent(nums, 2))
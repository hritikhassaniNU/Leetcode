def topKFrequent(nums, k):
    counts = {}

    # Step 1: Count frequencies
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Step 2: Create frequency buckets
    buckets = [[] for _ in range(len(nums) + 1)]

    # Step 3: Place numbers into buckets
    for num, freq in counts.items():
        buckets[freq].append(num)

    # Step 4: Read highest frequencies first
    result = []

    for freq in range(len(nums), 0, -1):
        for num in buckets[freq]:
            result.append(num)

            if len(result) == k:
                return result

    return result
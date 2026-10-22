def productExceptSelf(nums):
    n = len(nums)

    prefix = [1] * n
    suffix = [1] * n

    # Calculate left-side products
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    # Calculate right-side products
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    # Combine both products
    result = []

    for i in range(n):
        result.append(prefix[i] * suffix[i])

    return result


def productExceptSelf(nums):
    n = len(nums)

    result = [1] * n
    prefix = 1

    # Left to right
    for i in range(n):
        result[i] = prefix
        prefix = prefix * nums[i]

    suffix = 1

    # Right to left
    for i in range(n - 1, -1, -1):
        result[i] = result[i] * suffix
        suffix = suffix * nums[i]

    return result
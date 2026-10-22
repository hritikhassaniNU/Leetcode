def productExceptSelf(nums):
    n = len(nums)
    result = []

    for i in range(n):
        product = 1
      

        for j in range(n):
            if i == j:
                continue

            product = product * nums[j]

        result.append(product)

    return result


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
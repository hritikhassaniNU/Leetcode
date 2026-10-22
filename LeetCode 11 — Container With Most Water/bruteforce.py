def maxArea(height):
    n = len(height)
    best = 0

    for left in range(n):
        for right in range(left + 1, n):
            width = right - left

            water_height = min(
                height[left], height[right]
            )

            area = width * water_height

            best = max(best, area)

    return best


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
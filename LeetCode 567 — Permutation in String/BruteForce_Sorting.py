def checkInclusion(s1, s2):
    m = len(s1)
    n = len(s2)

    if m > n:
        return False

    target = sorted(s1)

    for left in range(n - m + 1):
        right = left + m

        window = s2[left:right]

        if sorted(window) == target:
            return True

    return False
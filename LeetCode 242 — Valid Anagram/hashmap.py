def isAnagram(s, t):
    if len(s) != len(t):
        return False

    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if counts.get(char, 0) == 0:
            return False

        counts[char] -= 1

    return True
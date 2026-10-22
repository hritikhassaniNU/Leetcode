def lengthOfLongestSubstring(s):
    longest = 0
    n = len(s)

    for i in range(n):
        for j in range(i, n):

            seen = set()
            unique = True

            for k in range(i, j + 1):
                if s[k] in seen:
                    unique = False
                    break

                seen.add(s[k])

            if unique:
                length = j - i + 1
                longest = max(longest, length)

    return longest
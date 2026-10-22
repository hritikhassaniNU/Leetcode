def characterReplacement(s, k):
    n = len(s)
    longest = 0

    for left in range(n):
        for right in range(left, n):

            freq = {}

            for i in range(left, right + 1):
                char = s[i]
                freq[char] = freq.get(char, 0) + 1

            maxFreq = max(freq.values())
            windowLength = right - left + 1

            replacements = windowLength - maxFreq

            if replacements <= k:
                longest = max(longest, windowLength)

    return longest
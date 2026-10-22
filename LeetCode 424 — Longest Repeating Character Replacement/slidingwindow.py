def characterReplacement(s, k):
    freq = {}
    left = 0
    maxFreq = 0
    longest = 0

    for right in range(len(s)):
        char = s[right]

        freq[char] = freq.get(char, 0) + 1

        maxFreq = max(maxFreq, freq[char])

        if (right - left + 1) - maxFreq > k:
            freq[s[left]] -= 1
            left += 1

        longest = max(longest, right - left + 1)

    return longest
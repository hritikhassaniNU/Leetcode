def characterReplacement(s, k):
    freq = {}
    left = 0
    longest = 0

    for right in range(len(s)):
        char = s[right]

        freq[char] = freq.get(char, 0) + 1

        while (
            right - left + 1 - max(freq.values()) > k
        ):
            leftChar = s[left]
            freq[leftChar] -= 1

            if freq[leftChar] == 0:
                del freq[leftChar]

            left += 1

        longest = max(longest, right - left + 1)

    return longest
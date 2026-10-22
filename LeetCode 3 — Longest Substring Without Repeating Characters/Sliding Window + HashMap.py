def lengthOfLongestSubstring(s):
    last_seen = {}
    left = 0
    longest = 0

    for right, char in enumerate(s):

        if char in last_seen:
            left = max(left, last_seen[char] + 1)

        last_seen[char] = right

        length = right - left + 1
        longest = max(longest, length)

    return longest
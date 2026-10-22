def checkInclusion(s1, s2):
    m = len(s1)

    if m > len(s2):
        return False

    need = {}
    window = {}

    for char in s1:
        need[char] = need.get(char, 0) + 1

    for i in range(m):
        char = s2[i]
        window[char] = window.get(char, 0) + 1

    if need == window:
        return True

    for right in range(m, len(s2)):
        outgoing = s2[right - m]

        window[outgoing] -= 1

        if window[outgoing] == 0:
            del window[outgoing]

        incoming = s2[right]
        window[incoming] = window.get(incoming, 0) + 1

        if need == window:
            return True

    return False
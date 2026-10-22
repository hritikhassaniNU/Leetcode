def isPalindrome(s):
    chars = []

    for char in s:
        if char.isalnum():
            chars.append(char.lower())

    cleaned = "".join(chars)
    reversed_text = cleaned[::-1]

    return cleaned == reversed_text


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))
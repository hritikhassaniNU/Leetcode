def isValid(s):
    stack = []

    matching = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:

        if char in "([{":
            stack.append(char)

        else:
            if not stack:
                return False

            last_open = stack.pop()

            if last_open != matching[char]:
                return False

    return len(stack) == 0
def isValid(s):
    while True:
        updated = s.replace("()", "")
        updated = updated.replace("[]", "")
        updated = updated.replace("{}", "")

        if updated == s:
            break

        s = updated

    return s == ""
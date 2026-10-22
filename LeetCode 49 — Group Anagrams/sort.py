def groupAnagrams(strs):
    groups = {}

    for i, word in enumerate(strs):
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())
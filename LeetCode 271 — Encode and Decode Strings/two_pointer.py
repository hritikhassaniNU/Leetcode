class Codec:
    def encode(self, strs):
        pieces = []

        for word in strs:
            length = len(word)
            piece = str(length) + "#" + word
            pieces.append(piece)

        return "".join(pieces)

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            word = s[start:end]
            result.append(word)

            i = end

        return result


codec = Codec()

words = ["hello", "world", "python"]

encoded = codec.encode(words)
print(encoded)

decoded = codec.decode(encoded)
print(decoded)
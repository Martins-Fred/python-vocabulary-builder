def build_vocabulary(tokens):
    """Give every distinct word a number."""

    vocabulary = {}

    for word in tokens:
        if word not in vocabulary:
            vocabulary[word] = len(vocabulary) 

    return vocabulary


print(build_vocabulary(["the", "cat", "the", "sat"]))
print(build_vocabulary([]))
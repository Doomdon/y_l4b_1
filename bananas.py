import itertools

def bananas(s) -> set:
    result = set(itertools.combinations(s, len(s)))
    strstr = [str(item) for item in itertools.chain(result)]
    return "".join(strstr)


print((bananas("banana")))
print(bananas("bbananana"))

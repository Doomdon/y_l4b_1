import math


def count_find_num(primesL, limit):
    if math.prod(primesL) > limit:
        return []

    array_num = [math.prod(primesL)]

    for prime in primesL:
        for n in array_num:
            if n * prime > limit:
                continue
            array_num.append(n * prime)
    return [len(array_num), max(array_num)]


# тесты
primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]
print(count_find_num(primesL, limit))
primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]
print(count_find_num(primesL, limit))
primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]
print(count_find_num(primesL, limit))
primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]
print(count_find_num(primesL, limit))
primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
print(count_find_num(primesL, limit))

# import re
#
#
# def zeros(n):
#     factorial = 1
#     while n > 1:
#         factorial *= n
#         n -= 1
#     res = re.search(r"0+\b", str(factorial))
#
#     return len(res.group(0)) if res else 0
def zeros(n):
    if n < 5:
        return 0
    else:
        return n//5 + zeros(n//5)




#тесты
assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7

print(zeros(0))
print(zeros(6))
print(zeros(30))
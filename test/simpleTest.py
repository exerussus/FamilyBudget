
from functools import reduce


def check_if_exists(first, second):
    return reduce(lambda x, y: x or y, map(lambda x: x in second, first), False)


list1 = [1, 2, 3, 4]
list2 = [0, 5, 6, 8]

result = check_if_exists(list1, list2)
print(result)

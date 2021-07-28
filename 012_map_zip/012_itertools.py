# ! ---- # ---- # ---- # ---- # ---- # ----
'''
ITERTOOLS
'''
# ! ---- # ---- # ---- # ---- # ---- # ----
# ! ·
# ! ·
# ! ---- # ---- # ---- # ---- # ---- # ----
import itertools
import itertools as itl
# ! ---- # ---- # ---- # ---- # ---- # ----
# ! ·
# ! ·
# ! ---- # ---- # ---- # ---- # ---- # ----
'''EXAMPLE COUNTER'''
# ! ---- # ---- # ---- # ---- # ---- # ----
# counter = itl.count()
# print(counter)
# next(counter)
# print(counter)
# ! ---- # ---- # ---- # ---- # ---- # ----
# itl.count(start=5, step=5)
# ! ---- # ---- # ---- # ---- # ---- # ----
# counter = itl.cycle([1,2,3,4,5])
# ! ---- # ---- # ---- # ---- # ---- # ----
# counter = itl.repeat(2, times=5)
# ! ---- # ---- # ---- # ---- # ---- # ----
# ! ---- # ---- # ---- # ---- # ---- # ----
# def squares(x, y):
#     return x ** y
# ! ---- # ---- # ---- # ---- # ---- # ----
# result = map(squares, range(1,11))
# print(list(result))
# result2 = itl.starmap(squares, [(1, 2),(2, 2),(5, 4)])
# print(list(result2))

# ! ---- # ---- # ---- # ---- # ---- # ----

# letters = ['a', 'b', 'c', 'd']
# numbers = [1, 2, 3, 4]
# names = ['Jack', 'John']
# ! ---- # ---- # ---- # ---- # ---- # ----
# result = itl.combinations(letters, 2)
# for x in result:
#     print(x)
# ! ---- # ---- # ---- # ---- # ---- # ----
# result2 = itl.permutations(letters,2)
# for x in result2:
#     print(x)
# ! ---- # ---- # ---- # ---- # ---- # ----
# result3 = itl.product(letters,repeat=2)
# for x in result3:
#     print(x)
# ! ---- # ---- # ---- # ---- # ---- # ----
# result4 = itl.combinations_with_replacement(letters, 2)
# for x in result4:
#     print(x)
# ! ---- # ---- # ---- # ---- # ---- # ----
# result5 = itl.chain(letters, numbers)
# print(list(result5))
# for x in result5:
#     print(list(x))
# ! ---- # ---- # ---- # ---- # ---- # ----
# with open('logs.txt', 'r', encoding='UTF8') as file:
#     log_header = itl.islice(file,3)
#
#     for line in log_header:
#         print(line, end='')
# ! ---- # ---- # ---- # ---- # ---- # ----
# numbers2 = [4,5,4,3,2,1,0,4]
# selectors = [True, False, False, True]
#
# def more_than_two(x):
#     if x > 2:
#         return True
#     return False
# ! ---- # ---- # ---- # ---- # ---- # ----
# result = itl.compress(letters,selectors)
# for x in result:
#     print(x)
# ! ---- # ---- # ---- # ---- # ---- # ----
# result = filter(more_than_two, numbers2)
# for x in result:
#     print(x)
# ! ---- # ---- # ---- # ---- # ---- # ----
# result2 = itl.filterfalse(more_than_two,numbers2)
# for x in result2:
#     print(x)
# # ! ---- # ---- # ---- # ---- # ---- # ----
''' Массивы Питона '''
'''
List - Allows duplicate members, Changeable, square brackets[]
Tuple - Allows duplicate members, not changeable, round brackets()
Dictionary - No duplicate members, Changeable, indexed, Unordered, curly brackets{}
Set - No duplicate members. cannot be changeable, but can be added, curly brackets{}
'''
''' LIST EXAMPLES '''
# empty_list = [123,25.333,"Type of Symbols", True, None, [12, 29]]
# print(empty_list[5][1])

courses = ["History", 'Math', 'Literature', 'Physics', 'Programming']
courses2 = ['Art', 'Chemistry']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 1, 1]

''' ADD INTO LIST '''
# courses.append('English Courses')
''' INSERT INTO LIST '''
# courses.insert(2, 'Art')
''' EXTEND INTO LIST '''
# courses.extend(courses2)
''' REMOVE SOMETHING IN LIST '''
# courses.remove('Math')
''' POP SOMETHING IN LIST '''
# courses.pop(2)
''' REVERSE LIST '''
# print(courses.reverse())
''' SORTING LIST '''
# numbers.sort(reverse=True)
# courses.sort
# print(sorted(courses))
''' MINIMAL\MAX\SUM LIST '''
# print(min(courses))
# print(max(courses))
# print(sum(numbers))
''' COUNT LIST '''
# print(numbers.count(1))
''' INDEX LIST '''
# print(courses.index('Math'))
''' IN - LIST '''
# print('Math' in courses)
''' JOIN IN LIST '''
# some_string = 'Hello world, how are you?'
# print('|'.join(courses))
''' REPLACE DATA IN LIST '''
# courses[1] = 'English'
''' COPY LIST '''
# new_courses = courses.copy()
# courses[1] = 'English'
# print(new_courses)
# print(courses)


''' TUPLES  '''
# print(courses.count('Math'))
# print(courses.index("Math"))
''' CONVERT '''
# courses = list(courses)
# courses.pop()
# courses = tuple(courses)
# print(courses)


''' SETS '''
first_set = {"History", 'Math', 'Literature', 'Physics', 'Programming'}
second_set = {'History', 'Math'}

# print(first_set.intersection(second_set))
# print(first_set.difference(second_set))
# print(first_set.union(second_set))

# print(first_set.issuperset(second_set))
# print(second_set.issubset(first_set))

''' LOOP '''

# for course in first_set:
#     print(course)

# for number in range(1,100):
#     print(number ** 2)

# for num1 in range(0,10):
#     for num2 in range(0, 10):
#         for num3 in range(0, 10):
#             for num4 in range(0, 10):
#                 print(num1, num2, num3, num4)

# for num in range(0, 1000):
#     if num % 2 == 0:
#         print(num, 'is even')
#     else:
#         print(num, 'is odd')
#     if num % 10 == 0:
#         print(num, "can be divided by 10")
# indexOfNum = 0
# print("----------------------------")
# for indexNum in courses:
#     print(str(indexOfNum) + ':' + indexNum )
#     indexOfNum = indexOfNum + 1
#     print("----------------------------")

# new_dict = { 'name': 'Roman'}

some_list = [["name", "Roman"], ["surname", "Kutselepa"]]
for key, value in some_list:
    print(key + ': ' + value)
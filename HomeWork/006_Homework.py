s = input().split()

max_count = 0
new_list = []

for num in s:
    if s.count(num) > max_count:
        max_count = s.count(num)

for num in s:
    if s.count(num) == max_count:
        new_list.append(num)

new_list = list(set(new_list))

print(new_list)
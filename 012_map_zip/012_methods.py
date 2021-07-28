import random as rnd


'''
ZIP AND MAP METHODS
'''

# ---- # ---- # ---- # ---- # ---- # ----
''' ZIPPING FILES '''
# ---- # ---- # ---- # ---- # ---- # ----
# data1 = [100,200,300,400,500,600,700]
# data2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#
# print(list(zip(data1,data2)))
# ---- # ---- # ---- # ---- # ---- # ----

# ---- # ---- # ---- # ---- # ---- # ----
''' ZIPPING FILES WITH RANGE '''
# ---- # ---- # ---- # ---- # ---- # ----
# data1 = [100,200,300,400,500,600,700]
# data2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#
# zipped_list = zip(data1, data2, range(1, 15))
# print(list(zipped_list))
# ---- # ---- # ---- # ---- # ---- # ----

# ---- # ---- # ---- # ---- # ---- # ----
''' ZIPPING FILES WITH FOR LOOP '''
# ---- # ---- # ---- # ---- # ---- # ----
# data1 = [100,200,300,400,500,600,700]
# data2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#
# zipped_list = zip(data2, range(1, 15))
#
# for a, b in zipped_list:
#     print(a)
#     print(b)
# ---- # ---- # ---- # ---- # ---- # ----

# ---- # ---- # ---- # ---- # ---- # ----
''' ZIPPING FILES WITH RANDOM '''
# ---- # ---- # ---- # ---- # ---- # ----
# data2 = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
# num_list = []
# cnt = 0
# while cnt < 7:
#     num_list.append(rnd.randint(1,100))
#     cnt += 1
# zipped_list = zip(data2, num_list)
#
# for a, b in zipped_list:
#     print(a)
#     print(b)
# ---- # ---- # ---- # ---- # ---- # ----

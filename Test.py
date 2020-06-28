import os
import sys
# import kivy
from _datetime import datetime

def time(func):
    def wrapper():
        start = datetime.now()
        result= func()
        print(datetime.now() - start)
        return result
    return wrapper
# 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_five=[less for less in a if less<5]
print(less_five)

# 2
@time
def func():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [i for i in a if i in b]
    return  list(c)

print(func())
#3

dictionary={
   'a':  12,
   'b': 42,
   'c': 1,
   'd': 67
   }
dict_to_list = []
# ('a', 12), ('b', 42), ('c', 1), ('d', 67)

for i in dictionary:
    dict_to_list.append((i, dictionary[i]))
print(dict_to_list)

for i in range(1, len(dict_to_list)):

    if dict_to_list[i][1] < dict_to_list[i-1][1]:

            range_len_array = [x for x in range(len(dict_to_list[0:i + 1]))]
            reversed_ind_array = range_len_array[::-1]

            for j in reversed_ind_array:
                if j != 0:

                    if dict_to_list[j][1] < dict_to_list[j - 1][1]:
                        dict_to_list[j - 1], dict_to_list[j] = dict_to_list[j], dict_to_list[j - 1]
print(dict_to_list)

#4
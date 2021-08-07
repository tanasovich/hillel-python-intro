import random

first_list: list = [random.randrange(0, 100) for i in range(15)]
second_list: list = [random.randrange(0, 100) for i in range(15)]

'''
Use list comprehension to populate list by zero each time when number exists either only in the first list either only
in the second list (if-xor condition). Thus, list length equals to the number of unique integers. len function shows
this parameter (list length).
'''
print(len([0 for i in first_list + second_list
           if first_list.count(i) == 1 ^ second_list.count(i) == 1]
          ))

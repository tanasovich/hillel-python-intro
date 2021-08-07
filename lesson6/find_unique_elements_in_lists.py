import random

first_list: list = [random.randrange(0, 100) for i in range(15)]
second_list: list = [random.randrange(0, 100) for i in range(15)]

print(len([0 for i in first_list + second_list
           if first_list.count(i) == 1 ^ second_list.count(i) == 1]
          ))

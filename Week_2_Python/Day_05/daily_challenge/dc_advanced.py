# Instructions
# Here is a python code that generate a list of 20000 random numbers, called list_of_numbers.
# Extend this code to guess how many couples of numbers in list_of_numbers sum to target_number.

import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728

sorted_list = sorted(list_of_numbers)
target_list = []
target_set = set()
couples = 0
unique_couples = 0
for index in range(0, len(sorted_list)) :
    if sorted_list[index] <= target_number :
        target_list.append(sorted_list[index])
        target_set.add(sorted_list[index])
# print(target_list)
# print(target_set)
for index in range(0, len(target_list)) :
    number = target_number - target_list[index]
    if number in target_list :
        couples += 1
for index in range(0, len(target_set)) :
    number = target_number - list(target_set)[index]
    if number in target_set :
        unique_couples += 1
print(couples)
print(unique_couples // 2)
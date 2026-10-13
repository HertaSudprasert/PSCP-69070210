"""pizza"""
import math

people = int(input())
people_want_eat = int(input())
slice_per_tard = int(input())

# 10                     5      *    2
total_slice_want_eat = people * people_want_eat
#                        10              //8
total_tard_needed = math.ceil(total_slice_want_eat / slice_per_tard)

slice_left = total_slice_want_eat - (total_tard_needed * slice_per_tard)

print(total_slice_want_eat)
print(total_tard_needed)
print(abs(slice_left))

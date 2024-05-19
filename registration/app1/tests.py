from django.test import TestCase
original_list = [1, 2, 3, 4, 5]
original_list2 = [1, 2, 3, 4, 5]
reversed_list1 = original_list[::-1]
reversed_list2 = original_list2.reverse()

print(reversed_list1)
print(original_list2)
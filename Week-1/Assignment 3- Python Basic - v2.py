#Assignment 3: Python Basic

#find_max
def find_max(numbers):
  max_value = 0
  for i in numbers:  
    if i > max_value:
      max_value = i
  return max_value

print(find_max([1, 2, 4, 5]))
print(find_max([5, 2, 7, 1, 6]))

#find_position
def find_position(numbers, target):
  count = -1
  for i in numbers:
    count += 1
    if i == target:
      return count 
  return -1

print(find_position([5, 2, 7, 1, 6], 5))
print(find_position([5, 2, 7, 1, 6], 7))
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
print(find_position([5, 2, 7, 1, 6], 8))

#想想不用再 i == target 時多一個 count = count - 1

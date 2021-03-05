# -*- coding: utf-8 -*-
def binary_search_first(numbers, target):
    low = 0
    high = len(numbers) - 1

    for i in range(low, high):
        mid = (low + high)//2
        if target > numbers[mid]:
            low = mid
        elif target < numbers[mid]:
            high = mid
    if high - low <= 1:
        return mid+1
    #carry mid
    for i in range(low,mid+1):
        if numbers[i] == target:
            return i
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2)) 
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5))
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3)) 


"""
def binary_search_position(numbers, target):
    low = 0
    high = len(numbers) - 1
    for i in range(low, high):
        mid = (low + high)/2
        if target > numbers[mid]:
            low = mid
        elif target < numbers[mid]:
            high = mid
    return mid


print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
"""
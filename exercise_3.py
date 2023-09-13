'''Exercise #3
Write a program to implement a Linear Search Algorithm. Also in a comment, write the Time Complexity of the following algorithm.

Hint: Linear Searching will require searching a list for a given number.
    

# If number is not present return -1'''

nums_list = [10,23,45,70,11,15]
target = 71

def linear_search(nums_list, target): #O(N) - We have to pass through the list looking for are target making this Linear.

    if target in nums_list: #O(N) - We need to iterate through the nums_list
        return f'{target} IS in this list' #O(1) - Returning a constant

    if target not in nums_list: #O(N) - We need to look through our list again
        return -1   #O(1) - Returning a constant
    
print(linear_search(nums_list, target)) #O(N) - Calling the function it has to interate the list anyways
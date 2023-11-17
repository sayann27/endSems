import numpy as np

arr = np.array([1,2,3,4])
arr2 = np.array([1,4,0,6])

# There can be two types of comparisons
# 1. Using comparison operators
# 2. using logicla operators

# Example of comparison operators

greater_than = arr > arr2 #These form boolean arrays
not_equal = arr != arr2
print(greater_than)
print(not_equal)

#Example of logical operators
print(np.logical_and(greater_than, not_equal))
print(np.logical_or(greater_than, not_equal))
print(np.logical_not(greater_than))

# Example of masks
# The boolean arrays are often used as 'masks'. Masks are boolean arrays that are used for conditional filtering and data manipulation
new_arr = np.array(arr[greater_than])
print(new_arr) #Only the value which is true is taken here, this is how masks are used

#Indexing can also be done in two ways
#1. By providing a list of indexes
#2. By providing a boolean array (mask)
int_indexing = np.array(arr[[2,3]])
boolean_indexing = np.array(arr[[False, False, True, True]])
print(int_indexing)
print(boolean_indexing)
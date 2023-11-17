import numpy as np

arr = np.array([1,2,3,56,3,65,56,7])
print(arr)

# Rank 2 array put a nested list for this
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# array created using tuple
arr_tuple = np.array((1,2,3))
print(arr_tuple)

# aggregation functions in numpy
print(f"The mean is:   {np.mean(arr)}")
print(f"The median is: {np.median(arr)}")
print(f"The sum is:   {np.sum(arr)}")
print(f"The standard deviation is:   {np.std(arr)}")
print(f"The variance is:   {np.var(arr)}")
print(f"The min is:   {np.min(arr)}")
print(f"The product is:   {np.prod(arr)}")
print(f"The cumulative sum is:   {np.cumsum(arr)}")
print(f"The cumulative product is:   {np.cumprod(arr)}")
print(f"The percentile is:   {np.percentile(arr, 50)}") #The value needs to be between 0 to 100
print(f"The quantile is:   {np.quantile(arr, 0.5)}") #The value needs to be between 0 and 1 and is similar to percentile




# sorting in numpy arrays
s=np.sort(arr)
print(s)
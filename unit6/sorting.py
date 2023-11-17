import numpy as np

arr = np.array([1,2,0,45,34])

# ascending sorting
asc_sort = np.sort(arr)
print(asc_sort)

#descending sorting
desc_sort = np.sort(arr)[::-1]
print(desc_sort)

# Indexes that would sort it
idx_sort = np.argsort(arr)
print(idx_sort)

#Indexes of max and min
idx_max = np.argmax(arr)
idx_min = np.argmin(arr)
print(idx_max)
print(idx_min)


#Structured arrays

#These are np arrays where the column names and there data types are specified 
#mydt is a list of tuples where each tuple has a name and datatye for the structure
mydt = [('name', 'U10'), ('age', int), ('married', bool)]

# Here all the data is entered according to the structure and can be accessed by their structure column names instead of index
new_arr = np.array([('Sayan', 24, False), ('Subroto', 24, False)], dtype=mydt)
print(new_arr)
print(new_arr['married'])
# Here index is used to access the particular record corresponding to the array
print(new_arr[0])


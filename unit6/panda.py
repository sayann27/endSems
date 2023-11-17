import pandas as pd

#Series data type in pandas

data = [1,2,3]

#Creating without specific index
sr = pd.Series(data)
print(sr)

#Creating with specific index
indexing = ['a', 'b' ,'c']
sr2 = pd.Series(data, index = indexing)
print(sr2)

#DataFrame datatype (uses dictionary as a data input and looks like excel or SQL Table)
data = {'name': ['Sayan', 'Subroto'], 'married': [True, False]}

#Creating without specific index
df = pd.DataFrame(data)
print(df)

#Creating with specific index
indexes = ['person1', 'person2']
df2 = pd.DataFrame(data, index=indexes)
print(df2)


#Reading from csv

df3 = pd.read_csv("demo.csv")
print(df3)


#Accessing data

#4 types of access
#1. Label based accessing  - using label names
#2. Index based accessing - using index
#3. Boolean accessing - Using a condition
#4. Fast Scalar accessing - Using integer values to access a specific record

#Label based accessing
print("\n\nNow we are accessing data")
print(df2['name']['person1'])

#Postition based
print(df2.iloc[0][0])

#Boolean accessing
print(df2[df2['married'] == True])

#Sorting
print(df2.sort_values(by='name', ascending=False))

#Missing data handling
print("\n\nHandling missing values")
print(df3.isna()) #alias for isnull
#same for notna (notnull)
print(df3.fillna(25))
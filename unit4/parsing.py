import pandas as pd

with open('convert.txt', 'r') as file:
    #It can be directly used or after converting it into a list of lines
    # lines = file.readlines()

    #removes \n character from the lines
    for line in file:
        print(line.strip())

df = pd.read_csv('convert.txt', sep=',', header=None, names=['column1', 'column2', 'column3'])
print(df)
df.to_csv('converted.csv', index=None)
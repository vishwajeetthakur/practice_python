
from distutils.log import error
import pandas as pd
import numpy as np

#1 link https://www.w3resource.com/python-exercises/pandas/index-dataframe.php

''''
data = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
d= pd.DataFrame(data)
print(d)

'''
#2



exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
data = pd.DataFrame(exam_data,index=labels)
print(data)
#3
'''
print(data.info())
#4 
print (data[:3])
#5 print selected colmns
print(data[['name','score']])
'''
#6 (iloc:integer index based, can specify rows and colmns)
print  (data.iloc[[1, 3, 5, 6], [1, 3]])

#7
print(data[data['attempts'] > 2])
#8
total_rows=len(data.axes[0])
total_cols=len(data.axes[1])
print(total_rows)
print(total_cols)

#9
print(data[data['score'].isnull()])
#10
print(data[data['score'].between(15, 20)])
#11
print(data[(data['attempts'] < 2) & (data['score'] > 15)])
#12
data.loc['d', 'score'] = 11.5
print(data)
#13
print(data['attempts'].sum())
#14
print(data['score'].mean())
#15
data.loc['k'] = [1, 'Suresh', 'yes', 15.5]
print(data)
#to drop
data = data.drop('k')
#16
data.sort_values(by=['name', 'score'], ascending=[False, True])
#17
data['qualify'] = data['qualify'].map({'yes': True, 'no': False})
print(data)
#18
data['name'] = data['name'].replace('James', 'Suresh')
#19
data.pop('attempts')
print(data)
#20
age = [18,19,18,20,21,22,23,24,25,26]
data['age']=age
print(data)
#22
liss=(list(data.columns.values))
print(liss)
#23
d = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(d)
print("Original DataFrame")
print(df)
df.columns = ['Column1', 'Column2', 'Column3']
df = df.rename(columns={'col1': 'Column1', 'col2': 'Column2', 'col3': 'Column3'})
print("New DataFrame after renaming columns:")
print(df)
#24
#x=df.loc[df['column2'] == 4]
#print(x)
#25
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print("Original DataFrame")
print(df)
print('After altering col1 and col3')
df = df[['col3', 'col2', 'col1']]
print(df)

#26
df2 = {'col1': 10, 'col2': 11, 'col3': 12}
df = df.append(df2, ignore_index=True)
print(df)

#27
df.to_csv('new_file.csv', sep='\t', index=False)
new_df = pd.read_csv('new_file.csv')
print(new_df)

#28
df1 = pd.DataFrame({'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'city': ['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles', 'Los Angeles', 'Georgia', 'Georgia', 'Los Angeles']})
g1 = df1.groupby(["city"]).size().reset_index(name='total ppl')
print(g1)
#29
df = df[df.col2 != 4]
print("New DataFrame")
print(df)
#30
pd.set_option('display.max_rows', 1500)
pd.set_option('display.max_columns', 1500)
pd.set_option('display.width', 2000)
print("Original DataFrame")
print(df)
#31
result = df.iloc[[2]]
print(result)
#32
data =  data.fillna(0)
print("\nNew DataFrame replacing all NaN with 0:")
print(data)
#34
#error
#35
exam_d = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
dff = pd.DataFrame(exam_d)
print("Original DataFrame")
print(dff)
print("\nNumber of NaN values in one or more columns:")
print(dff.isnull().values.sum())
#36
d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(d)
print("Original DataFrame")
print(df)
print("New DataFrame after removing 2nd & 4th rows:")
df = df.drop(df.index[[2,4]])
print(df)
#37
dff = dff.reset_index()
print(dff)
#38
part_70 = dff.sample(frac=0.7,random_state=10)
part_30 = dff.drop(part_70.index)
print(part_70)
print(part_30)
#39
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
s2 = pd.Series(['10', '20', 'php', '30.12', '40'])
print("Data Series:")
print(s1)
print(s2)
df = pd.concat([s1, s2],axis=1)
print("New DataFrame combining two series:")
print(df)
#40
dff = dff.sample(frac=1)
print(dff)
#41

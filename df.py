
import pandas as pd 

data = ["nidhi" , "sri" , "vyshu"]

initial = ['c' , 't' , 'c']

s = pd.Series(data=data , index=initial)  

print(s['t'])


name = ["sarah" , "max" , "cindy"]

print(name[2])


  

d = { 'NUM' : [1,2,3,4,5,45] , 'name' : ['nid' , 'sai' , 'sri' , 'teja' , 'sam','Shravya'] , 'roll no' : [5,33,1,34,"None",2] } 

print(d)



#d = [[1,2,3,4,5] , ['nid' , 'sai' , 'sri' , 'teja' , 'sam','Shravya'] , [6,7,8] ] 
data = pd.DataFrame(d)
# to filter colns from a huges dataframe 
#names = data[['name' , 'roll no']]

print(data[data['name']=='sai'])





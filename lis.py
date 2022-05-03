my_list=[6,"my","UD",68]
#print(mylist[:]) #list slicing
print(my_list)
print(my_list[1])
my_list.append("cs")
my_list.insert(1,"xyz")
print(my_list)
my_list.pop()
mylist2=[1,2]
my_list.insert(1,mylist2)
my_list.remove("my")
for i in range(len(my_list)):
    print(my_list[i],end=",")
print(len(my_list))
for i in my_list:
    print(i,end = " ")
# enumeration= to get index along with values
for ind,val in enumerate(my_list):
 print(ind,val)
 # to generate odd number

for new in range(50):
    if new%2==1:
        print(new, end= " ")
        new=i
k=[]
for i in range(20):
    if i%2==0:
        k.append(i)
        print(f"list of even numbers under {i} ")
        print(k)
        
print(k)
k[:5]="*"
oneline= [i for i in range(10) if i%2==1]
print(oneline)
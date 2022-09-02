# Append-a-List
list=[]
size=int(input("enter the size of list:"))
for i in range(1,size+1):
    a=int(input("enter the elements of list"))
    list.append(a)
even=[]
odd=[]
for j in list:
    if j%2==0:
        even.append(j)
        print("list of even",even)
    else:
        odd.append(j)
        print("list of odd",odd)

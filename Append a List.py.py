#Creating a list of "n" size and the appending the elements in it. Furthur dividing the list into two parts "EVEN" and "ODD".

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
    else:
        odd.append(j)
print("list of even",even)
print("list of odd",odd)

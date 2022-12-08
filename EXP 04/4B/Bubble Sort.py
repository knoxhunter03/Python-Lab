a=[]
size = int(input("\t Enter the size of the array : "))
print("\t Enter ",size," elements : ")
for i in range(size):
  a.insert(i,int(input()))
for i in range(len(a)-1) :
 for j in range(len(a)-i-1) :
   if a[j]>a[j+1]:
    a[j],a[j+1] = a[j+1],a[j]
print("\t The sorted array is : ",a)

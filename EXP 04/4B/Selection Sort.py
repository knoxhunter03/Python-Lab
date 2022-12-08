a=[]
size = int(input("\t Enter the size of the array : "))
print("\t Enter ",size," elements : ")
for i in range(size):
  a.insert(i,int(input()))
for i in range(len(a)-1) :
  small = a.index(min(a[i:]))
  a[i],a[small] = a[small],a[i]
print("\t The sorted array is : ",a)

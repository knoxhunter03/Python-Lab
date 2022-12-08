a=[]
size = int(input("\t Enter the size of the array : "))
print("\t Enter ",size," elements : ")
for i in range(size):
  a.insert(i,int(input()))
for i in range(1,len(a)) :
  key = a[i]
  j = i-1
  while j>=0  and key<a[j] :
   a[j+1] = a[j]
   j-=1
   a[j+1] = key
print("\t The sorted array is : ",a)

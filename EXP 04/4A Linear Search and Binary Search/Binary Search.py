def binary_Search(array,low,high,find) :
  if high>=low :
    mid = int((high+low)/2)
    if(array[mid] == find) :
      return mid
    elif(array[mid] > find) :
      return binary_Search(array,low,mid-1,find)
    else :
     return binary_Search(array,mid+1,high,find)
  else :
   return -1


size = int(input("\t Ente the Size of the Array : "))
print("\t Enter the Sorted Integer Array : ",end=" ")
array=[]
for num in range(0,size):
 array.insert(num,int(input()))
var = int(input("\t Enter the integer to be found : "))
index = int(binary_Search(array,0,len(array)-1,var))
if index==-1 :
  print("\t\t Element",var,"is not available in the array")
else :
  print("\t\t Element",var,"is found at index ",index)

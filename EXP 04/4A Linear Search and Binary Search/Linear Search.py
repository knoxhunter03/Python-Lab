def linear_Search(arr,find) :
 for i in range(0,len(arr)) :
  if arr[i] == find :
   return i
 return -1

array = str(input("\t Enter the String : "))
var = str(input("\t Enter the character to be found : "))[0]
index = int(linear_Search(array,var))
if index==-1 :
  print("\t\t Element",var,"is not available in the string")
else :
  print("\t\t Element",var,"is found at index ",index)

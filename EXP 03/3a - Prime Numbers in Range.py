n = int(input("\t Enter the value of n : "))
m = int(input("\t Enter the value of m : "))
if(m>n>0) :
 print("\t The prime Numbers are : ",end="")
 if(n<=3) :
  print("2 3",end=" ")
 for num in range(n,m+1):
  for i in range(2,int((num+1)/2)):
   if(i == int(num/2)) :
    print(num,end=" ")
   elif(num%i == 0) :
    i = 1
    num = num+1
else :
 print("\t Invalid Input ")

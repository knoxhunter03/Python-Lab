def gcd(a,b) :
 if(b == 0) :
  return a
 else :
  return gcd(b,a%b)
c = int(input("\t First value : "))
d = int(input("\t Second value: "))
print("\n\t GCD of ",c," and ",d," is : ",gcd(c,d))

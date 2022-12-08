total_overtime_pay=0
for i in range(10) :
  time= int(input("\n\t Enter the time employee worked in hrs : "))
  if (time>40):
    total_overtime_pay = total_overtime_pay + (12 * (time - 40))
print("\n\t\t Total Overtime Pay Of 10 employees is ",total_overtime_pay)

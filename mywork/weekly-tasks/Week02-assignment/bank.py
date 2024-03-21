amount1= int(input ("enter amount1(in cent): "))
amount2= int(input ("enter amount2(in cent): "))
totalAmount= amount1 + amount2
euro= totalAmount//100
cent= totalAmount%100
print (f" the sum of these is: €{euro}.{cent}")
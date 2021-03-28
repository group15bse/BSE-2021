amount = float(input("Enter amount to change: "))
#for any amount//given note or coin, gives the notes or coins available in the amount
#for any amount%given note or coin, gives the remainder of notes or coins in the amount
#notes section
#for 100 dollar
amount1 = amount//100
amount2 = amount%100
#for 50 dollar
amount3 = amount2//50
amount4 = amount2%50
#for 20 dollar
amount5 = amount4//20
amount6 = amount4%20
#for 10 dollar
amount7 = amount6//10
amount8 = amount6%10
#for 5 dollar
amount9 = amount8//5
amount10 = amount8%5
#for 1 dollar
amount11 = amount10//1
amount12 = amount10%1
#coins section
#for quaters
amount13 = amount12//0.25
amount14 = amount12%0.25
#for dimes
amount15 = amount14//0.1
amount16 = amount14%0.1
#for nickels
amount17 = amount16//0.05
amount18 = amount16%0.05
#for bronzes
amount19 = amount18//0.01
amount20 = amount18%0.01
print(int(amount1), "hundreds")
print(int(amount3), "fifties")
print(int(amount5), "twenties")
print(int(amount7), "tens")
print(int(amount9),  "five")
print(int(amount11), "one")
print(int(amount13), "quarter")
print(int(amount15), "dimes")
print(int(amount17), "nickles")
print(int(amount19), "pennies")
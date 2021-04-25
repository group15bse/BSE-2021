#GROUP 15 MEMBERS
#1. Arineitwe Davis 2020/BSE/011/PS
#2. Namuwaya Daphine Munnu 2020/BSE/048/PS
#3. Mulindwa Eric 2020/BSE/036/PS
#4. Otim Ronald 2020/BSE/061/PS

#Vending machine
nickels = 25
dimes = 25
quarters = 25
ones = 0
fives = 0
print("Welcome to a vending machine change maker program")
print("Change maker initialised.")
print(nickels,'nickles','\n',dimes,'dimes''\n',quarters,'quarters''\n',ones,'ones''\n',fives,'fives''\n')
while True:
        price = input("Enter the purchase price (xx.xx) or 'q' to quit:")
        if price == "q":
         print("Quiting.....")
         break
        else:
            print(price)
            price1 = float(price)
            if price1 > 0 and ((price1 * 100) % 5) == 0:
                print(price1)
                print("Menu for deposits:")
                print('\'n\' - deposit a nickel')
                print('\'d\' - deposit a dime')
                print('\'q\' - deposit a quarter')
                print('\'o\' - deposit a one dollar bill')
                print('\'f\' - deposit a five quarter bill')
                print('\'c\' - to cancel purchase')
                #dollar = round(price1//1)

                cents = round(price1*100)
                # cents
                dollar1 = 100
                nickel = 5
                quarter = 25
                dime = 10
                amountpaid = 0
                if True:
                    amountpaid = 0
                    while cents > 0:
                        deposit = input("Indicate your deposit:")
                        if deposit == 'n':
                           cents = cents - 5
                           amountpaid = amountpaid + 5
                        elif deposit == 'd':
                             cents = cents - 10
                             amountpaid = amountpaid + 10
                        elif deposit == 'q':
                             cents = cents - 25
                             amountpaid = amountpaid + 25
                        elif deposit == 'o':
                             cents = cents - 100
                             amountpaid = amountpaid + 100
                        elif deposit == 'f':
                             cents = cents - 500
                             amountpaid = amountpaid + 500
                        elif deposit == 'c':
                            break
                        dollar = cents // 100
                        if dollar >0:
                           print("Payment due",dollar,'dollar',cents%100,'cents')
                        else:
                            print("Payment due",cents%100,"cents")

                        print('Please take your change below\n',round(abs(cents)),"cents")
                        continue
            else:
                 print("Illegal price: Must be a non-negative multiple of 5 cents.")



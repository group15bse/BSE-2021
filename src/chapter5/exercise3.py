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
        price1 = float(price)
        if price1 > 0 and ((price1 * 100) % 5) == 0:
           print("Menu for deposits:")
           continue
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")



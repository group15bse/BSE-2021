while True:
    try:
        print("\nWelcome!!!")
        code = input("Enter customer code:")
        if code == 'r' or code == 'R':
            print('Valid code r')
        elif code == 'c' or code == 'C':
            print('Valid code c')
        elif code == 'i' or code == 'I':
            print('Valid code i')
        else:
            print('Invalid code')
            continue
    except:
        print("Error!!!, Enter a valid code.")
    a = int(input("Beginning meter number:"))
    b = int(input("Ending meter number:"))
    if a >= 0 and b <= 999999999:
        if a > b:
            gallons = (1000000000 - a) + b
        else:
            b > a
            gallons = b - a
    else:
        a < 0 and b > 999999999
        print("Invalid meter number!!!")
        print("Please enter a valid meter number")
        continue
    if code == 'r' and code == 'R':
        bill = 5.00 + (gallons * 0.0005)
    elif code == 'c' and code == 'R':
        if gallons > 4000000:
            bill = 1000 + ((gallons - 4000000) * 0.00025)
        else:
            bill = 1000
    else:
        code == 'i' and code == 'I'
        if gallons <= 4000000:
            bill = 1000
        elif gallons > 4000000 and gallons <= 10000000:
            bill = 2000
        else:
            gallons > 10000000
            bill = 2000 + ((gallons - 4000000) * 0.00025)
    print("Gallons of water used:",gallons * 0.1)
    print(f"Amount billed: ${bill:.2f}")
    print("\nCustomer code:",code)
    print("Customer beginning meter reading:",a)
    print("Customer ending meter reading:",b)
    print("Gallons of water used by the customer:",gallons)
    print(f"Amount of money billed to the customer: ${bill:.2f}")



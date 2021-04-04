guests = int(input("Enter number of guests:"))
if guests <= 50:
    print("Cost $4,000")
elif guests <= 100:
    print("Cost $10,000")
elif guests <= 200:
    print("Cost $15,000")
else:
    print("Cost $20,000")
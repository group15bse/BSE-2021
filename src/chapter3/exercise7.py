try:
    location = input("Enter job location:")
    pay = float(input("Enter pay:"))
    if location == "Mbarara":
        if pay > 4000000:
            print("I will take on the job")
        else:
            print("No way")
    elif location == "Kampala":
        if pay >= 10000000:
            print("I will take on the job")
        else:
            print("No way")
    elif location == "Space":
            print("Without doubt, I'll will take it")
    else:
        if pay > 6000000:
             print("Sure, I can work with this")
        else:
            print("No thanks, I can find something better")
except:
    print("Invalid input")
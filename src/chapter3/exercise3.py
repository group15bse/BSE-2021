score = float(input("Enter score:"))
if score >= 0.0 and score <= 1.0:
    if score >= 0.9:
        print("Grade", 'A')
    elif score >= 0.8:
        print("Grade", 'B')
    elif score >= 0.7:
        print("Grade", 'C')
    elif score >= 0.6:
        print("Grade", 'D')
    else:
        print("Grade", 'F')
else:
    print("Bad score")


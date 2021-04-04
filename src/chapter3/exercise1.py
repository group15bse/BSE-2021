hours = float(input("Enter hours:"))
rate = float(input("Enter rate:"))
if hours > 40:
    epay = (hours - 40) * rate * 1.5
    pay = (40 * rate) + epay
else:
    pay = hours * rate
print("Pay",pay)
try:
    total = 0
    count = 0
    while True:
        num = input("Enter a number: ")
        if num == "done":
            break
        else:
            num1 = float(num)
            total = total + num1
            count = count + 1
            average = total/count
    print(total,count,average)
except:
    print("Please enter a valid input")
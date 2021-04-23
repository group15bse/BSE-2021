min = None
max = None
while True:
        try:
            num = input('Enter numbers: ')
            if num == 'done':
                break
            else:
                num1 = float(num)
            if min is None or num1 < min:
                min = num1
            if max is None or num1 > max:
                max = num1
        except:
               print("Enter a valid input!!")
print('min',min)
print('max',max)

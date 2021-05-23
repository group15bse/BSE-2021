list = []
while True:
    inp = input("Enter a number: ")
    if inp == "done":
       break
    else:
        value = float(inp)

    list.append(value)
max = max(list)
min = min(list)


print('list =', list)
print('max =', max)
print('min =', min)



def investment():
    c = float(input("Enter initial investment:"))
    r = float(input("Enter the rate:"))
    n = float(input("Enter number of computation per year:"))
    t = float(input("Enter years:"))
    v = 1 + r/n
    k = t*n
    z = v**k
    p = c * z
    print(round(p,2))
investment()

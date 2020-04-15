c0 = int(input("Enter c0: "))

if c0 > 1:
    steps = 0
    while c0 != 1:
        if c0 %2 != 0:
            c0 = 3 * c0 + 1
        else:
            c0 = c0 // 2
        print (c0)
        steps += 1
    print ("steps =", steps)
else:
    print ("Bad c0 value")

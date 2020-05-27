def l100kmtompg(liters):
    gallons = liters/3.785411784
    miles = 1000/1609.344*100
    return miles/gallons

def mpgtol100km(miles):
    km100 = miles*1609.344/1000/100
    liters = 3.785411784
    return liters/km100

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

beatles = []
length = len(beatles)
print("Step 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

for members in range(2):
    beatles.append(input("New band member: "))
print("Step 3:", beatles)

del(beatles[-1])
del(beatles[-1])
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list length
print("The Fab", len(beatles))

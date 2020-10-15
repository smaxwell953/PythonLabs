str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

strx1 = ''.join(sorted(list(str1.upper().replace(' ',''))))
strx2 = ''.join(sorted(list(str2.upper().replace(' ',''))))
if len(strx1) > 0 and strx1 == strx2:
	print("Anagrams")
else:
	print("Not anagrams")

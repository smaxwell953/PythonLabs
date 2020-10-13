text = input("Enter text: ")
text = text.replace(' ','')
if len(text) > 1 and text.upper() == text[::-1].upper() or \
   text.lower() == text[::-1].lower():
	print("It's a palindrome")
else:
	print("It's not a palindrome")

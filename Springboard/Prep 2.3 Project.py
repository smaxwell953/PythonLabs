text = input("Enter message: ")
shift = int(input("Enter cipher's shift (1..25): "))

def caesarCipher():
    cipher = ''
    
    for char in text:
        if char.isalpha():
            code = ord(char) + shift
            if char.isupper():
                first = ord('A')
            else:
                first = ord('a')
            code -= first
            code %= 26
            cipher += chr(first + code)
        else:
            cipher += char

    print(cipher)

caesarCipher()

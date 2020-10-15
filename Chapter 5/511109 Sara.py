date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM or MMDDYYYY or DDMMYYYY, 8 digits): ")
if len(date) != 8 or not date.isdigit():
        print("Invalid date.")
else:
        while len(date) > 1:
                sum = 0
                for dig in date:
                        sum += int(dig)
                date = str(sum)
        print("Your Digit of Life is: " + date)

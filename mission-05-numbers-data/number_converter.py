# A small program to convert a decimal number to binary and hexadecimal

number_text = input("Enter a positive whole number: ")

try:
    number = int(number_text)

    if number <= 0:
        print("Please enter a number greater than zero.")
    else:
        print("Binary:", bin(number))
        print("Hexadecimal:", hex(number))

except ValueError:
    print("Please enter a valid whole number.")


num = int(input("Enter a decimal number: "))

print("1. Convert to Binary")
print("2. Convert to Hexadecimal")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Binary:", bin(num)[2:])

elif choice == 2:
    print("Hexadecimal:", hex(num)[2:].upper())

else:
    print("Invalid choice")

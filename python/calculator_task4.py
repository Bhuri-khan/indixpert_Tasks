print("================================")
print("---------- Calculator ----------")
print("================================")
print("1. Addition")
print("2. Substraction")
print("3. Multiply")
print("4. Divide")
choice=input("Enter Your Choice: ")
if choice=="1":
    first_number=int(input("Enter First Number: "))
    second_number=int(input("Enter Second Number: "))
    print("Addition: ",first_number+second_number)
elif choice=="2":
    first_number=int(input("Enter First Number: "))
    second_number=int(input("Enter Second Number: "))
    print("Substraction: ",first_number-second_number)
elif choice=="3":
    first_number=int(input("Enter First Number: "))
    second_number=int(input("Enter Second Number: "))
    print("Multiply: ",first_number*second_number)
elif choice=="4":
    first_number=int(input("Enter First Number: "))
    second_number=int(input("Enter Second Number: "))
    print("Divide: ",first_number/second_number)
else:
    print("Invalid Your Choice: ")
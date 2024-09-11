from calculate import calculation
from kyle_factors import factors
import time
import random as rand

print("""
Welcome to the Basic Python Calculator!
Program by Kyle Bendall.
Press CTRL+C to exit at any time.
Available operators: +, -, *, /, //, %
You can also find the factors of a number by entering 'yes' when prompted.
""")

print("LOADING: This may take a few seconds...")

sleep = rand.randint(3, 7)

time.sleep(sleep)

running = input("Would you like to perform a calculation with the Basic Python Calculator? (yes/no): ")


while running.lower() == "yes":
    do_factors = input("Do you want to find the factors of a number? (yes/no): ")
    if do_factors.lower() == "yes":
        num = int(input("Enter a number to find it's factors: "))
        print(f"Factors of {num} are: ")
        factors(num)
    else:
        print("OK! Starting simple calculation module...")
        while True:
            try:
                num1 = int(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        operator = input("Enter operator (+, -, *, /, //, %): ")
        while True:
            try:
                num2 = int(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")

        calculation(num1=num1, operator=operator, num2=num2)

        running = input("Do you want to perform another calculation? (yes/no): ")

if running.lower() == "no":
    print("Thank you for using the Basic Python Calculator. Goodbye!")
    time.sleep(3)
    

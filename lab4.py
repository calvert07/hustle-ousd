continue_checking = "yes"

while continue_checking == "yes":
    age = int (input("Enter the person's age: "))
    if age >= 18:
        print ("This person is eligible to vote.")
    else:
        print ("This person is not eligible to vote.")
    continue_checking = input ("Do you want to check another age? (yes/no): ")

print ("Thank you for using the voting eligibility checker!")
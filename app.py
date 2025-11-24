print("Test")
print("test")
try:
    #Input asks for users starting amount
    starting_amount = float(input("What is your starting amount?"))
    ending_amount = starting_amount * 1.1
    print(f"Ending amount is {ending_amount}")
    #Shows an error message if user puts in wrong numnber
except ValueError:
    print("Please Enter a Valid Figure")
    exit()
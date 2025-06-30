logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1, n2):
    return n1 + n2
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a // b
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
repeat_again = True
first_number = float(input("What's the first number? "))
while repeat_again:
    operation = input("Choose an operation: \n+ \n- \n* \n/ \n")
    second_number = float(input("What's  the next number? "))
    for each_operation in operations:
        if operation == each_operation:
            result = operations[each_operation](first_number, second_number)
            print(f"{first_number} {operation} {second_number} = {result}")
            continue_calculation = input(
                f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation, 'quit' to exit: ").lower()
            if continue_calculation == "y":
                first_number = result
            elif continue_calculation == "n":
                print("\n" * 40)
                first_number = float(input("What's the first number? "))
            elif continue_calculation == "quit":
                print("Goodbye!")
                repeat_again = False
            else:
                print("You entered the wrong input.")
                repeat_again = False




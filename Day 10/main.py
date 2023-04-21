print("Welcome to PyCalculator!")


def calculate(first_num, second_num, operation):
    if operation == "+":
        solution = first_num + second_num
    elif operation == "-":
        solution = first_num - second_num
    elif operation == "*":
        solution = first_num * second_num
    elif operation == "/":
        solution = first_num / second_num
    else:
        print("There was an unexpected error.")
        return None

    print(f"{first_num} {operation} {second_num} = {solution}")
    return solution


def get_values(first_num):
    if first_num is None:
        first_num = int(input("What's the first number?: "))

    operation = input("Pick an operation (+-*/): ")
    second_num = int(input("What is the second number?: "))
    calc_num = calculate(first_num, second_num, operation)
    return calc_num


first_num = None
while True:
    calc_num = get_values(first_num)
    sentinel = input(f"Type 'y' to continue calculating with {calc_num} or type 'n' to start a new calculation. Type 'q' to quit.\n")
    if sentinel == "y":
        first_num = calc_num
    elif sentinel == 'n':
        first_num = None
    else:
        break
print("Thank you for using PyCalculator.")
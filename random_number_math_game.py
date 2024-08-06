import random


def get_correct_ans(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return round(num1 / num2, 2)
    elif operator == "%":
        return num1 % num2


operator_descriptions = {
    "+": "Add",
    "-": "Subtract",
    "*": "Multiply",
    "/": "Divide upto 2 decimal places",
    "%": "Modulus",
}

operators = ["+", "-", "*", "/", "%"]
score = 0
count = 0
while count < 5:
    count = count + 1

    # Generate two random integers
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    # Generate random operator
    operator_index = random.randint(0, 4)
    operator = operators[operator_index]

    # Print description of operator
    print(f"{operator_descriptions[operator]}:")

    # Get user input
    user_input = float(input(f"{num1} {operator} {num2} = "))

    # Get correct answer
    correct_ans = float(get_correct_ans(num1, num2, operator))
    print()

    # Compare user
    if user_input == correct_ans:
        score = score + 1

print(f"Your score is: {score}")

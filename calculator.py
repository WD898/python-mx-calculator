# Integer calculator


# List of functions
def add(num1, num2):
    addition = num1 + num2
    return addition


def sub(num1, num2):
     subtraction = num1 - num2
     return subtraction


def multi(num1, num2):
    multiplication = num1 * num2
    return multiplication


def div(num1, num2):
    division = num1 / num2
    return division


def main():
    # Determine which operation to undertake
    opr = input("Please select the operator :\n + - * / ")
    if opr not in ["+", "-", "*", "/"]:
        print("Invalid selection\n")
        main()

    # Ensure that only integer numbers are selected
    try:
        num1=int(input("First number : "))
        num2=int(input("Second number : "))

    # If a non integer is selected, throw an error message and try again
    except ValueError:
        print("Please select an integer\n")
        main()

    if opr == "+":
        answer = add(num1, num2)

    elif opr == "-":
        answer = sub(num1, num2)

    elif opr =="*":
        answer = multi(num1, num2)

    elif opr =="/":
        answer = div(num1, num2)

    print("Your answer is : {} {} {} = {:.2f}".format(num1, opr, num2, answer))


if __name__ == "__main__":
    print("--------Welcome to MX Calculator--------\n"
            "-----Developed by (Swarup Bhagwat.)-----\n"
            "-----------------V1.3-------------------\n")
    main()

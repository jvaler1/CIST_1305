# Create a module named calc_one
# It will take 2 inputs and do addition, subtraction, multiplication, division, and modulus

import calc_one

def main():
    
    num1, num2, operation = num_input()
    output(num1, num2, operation)


def output(num1, num2, operation):
    print(f"\nYou input {num1} and {num2}, then selected {operation}. The output is:\n")

    operation = operation.lower()
    match operation:
        case "add":
            print(f"Output: {calc_one.calc_sum(num1, num2)}\n")
        case "subtract":
            print(f"Output: {calc_one.calc_sub(num1, num2)}\n")
        case "multiply":
            print(f"Output: {calc_one.calc_mult(num1, num2)}\n")
        case "divide":
            print(f"Output: {calc_one.calc_div(num1, num2)}\n")
        case "modulus":
            print(f"Output: {calc_one.calc_mod(num1, num2)}\n")
        case _:
            print(f"Error: The operation input {operation} was invalid")
            

def num_input():

    num1 = int(input("Input first number to calculate: "))
    num2 = int(input("Input second number to calculate: "))
    operation = input(f"What operation will done? Valid inputs are:\n"
                      f"Add | Subtract | Multiply | Divide | Modulus\n"
                      )
    
    return num1, num2, operation

main()
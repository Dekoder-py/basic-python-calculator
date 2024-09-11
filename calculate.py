from result import print_result
def calculation(operator, num1, num2):
    if operator == "+":
        result = num1 + num2
        print_result(result)
    elif operator == "-":
        result = num1 - num2
        print_result(result)
    elif operator == "*":
        result = num1 * num2
        print_result(result)
    elif operator == "//":
        result = num1 // num2
        print_result(result)
    elif operator == "%":
        result = num1 % num2
        print_result(result)
    elif operator == "/":
        float_num1 = float(num1)
        float_num2 = float(num2)
        result = float_num1 / float_num2
        print_result(result)
    else:
        print("ERROR: INVALID INPUT.")

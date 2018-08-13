import re
import math
import ast


def input_validation(exp):
    if re.search(r'[a-zA-Z=#<>`;\?\\]', exp):
        raise ValueError("Unexpected characters in expression.")


def evaluate_literal_types(exp_list):
    operations = ['+', '-', '*', '/', '^', '!', '%', '&', '$', '@', '[', ']']
    return [ast.literal_eval(operand) if operand not in operations else operand for operand in exp_list]


def exp_to_list(exp):
    exp_list = re.findall(
        r'[\[\]@&!*/^%$+-]|~?\d+(?:\.\d*)?|~?\.\d+', exp.replace(' ', ''))
    return [e.replace('~', '-') for e in exp_list]


def closest_operation(exp_list, operation_group):
    return min(exp_list.index(op) if op in exp_list else math.inf for op in operation_group)


def list_rindex(alist, value):
    return len(alist) - list(reversed(alist)).index(value) - 1


def evaluate_operation(exp_list, op_pos):
    operation = exp_list[op_pos]
    left_op = exp_list[op_pos - 1]
    right_op = exp_list[op_pos + 1] if len(exp_list) > op_pos + 1 else None

    if operation == ']':
        opening_bracket_pos = list_rindex(exp_list[:op_pos], '[')
        evaluated_expression = evaluate_list(
            exp_list[opening_bracket_pos+1:op_pos])
        exp_list[op_pos] = evaluated_expression
        del exp_list[opening_bracket_pos:op_pos]
        return

    if operation == '!':
        exp_list[op_pos] = math.factorial(left_op)
        del exp_list[op_pos-1]
        return

    elif operation == '&':
        exp_list[op_pos] = min(left_op, right_op)
    elif operation == '$':
        exp_list[op_pos] = max(left_op, right_op)
    elif operation == '@':
        exp_list[op_pos] = (left_op + right_op) / 2
    elif operation == '%':
        exp_list[op_pos] = left_op % right_op
    elif operation == '^':
        exp_list[op_pos] = math.pow(left_op, right_op)
    elif operation == '/':
        exp_list[op_pos] = left_op / right_op
    elif operation == '*':
        exp_list[op_pos] = left_op * right_op
    elif operation == '+':
        exp_list[op_pos] = left_op + right_op
    elif operation == '-':
        exp_list[op_pos] = left_op - right_op
    del exp_list[op_pos-1], exp_list[op_pos]


def evaluate_list(exp_list):
    precedence = [('+', '-'), ('*', '/'),
                  ('^'), ('!', '%'), ('&', '$', '@'), (']')]
    for operation_group in reversed(precedence):
        while closest_operation(exp_list, operation_group) != math.inf:
            operation = closest_operation(exp_list, operation_group)
            evaluate_operation(exp_list, operation)
    return exp_list[0]


def main():
    print('Please enter your arithmetic expression.')
    while True:
        expression = input('>>> ')
        try:
            input_validation(expression)
            expression_list = exp_to_list(expression)
            expression_list = evaluate_literal_types(expression_list)
            evaluate_list(expression_list)
            print(*expression_list)
        except (TypeError, ValueError):
            print("Please make sure you're entering a valid expression.")


if __name__ == '__main__':
    main()

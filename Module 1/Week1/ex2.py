import math


# Check number
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


# Activation functions
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def elu(x, alpha=0.01):
    return x if x > 0 else alpha * (math.exp(x) - 1)


def activation_function(x, activation_name):
    if not is_number(x):
        print('x must be a number')
        return

    x = float(x)

    if activation_name not in ['sigmoid', 'relu', 'elu']:
        print(f'{activation_name} is not supported')
        return

    if activation_name == 'sigmoid':
        result = sigmoid(x)
    elif activation_name == 'relu':
        result = relu(x)
    elif activation_name == 'elu':
        result = elu(x)

    print(f'{activation_name}: f({x})={result}')


if __name__ == '__main__':
    x_input = input("Enter value of x: ")
    activation_function_name = input("Enter activation function name (sigmoid, relu, elu): ")

    activation_function(x_input, activation_function_name)

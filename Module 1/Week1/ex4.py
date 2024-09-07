def factorial(num):
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def sin_approx(x, n):
    # tính giá trị chuỗi Taylor của sin(x) với n lần lặp
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result


def cos_approx(x, n):
    result = 0
    for i in range(n):
        term = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result


def sinh_approx(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result


def cosh_approx(x, n):
    result = 0
    for i in range(n):
        term = (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result


# Test
x = float(input("Enter value of x (radian): "))
n = int(input("Enter number of terms for approximation (n): "))

if n <= 0:
    print("Number of terms must be a positive integer greater than 0")
else:
    print(f'sin({x}) ≈ {sin_approx(x, n)}')
    print(f'cos({x}) ≈ {cos_approx(x, n)}')
    print(f'sinh({x}) ≈ {sinh_approx(x, n)}')
    print(f'cosh({x}) ≈ {cosh_approx(x, n)}')

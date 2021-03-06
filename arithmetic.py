def add(num1, num2):
    """adding num1 plus num2"""

    return num1 + num2


def subtract(num1, num2):
    """subtract num2 from num1"""

    return num1 - num2


def multiply(num1, num2):
    """multiply num1 by num2"""

    return num1 * num2


def divide(num1, num2):
    """devide num1 by num2"""

    return float(num1) / float(num2)


def square(num1):
    """num1 squared"""

    return num1 * num1


def cube(num1):
    """num1 cubed"""

    return num1 * num1 * num1


def power(num1, num2):
    """num1 to the num2 power"""
    if num2 > 0:
        return float(num1) ** float(num2)
    else:
        return (1.0/(float(num1) ** float(num2)))

def mod(num1, num2):
    """remainder when num1 is divided by num2"""

    return num1 % num2

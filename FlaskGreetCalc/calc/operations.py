def add(a, b):
    """Ad"""
    return a + b

def sub(a, b):
    """Subtract"""
    return a - b

def mult(a, b):
    """Multiply"""
    return a * b

def div(a, b):
    """Divide"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b


from jsonrpc import dispatcher


@dispatcher.add_method
def add(addend1: float, addend2: float) -> float:
    return addend1 + addend2


@dispatcher.add_method
def subtract(minuend: float, subtrahend: float) -> float:
    return minuend - subtrahend


@dispatcher.add_method
def multiply(multiplicand: float, multiplier: float) -> float:
    return multiplicand * multiplier


@dispatcher.add_method
def divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        msg = "Division by zero is not allowed."
        raise ValueError(msg)
    return dividend / divisor

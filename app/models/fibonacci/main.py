from app.lib.fibonacci import main as fibonacciLib

def getNNumbers(n, offset):
    return [fibonacciLib.getNthNumber(i) for i in range(offset, n)]


class FibonacciModel:
    pass

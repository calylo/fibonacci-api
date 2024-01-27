from app.lib.fibonacci import main as fibonacciLib

def getPage(page, pageSize):
    offset = page * pageSize
    result = [fibonacciLib.getNthNumber(i) for i in range(offset, pageSize + offset)]

    return {
        "result": result, 
        "page": page, 
        "pageSize": pageSize
    }

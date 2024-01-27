from app.lib.fibonacci import main as fibonacciLib
from app.models.blacklist import main as blacklistModel

def getPage(page, pageSize):
    offset = page * pageSize
    result = []
    for i in range(offset, pageSize + offset):
        number = fibonacciLib.getNthNumber(i)
        if(blacklistModel.contains(number)):
            number = None
        result.append(number)

    return {
        "result": result, 
        "page": page, 
        "pageSize": pageSize
    }


def getNumber(n):

    return {
        "result": fibonacciLib.getNthNumber(n), 
    }

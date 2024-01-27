from app.lib.fibonacci import main as FibonacciLib
from fastapi import HTTPException

_blacklist = []


def addToList(n):
    if (not FibonacciLib.isFibonacciNumber(n)):
        raise HTTPException(status_code=400,
                            detail="Number is not in fibonacci sequence")
    if (n in _blacklist):
        raise HTTPException(status_code=409,
                            detail="Number is already in blacklist")
    _blacklist.append(n)
    _blacklist.sort()

    return {"result": n}


def getPage(page, pageSize):

    return {
        "result": _blacklist[page * pageSize:page + 1 * pageSize],
        "page": page,
        "pageSize": pageSize,
    }


def contains(n):
    return n in _blacklist

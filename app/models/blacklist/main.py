from app.lib.fibonacci import main as FibonacciLib
from fastapi import HTTPException

_blacklist = []

def addToList(n):
    if(not FibonacciLib.isFibonacciNumber(n)):
        raise HTTPException(status_code=400, detail="Number is not in fibonacci sequence")
    _blacklist.append(n)
    return {"result": n}

from fastapi import HTTPException

from app.lib.fibonacci import main as FibonacciLib

_blacklist = []


def add_to_list(n):
    if not FibonacciLib.is_fibonacci_number(n):
        raise HTTPException(status_code=400,
                            detail="Number is not in fibonacci sequence")
    if n in _blacklist:
        raise HTTPException(status_code=409,
                            detail="Number is already in blacklist")
    _blacklist.append(n)
    _blacklist.sort()

    return {"result": n}


def get_page(page, page_size):

    return {
        "result": _blacklist[page * page_size:page + 1 * page_size],
        "page": page,
        "pageSize": page_size,
    }


def contains(n):
    return n in _blacklist

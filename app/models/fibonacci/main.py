from app.lib.fibonacci import main as fibonacciLib
from app.models.blacklist import main as blacklistModel


def get_page(page, page_size):
    offset = page * page_size
    result = []
    for i in range(offset, page_size + offset):
        number = fibonacciLib.get_nth_number(i)
        if blacklistModel.contains(number):
            number = None
        result.append(number)

    return {
        "result": result,
        "page": page,
        "pageSize": page_size
    }


def get_number(n):

    return {
        "result": fibonacciLib.get_nth_number(n),
    }

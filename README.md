# fibonacci-api
API for returning fibonacci numbers
## setup
```bash
pip3 install fastapi
pip3 install "uvicorn[standard]"
```

## run
```bash
uvicorn app.main:app --reload
```

## test
```bash
python3 -m unittest app.tests.test_lib.test_fibonacci
```

## Endpoints
### GET /api/v1/fibonacci/numbers
Get a collection of fibonacci numbers

Example response:
```JSON
{
    "result": [0,1,1,2,3,5],
    "page": 0,
    "pageSize": 5
}
```
> **_NOTE:_**  Numbers can be null. [See description](#blacklist-handling)

### GET /api/v1/fibonacci/numbers/{index}
Get Nth fibonacci number

Example response:
```JSON
{
    "result": 5
}
```

### GET /api/v1/fibonacci/blacklist
Get blacklist collection

Example response:
```JSON
{
    "result": [0,3,5],
    "page": 0,
    "pageSize": 3
}
```

### POST /api/v1/fibonacci/blacklist
Add number to blacklist

Example request body:
```JSON
{
    "number": 5,
}
```

Example response:
```JSON
{
    "number": 5,
}
```

## Pagination
Any collection supports pagination using query parameters:
- `page` page number to request, zero-indexed
- `pageSize` number of results per page, defaults to 100

example request: 

`GET /api/v1/fibonacci/numbers?page=2&pageSize=15`



## Fibonacci calculation
An nth power of matrix algorithm is implemented for efficient calculation, giving time complexity of O(Log n)

This approach relies on the fact that if we n times multiply the matrix M = {{1,1},{1,0}} to itself (in other words calculate power(M, n)), then we get the (n+1)th Fibonacci number as the element at row and column (0, 0) in the resultant matrix.

If n is even then k = n/2:   
- Therefore Nth Fibonacci Number = F(n) = [2*F(k-1) + F(k)]*F(k)

If n is odd then k = (n + 1)/2:    
- Therefore Nth Fibonacci Number = F(n) = F(k)*F(k) + F(k-1)*F(k-1)

algorithm source: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

## Fibonacci validation
To validate input as fibonacci numbers we take advantage of the mathematical property that if 5n^2+4 or 5n^2-4 is a perfect square

## Blacklist handling
Numbers blacklisted will be replaced with null in the output to ensure that page size matches the request and to ensure that each number returned will always have the correct index
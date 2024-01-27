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


## Fibonacci calculation
An nth power of matrix algorithm is implemented for efficient calculation, giving time complexity of O(Log n)

This approach relies on the fact that if we n times multiply the matrix M = {{1,1},{1,0}} to itself (in other words calculate power(M, n)), then we get the (n+1)th Fibonacci number as the element at row and column (0, 0) in the resultant matrix.

If n is even then k = n/2:   
- Therefore Nth Fibonacci Number = F(n) = [2*F(k-1) + F(k)]*F(k)

If n is odd then k = (n + 1)/2:    
- Therefore Nth Fibonacci Number = F(n) = F(k)*F(k) + F(k-1)*F(k-1)

algorithm source: https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/


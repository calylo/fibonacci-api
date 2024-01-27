# algorithm for calculating nth fibonacci number
# sourced from https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/

def getNthNumber(n):
    F = [[1, 1],
         [1, 0]]
    if (n == 0):
        return 0
    _nthPowerOfMatrix(F, n - 1)
 
    return F[0][0]
 
 
def _multiplyMatrix(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])
 
    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w
 
def _nthPowerOfMatrix(F, n):
    if(n == 0 or n == 1):
        return
    M = [[1, 1],
         [1, 0]]
 
    _nthPowerOfMatrix(F, n // 2)
    _multiplyMatrix(F, F)
 
    if (n % 2 != 0):
        _multiplyMatrix(F, M)
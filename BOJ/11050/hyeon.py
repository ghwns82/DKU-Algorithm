n, r = map(int, input().split())

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# nCr = n! / ((n-r)! * r!)
answer = factorial(n) // (factorial(n-r)*factorial(r))
print(answer)
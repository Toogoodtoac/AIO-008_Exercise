def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
def sin_approx(x,n):
    result = 0
    for i in range(n):
        term = (-1)**i * x**(2*i+1) / factorial(2*i+1)
        result += term
    return result
def cos_approx(x,n):
    result = 0
    for i in range(n):
        term = (-1)**i * x**(2*i) / factorial(2*i)
        result += term
    return result + 1  # cos(0) = 1
def sinh_approx(x,n):
    result = 0
    for i in range(n):
        term = x**(2*i+1) / factorial(2*i+1)
        result += term
    return result
def cosh_approx(x,n):
    result = 0
    for i in range(n):
        term = x**(2*i) / factorial(2*i)
        result += term
    return result + 1 
if __name__ == '__main__':
    x=float(input("Enter x:"))
    n=int(input("Enter n:"))
    print("sin(x)=",sin_approx(x,n))
    print("cos(x)=",cos_approx(x,n))
    print("sinh(x)=",sinh_approx(x,n))
    print("cosh(x)=",cosh_approx(x,n))
  

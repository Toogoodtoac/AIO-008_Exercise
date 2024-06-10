import math
def different_of_nth_root_error(y, y_hat, n, p):
        error = abs(y ** (1/n) - y_hat ** (1/n))
        loss = error ** p
        return loss
if __name__ == '__main__':
    y=float(input("Enter y:"))
    y_hat=float(input("Enter y_hat:"))
    n=int(input("Enter n:"))
    p=int(input("Enter p:"))
    print(different_of_nth_root_error(y, y_hat, n, p))
  

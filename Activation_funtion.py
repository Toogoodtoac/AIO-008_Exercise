import math
import sys
import numpy as np
def check_activation_function(function_name):
  valid_functions = ['sigmoid', 'relu', 'elu']
  if function_name.lower() in valid_functions:
      return True
  else:
      print(f"{function_name} is not supported")
      return False
def is_number (n) :
   try :
    float (n) 
   except ValueError :
    return False
    return True
def elu(e,x):
  alpha=0.01
  return np.where(x > 0, x, alpha * (e**x - 1))
def sigmoid(e,x):
  return 1 / (1 + e**(-x))
def relu(e,x):
  return np.maximum(0, x)
if __name__ == '__main__':
  e=math.e
  x=float(input('Enter x: '))
  activation_name=input('Activation name: ')
  if is_number(x)==False:
    print (f'x must be a number')
    sys.exit(1)
  if(check_activation_function(activation_name)==False):
    sys.exit(1)
  if(activation_name=='sigmoid'):
    print(f'sigmoid: {sigmoid(e,x)}')
  elif(activation_name=='relu'):
    print(f'relu: {relu(e,x)}')
  elif(activation_name=='elu'):
    print(f'elu: {elu(e,x)}')

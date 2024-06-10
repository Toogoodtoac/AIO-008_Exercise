import random
import math
import sys
def mae_loss(predict, target):
    return sum(abs(y_true - y_pred) for y_true, y_pred in zip(target, predict)) / len(target)
def mse_loss(predict, target):
    return sum((y_true - y_pred) ** 2 for y_true, y_pred in zip(target, predict)) / len(target)
def rmse_loss(predict, target):
    return math.sqrt(mse_loss(predict, target))
if __name__ == '__main__':
    num_samples = input("Enter the number of samples: ")
    if not num_samples.isnumeric():
        print("Number of samples must be an integer number.")
        sys.exit(1)
    num_samples = int(num_samples)
    loss_name = input("Enter the loss name (MSE, MAE, RMSE): ")
    for i in range(num_samples):
        predict = [random.uniform(0, 10) for _ in range(num_samples)]
        target = [random.uniform(0, 10) for _ in range(num_samples)]
        if loss_name == "MAE":
            loss = mae_loss(predict, target)
        elif loss_name == "MSE":
            loss = mse_loss(predict, target)
        elif loss_name == "RMSE":
            loss = rmse_loss(predict, target)
        print(f"{loss_name}, sample={i},predict={predict[i]},target={target[i]}, {loss}")

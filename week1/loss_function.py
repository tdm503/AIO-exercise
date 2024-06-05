import math
import random
def cal_ae(y,y_hat):
    return abs(y-y_hat)

def cal_se(y,y_hat):
    return (y-y_hat)*(y-y_hat)

def cal_mae(num_sample):
    sum = 0
    for i in range (num_sample):
        y = random.uniform(0,10)
        y_hat = random.uniform(0,10)
        sum += cal_ae(y,y_hat)
        print(f"MAE {i} {y} {y_hat} {cal_ae(y,y_hat)}")
    return sum/num_sample

def cal_mse(num_sample):
    sum = 0
    for i in range (num_sample):
        y = random.uniform(0,10)
        y_hat = random.uniform(0,10)
        sum += cal_se(y,y_hat)
        print(f"MSE {i} {y} {y_hat} {cal_se(y,y_hat)}")
    return sum/num_sample

def cal_loss_fun():
    num_sample = (input("enter number of samples "))
    if not num_sample.isnumeric():
        print("number of sample must be an integer number ")
        return
    num_sample = int(num_sample)
    loss_name = input("enter name of loss function")
    if loss_name == "MAE":
        res = cal_mae(num_sample)
    elif loss_name == "MSE":
        res = cal_mse(num_sample)
    
cal_loss_fun()


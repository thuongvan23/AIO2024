import random
import math


def calculate_loss(num_sample, name_loss_function):
    if not num_sample.isnumeric():
        print('number of samples must be an integer number')
        return

    num_sample = int(num_sample)

    predictions = []
    targets = []

    for i in range(num_sample):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        predictions.append(predict)
        targets.append(target)
        print(f'sample-{i}: predict={predict}, target={target}')

    if name_loss_function == 'MAE':
        loss = sum(abs(targets[i] - predictions[i]) for i in range(num_sample)) / num_sample
    elif name_loss_function == 'MSE':
        loss = sum((targets[i] - predictions[i]) ** 2 for i in range(num_sample)) / num_sample
    elif name_loss_function == 'RMSE':
        mse = sum((targets[i] - predictions[i]) ** 2 for i in range(num_sample)) / num_sample
        loss = math.sqrt(mse)

    try:
        print(f'{name_loss_function}: {name_loss_function} loss = {loss}')
    except:
        print(f'{name_loss_function} is not supported')


num_samples = input("Enter number of samples: ")
loss_function = input("Enter loss function name (MAE, MSE, RMSE): ")

calculate_loss(num_samples, loss_function)

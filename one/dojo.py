# https://www.jetbrains.com/pycharm/documentation/
import numpy as np
import math

def compute_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'ok'
    return result



if __name__ == '__main__':
    user_weight = float(input('Podaj wage [kg]: '))
    user_height = float(input('Podaj wzrost[m]: '))
    user_bmi = compute_bmi(user_weight, user_height)
    print(f'You are {user_bmi}.')
    a = np.zeros(4)
    print(a)

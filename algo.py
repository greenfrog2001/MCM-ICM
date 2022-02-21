import numpy as np
import random

subcourse_1 = [3, 5, 0]
subcourse_2 = [3, 0, 0]
subcourse_3 = [3, -6, 0]
subcourse_4 = [3, 0, 0]
subcourse_5 = [3, 5, 0]
subcourse_6 = [3, 0, 0]
subcourse_7 = [3, -10, 0]
subcourse_8 = [3, 0, 0]
subcourse_9 = [3, 6, 0]
subcourse_10 = [3, 0, 0]

course = [subcourse_1, subcourse_2, subcourse_3, subcourse_4, subcourse_5, subcourse_6, subcourse_7, subcourse_8, subcourse_9, subcourse_10]

# def get_T_end(m, p_0, alpha, x, sigma, v_0):
#     T_end = m/np.sqrt(p_0-m*np.sin(alpha))*(np.arccosh(np.exp((x-sigma)/m)) - np.arctanh(v_0/np.sqrt(p_0-m*np.sin(alpha))))
#     return T_end

def get_T_end(m, p_0, alpha, x):
    C = 50
    return C/m * ((p_0 - m*np.sin(alpha) + C) + np.sqrt((p_0 - m*np.sin(alpha) + C)**2 - 2*(C**2)/m - 2*C/m*x)) 

def tanh(x):
    return x + x**3/3

def cosh(x):
    return np.log(2**x) - 1 / (4*(x**2))

# def get_T_end(m, p_0, alpha, x, sigma, v_0):
#     # T_end = m/np.sqrt(p_0-m*np.sin(alpha))*(cosh(np.exp((x-sigma)/m)) - tanh(v_0/np.sqrt(p_0-m*np.sin(alpha))))
#     T_end = m/np.sqrt(p_0-m*np.sin(alpha))*(cosh(np.exp((x-sigma)/m)))
#     return T_end

def get_W_balance(W):
    pass

E_0 = 23*70
m = 70
LAMBDA = 5718
CRITICAL_POWER = 351
TAU = 316
V0 = 16
SIGMA = m/2.5

P_upper = E_0

# loops
n = 10
totalTime = 0
W_balance = 23000
P_list = []
for i in range(n):
    while True:
        print(W_balance)
        P = random.uniform(0.5*CRITICAL_POWER, P_upper)
        try:
            # T_end = get_T_end(m, P, course[i][1], course[i][0], SIGMA, V0)
            T_end = get_T_end(m, P, course[i][1], course[i][0])
        except RuntimeWarning:
            continue
        totalTime += T_end
        if P >= CRITICAL_POWER:
            print('P >= CP')
            new_W_balance = W_balance - totalTime*(P - CRITICAL_POWER)*np.exp(-T_end/TAU)
            if W_balance <= 0:
                print('W_balance <= 0')
                totalTime -= T_end
            else:
                print('W_balance > 0')
                W_balance = new_W_balance
                P_list.append(P)
                P_upper = LAMBDA/totalTime + CRITICAL_POWER
                break
        else:
            print('P < CP')
            W_balance += (CRITICAL_POWER - P)*np.exp(-T_end/TAU)
            P_list.append(P)
            P_upper = LAMBDA/totalTime + CRITICAL_POWER
            break

print(f'Total time: {totalTime}')
print(f'Power list: {P_list}')
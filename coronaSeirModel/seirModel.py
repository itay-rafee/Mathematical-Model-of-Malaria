import numpy as np

# delta - Efficacy of the vaccine on the population
#           if the effect
""" 
    if the affect of the vaccine is 100% then delta is 1 and the experssion turns to 0- no one new is infected
    if rhe affect of the vaccine is 0% then delta is 0 and the expression turn to 1-  meaningless (the equation is as before)
"""


def seir_model_with_soc_dist(init_vals, params, t, delta=0.3):
    S_0, E_0, I_0, R_0 = init_vals
    S, E, I, R = [S_0], [E_0], [I_0], [R_0]
    alpha, beta, gamma, rho = params
    dt = t[1] - t[0]
    for _ in t[1:]:
        next_S = S[-1] - (rho * beta * S[-1] * I[-1]) * dt
        next_E = E[-1] + (rho * beta * S[-1] * I[-1] - (1 - delta) * alpha * E[-1]) * dt
        next_I = I[-1] + ((1 - delta) * alpha * E[-1] - gamma * I[-1]) * dt
        next_R = R[-1] + (gamma * I[-1]) * dt
        S.append(next_S)
        E.append(next_E)
        I.append(next_I)
        R.append(next_R)
    return np.stack([S, E, I, R]).T

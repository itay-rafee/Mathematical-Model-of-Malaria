import numpy as np

# delta - Efficacy of the vaccine on the population
#           if the effect
""" 
    if the affect of the vaccine is 100% then delta is 1 and the experssion turns to 0 - no one new is infected
    if rhe affect of the vaccine is 0% then delta is 0 and the expression turn to 1 - meaningless (the equation is as before)
"""


def seir_ross_model(init_vals, params, t):
    Sh_0, Eh_0, Ih_0, Rh_0, Sm_0, Em_0, Im_0 = init_vals
    Sh, Eh, Ih, Rh = [Sh_0], [Eh_0], [Ih_0], [Rh_0]
    Sm, Em, Im = [Sm_0], [Em_0], [Im_0]
    a, b, c, m, r, mu2 = params
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
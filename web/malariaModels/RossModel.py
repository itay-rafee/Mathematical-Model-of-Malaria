import numpy as np


def ross_model(init_vals, params, t):
    Ih_0, Im_0 = init_vals
    Ih = [Ih_0]
    Im = [Im_0]
    a, b, c, m, r, mu2 = params
    for time_now in range(t):
        next_Ih = Ih[-1] + (a * b * m * Im[-1] * (1 - Ih[-1]) - (r * Ih[-1]))
        next_Im = Im[-1] + (a * c * Ih[-1] * (1 - Im[-1]) - (mu2 * Im[-1]))
        Ih.append(next_Ih)
        Im.append(next_Im)
    return np.stack([Ih, Im]).T


def reproductive_number(params):
    a, b, c, m, r, mu2 = params
    R0 = (m * (a ** 2) * b * c) / (r * mu2)
    return R0



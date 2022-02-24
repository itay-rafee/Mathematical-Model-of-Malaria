import numpy as np


def macdonald_model(init_vals, params, t):
    Ih_0, Em_0, Im_0 = init_vals
    Ih = [Ih_0]
    Em = [Em_0]
    Im = [Im_0]
    a, b, c, m, r, mu2, tau_m = params
    dt = t[1] - t[0]
    e2 = np.e ** (-mu2 * tau_m)
    for _ in range(250):
        t = _ - tau_m
        next_Ih = Ih[-1] + (a * b * m * Im[-1] * (1 - Ih[-1]) - (r * Ih[-1])) * dt
        if t < 0:
            next_Em = Em[-1] + (a * c * Ih[-1] * (1 - Em[-1] - Im[-1]) - mu2 * Em[-1]) * dt
            next_Im = Im[-1] + (- mu2 * Im[-1]) * dt
        else:
            next_Em = Em[-1] + (a * c * Ih[-1] * (1 - Em[-1] - Im[-1]) -
                                a * c * Ih[t] * (1 - Em[t] - Im[t]) * e2 - mu2 * Em[-1]) * dt
            next_Im = Im[-1] + (a * c * Ih[t] * (1 - Em[t] - Im[t]) * e2 - mu2 * Im[-1]) * dt
        Ih.append(next_Ih)
        Em.append(next_Em)
        Im.append(next_Im)
    return np.stack([Ih, Em, Im]).T


def reproductive_number(params):
    a, b, c, m, r, mu2, tau_m = params
    e2 = np.e ** (-mu2 * tau_m)
    R0 = (m * (a ** 2) * b * c * e2) / (r * mu2)
    return R0

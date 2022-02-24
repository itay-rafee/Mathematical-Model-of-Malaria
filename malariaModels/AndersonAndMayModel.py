import numpy as np


def anderson_and_may_model(init_vals, params, t):
    Eh_0, Ih_0, Em_0, Im_0 = init_vals
    Eh = [Eh_0]
    Ih = [Ih_0]
    Em = [Em_0]
    Im = [Im_0]
    a, b, c, m, r, mu1, mu2, tau_m, tau_h = params
    dt = t[1] - t[0]
    e1 = np.e ** (- (r + mu1) * tau_h)
    e2 = np.e ** (- mu2 * tau_m)
    for _ in range(250):
        tm = _ - tau_m
        th = _ - tau_h
        next_Eh = Eh[-1] + (a * b * m * Im[-1] * (1 - Eh[-1] - Ih[-1])
                            - a * b * m * Im[th] * (1 - Eh[th] - Ih[th]) * e1
                            - r * Eh[-1] - mu1 * Eh[-1]) * dt

        next_Ih = Ih[-1] + (a * b * m * Im[th] * (1 - Eh[th] - Ih[th]) * e1
                            - r * Ih[-1] - mu1 * Ih[-1]) * dt

        next_Em = Em[-1] + (a * c * Ih[-1] * (1 - Em[-1] - Im[-1])
                            - a * c * Ih[tm] * (1 - Em[tm] - Im[tm]) * e2 - mu2 * Em[-1]) * dt
        next_Im = Im[-1] + (a * c * Ih[tm] * (1 - Em[tm] - Im[tm]) * e2 - mu2 * Im[-1]) * dt

        Eh.append(next_Eh)
        Ih.append(next_Ih)
        Em.append(next_Em)
        Im.append(next_Im)
    return np.stack([Em, Ih, Em, Im]).T


def reproductive_number(params):
    a, b, c, m, r, mu1, mu2, tau_m, tau_h = params
    e1 = np.e ** (-mu2 * tau_m)
    e2 = np.e ** (-mu1 * tau_h)
    R0 = (m * (a ** 2) * b * c * e1 * e2) / (r * mu2)
    return R0

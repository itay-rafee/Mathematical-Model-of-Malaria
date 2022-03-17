from math import ceil

import numpy as np

def arnon_model(m_params, t):
    d, eta_m, eta_p, n_m, s, c_s, mos, hum = m_params
    c_total = s * c_s
    k = np.zeros((eta_p,), dtype=int)
    k[0] = n_m
    f = []
    eggs_total = 0

    for time_now in range(t):
        next_g = k[(time_now % eta_p)] * ceil(mos * (1 - d))
        g = f.copy()
        g.append(next_g)
        if time_now - eta_m - 1 >= 0:
            eggs_total = sum(g[time_now - eta_m - 1:])
        else:
            eggs_total = sum(g)
        print("befor"+str(eggs_total))
        p = eggs_total - c_total
        f.append(next_g)
        if p > 0:
            for i in range(eta_m):
                f[time_now - i] = g[time_now - i] - ceil((g[time_now - i] * p) / eggs_total)

        mos = ceil(mos * (1 - d))
        if time_now - eta_m >= 0:
            mos += f[time_now - eta_m]
        if time_now - eta_m - 1 >= 0:
            eggs_total = sum(f[time_now - eta_m - 1:])
        else:
            eggs_total = sum(f)
        print("after"+str(eggs_total))
        # print(f"{time_now}: {mos}")
        # print(str(time_now)+": " + str(mos))


params_m = 0.05, 12, 4, 3, 100, 300, 2000, 100
arnon_model(params_m, 100)
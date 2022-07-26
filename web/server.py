from flask import Flask, render_template, request, redirect, Response
import csv

app = Flask(__name__)

import io
import base64
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from malariaModels.AndersonAndMayModel import anderson_and_may_model
from malariaModels.MacdonaldModel import macdonald_model
from malariaModels.RossModel import ross_model

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/index.html')
def main_page2():
    return render_template('modal.html')


##################################

# def plot_png():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = np.random.rand(100)
#     ys = np.random.rand(100)
#     axis.plot(xs, ys)
#     output = io.BytesIO()
#     FigureCanvas(fig).print_png(output)
#     return Response(output.getvalue(), mimetype='image/png')

# def plot_png():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = np.random.rand(100)
#     ys = np.random.rand(100)
#     axis.plot(xs, ys)
#     output = io.BytesIO()
#     # FigureCanvas(fig).print_png(output)
#     # return Image.open(output)
#     axis.figure.savefig(output, format="png")
#     #FigureCanvas(fig).print_png(output)
#     output.seek(0)
#     image_memory = base64.b64encode(output.getvalue())
#     return image_memory
#     #FigureCanvas(fig).print_png(output)
#     #return Response(output.getvalue(), mimetype='image/png')


def plot_png(data):
    fig = Figure()
    t = 250
    # a, b, c, m, r, mu1, mu2, tau_m, tau_h = 0.2, 0.5, 0.5, 20, 0.01, 0.017, 0.12, 10, 21
    # d, eta_m, eta_p, n_m, s, c_s, mos, hum = 0.05, 12, 4, 3, 100, 300, 5000, 100
    a, b, c, m, r = float(data["a"]), float(data["b"]), float(data["c"]), int(data["m"]), float(data["r"])
    mu1, mu2, tau_m, tau_h = float(data["mu1"]), float(data["mu2"]), int(data["tau_m"]), int(data["tau_h"])
    d, eta_m, eta_p, n_m = float(data["d"]), int(data["eta_m"]), int(data["eta_p"]), int(data["n_m"])
    s, c_s, mos, hum = int(data["s"]), int(data["c_s"]), int(data["mos"]), int(data["hum"])
    # ====== Ross Model ======
    params = a, b, c, m, r, mu2
    init_val = 0.0015, 0
    RR = ross_model(init_val, params, t)

    R_Ih = []
    R_Im = []
    for i in RR:
        R_Ih.append(i[0])
        R_Im.append(i[1])

    # ====== Macdonald Model ======
    params = a, b, c, m, r, mu2, tau_m
    init_val = 0.0015, 0, 0
    MC = macdonald_model(init_val, params, t)

    M_Ih = []
    M_Im = []
    for i in MC:
        M_Ih.append(i[0])
        M_Im.append(i[2])

    # ====== Anderson and May Model ======
    params = a, b, c, m, r, mu1, mu2, tau_m, tau_h
    init_val = 0, 0.0015, 0, 0
    AM = anderson_and_may_model(init_val, params, t)

    A_Ih = []
    A_Im = []
    for i in AM:
        A_Ih.append(i[1])
        A_Im.append(i[3])

    # # ====== Arnon Model ======
    # params = a, b, c, r, mu1, mu2, tau_m, tau_h
    # m_params = mu2, eta_m, eta_p, n_m, s, c_s, mos, hum
    # init_val = 0, 0.0015, 0, 0
    # AR = arnon_model(init_val, params, m_params, t)

    # AR_Ih = []
    # AR_Im = []
    # for i in AR:
    #     AR_Ih.append(i[1])
    #     AR_Im.append(i[3])

    # ====== Print on chart ======
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(R_Ih, 'b', label='RR Ih')
    axis.plot(R_Im, '--b', label='RR Im')

    axis.plot(M_Ih, 'g', label='MC Ih')
    axis.plot(M_Im, '--g', label='MC Im')

    axis.plot(A_Ih, 'r', label='AM Ih')
    axis.plot(A_Im, '--r', label='AM Im')

    # axis.plot(AR_Ih, 'y', label='AR Ih')
    # axis.plot(AR_Im, '--y', label='AR Im')

    axis.legend()
    # naming the x axis
    axis.set_xlabel('time')
    # naming the y axis
    axis.set_ylabel('Prevalence')

    # giving a title to my graph
    # plt.title('Mathematical models of malaria')

    # function to show the plot
    output = io.BytesIO()
    axis.figure.savefig(output, format="png")
    output.seek(0)
    image_memory = base64.b64encode(output.getvalue())
    return image_memory


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        rend_image = plot_png(data).decode('utf-8')
        return render_template('modal.html', rendered_image=rend_image)


# return plot_png()

@app.route('/modal')
def modal_page():
    # print(plot_png2().width())
    rend_image = plot_png().decode('utf-8')
    return render_template('modal.html', rendered_image=rend_image)

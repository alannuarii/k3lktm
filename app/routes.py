from turtle import title
from app import app
from flask import render_template
from app.models.lb3 import LB3


@app.route('/')
def index():
    # title = 'Beranda'
    return render_template('pages/home.html', title='Home | K3L KTM', active_home='active')


@app.route('/lb3-converter')
def lb3():
    list_lb3 = LB3.query.all()
    list_konstanta = []
    satuan = []
    for i in range(len(list_lb3)):
        list_konstanta.append(list_lb3[i].konstanta)
        satuan.append(list_lb3[i].satuan_awal)

    return render_template('pages/lb3-converter.html', title='LB3 Converter | K3L KTM', active_lb3='active', list_lb3 = list_lb3, list_konstanta = list_konstanta, satuan = satuan)



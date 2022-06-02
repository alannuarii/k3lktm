from turtle import title
from app import app
from flask import render_template
from app.models.lb3 import LB3


@app.route('/')
def index():

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


@app.route('/logbook')
def logbook():

    return render_template('pages/logbook.html', title='LogBook | K3L KTM', active_logbook='active')


@app.route('/logbook/limbah-domestik/debit')
def debit_domestik():

    return render_template('pages/debit-domestik.html', title='Debit Limbah Domestik | K3L KTM', active_logbook='active')


@app.route('/logbook/sludge')
def sludge():

    return render_template('pages/sludge.html', title='Sludge | K3L KTM', active_logbook='active')


@app.route('/logbook/oli-bekas')
def oli_bekas():

    return render_template('pages/oli-bekas.html', title='Oli Bekas | K3L KTM', active_logbook='active')


@app.route('/logbook/filter-bekas')
def filter_bekas():

    return render_template('pages/filter-bekas.html', title='Filter Bekas | K3L KTM', active_logbook='active')


@app.route('/logbook/majun-bekas')
def majun_bekas():

    return render_template('pages/majun-bekas.html', title='Majun Bekas | K3L KTM', active_logbook='active')
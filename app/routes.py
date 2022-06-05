from datetime import datetime
from turtle import title
from app import app
from app import db
from flask import render_template, request, redirect, url_for
from app.models.lb3 import LB3
from app.models.sludge import Sludge
from app.models.oli_bekas import OliBekas
from app.models.filter_bekas import FilterBekas
from app.models.majun_bekas import MajunBekas
from app.models.debit_proses import DebitProses
from app.models.ph_proses import PHProses
from app.models.debit_domestik import DebitDomestik
from app.models.ph_domestik import PHDomestik
import socket
import os
from werkzeug.utils import secure_filename
from googletrans import Translator



@app.route('/')
def index():
    hostname = socket.gethostname()
    ip = str(socket.gethostbyname(hostname))
    return render_template('pages/home.html', title='Home | K3L KTM', active_home='active', ip = ip)


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
    query = request.args.get('bulan')
    debit = DebitDomestik.query.filter_by(bulan=query).all()
    if query:
        query_datetime = datetime.strptime(query, '%Y-%m')
        bulan = query_datetime.strftime('%B')
        tahun = query_datetime.strftime('%Y')
        result = Translator().translate(bulan, src='en', dest='id')
        return render_template('pages/debit-domestik.html', title='Debit Limbah Domestik | K3L KTM', active_logbook='active', debits=debit, bulan=result.text, tahun=tahun)
    return render_template('pages/debit-domestik.html', title='Debit Limbah Domestik | K3L KTM', active_logbook='active', debits=debit)


@app.route('/logbook/input-ppa', methods=['GET', 'POST'])
def input_ppa():
    if request.method == 'POST':
        if request.form['ppa'] == 'debitproses':
            tanggal = request.form['tanggal']
            debit = request.form['debit']
            bulan = request.form['bulan'][:7]
            debitproses = DebitProses(tanggal=tanggal, debit=debit, bulan=bulan)
            db.session.add(debitproses)
            db.session.commit()
            return redirect(url_for('input_ppa'))
        elif request.form['ppa'] == 'phproses':
            tanggal = request.form['tanggal']
            ph = request.form['ph']
            bulan = request.form['bulan'][:7]
            phproses = PHProses(tanggal=tanggal, ph=ph, bulan=bulan)
            db.session.add(phproses)
            db.session.commit()
            return redirect(url_for('input_ppa'))
        elif request.form['ppa'] == 'debitdomestik':
            tanggal = request.form['tanggal']
            debit = request.form['debit']
            bulan = request.form['bulan'][:7]
            debitdomestik = DebitDomestik(tanggal=tanggal, debit=debit, bulan=bulan)
            db.session.add(debitdomestik)
            db.session.commit()
            return redirect(url_for('input_ppa'))
        elif request.form['ppa'] == 'phdomestik':
            tanggal = request.form['tanggal']
            ph = request.form['ph']
            bulan = request.form['bulan'][:7]
            phdomestik = PHDomestik(tanggal=tanggal, ph=ph, bulan=bulan)
            db.session.add(phdomestik)
            db.session.commit()
            return redirect(url_for('input_ppa'))
    return render_template('pages/input-ppa.html', title='Input Data Harian | K3L KTM', active_logbook='active')


@app.route('/logbook/sludge', methods=['GET', 'POST'])
def sludge():
    list_sludge = Sludge.query.all()
    if request.method == 'POST':
        if request.files:
            tanggal = request.form['tanggal']
            keluar = request.form['keluar']
            manifest = request.files['manifest']
            filename = secure_filename(manifest.filename)
            renamefile = 'Sludge-'+filename
            manifest.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            sludge = Sludge(tanggal=tanggal, keluar=keluar, manifest=renamefile)
            db.session.add(sludge)
            db.session.commit()
            return redirect(url_for('sludge'))
        else:
            tanggal = request.form['tanggal']
            masuk = request.form['masuk'] 
            sludge = Sludge(tanggal=tanggal, masuk=masuk)
            db.session.add(sludge)
            db.session.commit()
            return redirect(url_for('sludge'))
    return render_template('pages/sludge.html', title='Sludge | K3L KTM', active_logbook='active', sludges=list_sludge)


@app.route('/logbook/oli-bekas', methods=['GET', 'POST'])
def oli_bekas():
    list_oli_bekas = OliBekas.query.all()
    if request.method == 'POST':
        if request.files:
            tanggal = request.form['tanggal']
            keluar = float(request.form['keluar']) 
            manifest = request.files['manifest']
            filename = secure_filename(manifest.filename)
            renamefile = 'OliBekas-'+filename
            manifest.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            oli_bekas = OliBekas(tanggal=tanggal, keluar=keluar, manifest=renamefile)
            db.session.add(oli_bekas)
            db.session.commit()
            return redirect(url_for('oli_bekas'))
        else:
            tanggal = request.form['tanggal']
            masuk = float(request.form['masuk']) 
            oli_bekas = OliBekas(tanggal=tanggal, masuk=masuk)
            db.session.add(oli_bekas)
            db.session.commit()
            return redirect(url_for('oli_bekas'))
    return render_template('pages/oli-bekas.html', title='Oli Bekas | K3L KTM', active_logbook='active', oli_bekas=list_oli_bekas)


@app.route('/logbook/filter-bekas', methods=['GET', 'POST'])
def filter_bekas():
    list_filter_bekas = FilterBekas.query.all()
    if request.method == 'POST':
        if request.files:
            tanggal = request.form['tanggal']
            keluar = float(request.form['keluar']) 
            manifest = request.files['manifest']
            filename = secure_filename(manifest.filename)
            renamefile = 'FilterBekas-'+filename
            manifest.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            filter_bekas = FilterBekas(tanggal=tanggal, keluar=keluar, manifest=renamefile)
            db.session.add(filter_bekas)
            db.session.commit()
            return redirect(url_for('filter_bekas'))
        else:
            tanggal = request.form['tanggal']
            masuk = float(request.form['masuk']) 
            filter_bekas = FilterBekas(tanggal=tanggal, masuk=masuk)
            db.session.add(filter_bekas)
            db.session.commit()
            return redirect(url_for('filter_bekas'))
    return render_template('pages/filter-bekas.html', title='Filter Bekas | K3L KTM', active_logbook='active', filter_bekas=list_filter_bekas)


@app.route('/logbook/majun-bekas', methods=['GET', 'POST'])
def majun_bekas():
    list_majun_bekas = MajunBekas.query.all()
    if request.method == 'POST':
        if request.files:
            tanggal = request.form['tanggal']
            keluar = float(request.form['keluar']) 
            manifest = request.files['manifest']
            filename = secure_filename(manifest.filename)
            renamefile = 'MajunBekas-'+filename
            manifest.save(os.path.join(app.config['UPLOAD_FOLDER'], renamefile))
            majun_bekas = MajunBekas(tanggal=tanggal, keluar=keluar, manifest=renamefile)
            db.session.add(majun_bekas)
            db.session.commit()
            return redirect(url_for('majun_bekas'))
        else:
            tanggal = request.form['tanggal']
            masuk = float(request.form['masuk']) 
            majun_bekas = MajunBekas(tanggal=tanggal, masuk=masuk)
            db.session.add(majun_bekas)
            db.session.commit()
            return redirect(url_for('majun_bekas'))
    return render_template('pages/majun-bekas.html', title='Majun Bekas | K3L KTM', active_logbook='active', majun_bekas=list_majun_bekas)
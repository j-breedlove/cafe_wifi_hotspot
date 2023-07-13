from flask import render_template, redirect, url_for
from app import app, db
from app.forms.hotspot_form import HotspotForm
from app.models.hotspot import Hotspot


@app.route('/')
def index():
    hotspots = Hotspot.query.all()
    return render_template('index.html', hotspots=hotspots)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = HotspotForm()
    if form.validate_on_submit():
        hotspot = Hotspot(name=form.name.data, wifi_quality=form.wifi_quality.data, power_rating=form.power_rating.data)
        db.session.add(hotspot)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_hotspot.html', form=form)

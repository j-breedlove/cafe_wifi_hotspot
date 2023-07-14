from flask import render_template, redirect, url_for, flash
from app import app, db
from app.forms.hotspot_form import HotspotForm
from app.models.hotspot import Hotspot


@app.route('/')
def index():
    """
        Index route. Fetches all hotspots from the database and renders them in the index template.

        :return: Rendered index template with all hotspots.
        """
    hotspots = Hotspot.query.all()
    return render_template('index.html', hotspots=hotspots)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
        Add route. Handles both GET and POST requests. If the method is POST and the form is valid,
        adds a new hotspot to the database, commits the session, flashes a success message and
        redirects to the index page.

        :return: Rendered add_hotspot template with form or redirect to index page.
        """
    form = HotspotForm()

    if form.validate_on_submit():
        hotspot = Hotspot(
            name=form.name.data,
            wifi_quality=form.wifi_quality.data,
            power_rating=form.power_rating.data
        )

        db.session.add(hotspot)
        db.session.commit()

        flash('Hotspot added')
        return redirect(url_for('index'))

    return render_template('add_hotspot.html', form=form)


@app.route('/delete/<int:hotspot_id>', methods=['POST'])
def delete(hotspot_id):
    """
        Delete route. Deletes a hotspot with the given ID from the database, commits the session,
        flashes a success message and redirects to the index page.

        :param hotspot_id: ID of the hotspot to be deleted.
        :return: Redirect to index page.
        """
    hotspot = Hotspot.query.get_or_404(hotspot_id)

    db.session.delete(hotspot)
    db.session.commit()

    flash('Hotspot deleted')
    return redirect(url_for('index'))

# Coffee and Wifi
![coffe_wifi_index.png](app%2Fstatic%2Fimg%2Fcoffe_wifi_index.png)
![coffe_wifi_add.png](app%2Fstatic%2Fimg%2Fcoffe_wifi_add.png)
A Flask web application that allows users to enter various wifi hotspots by name, the quality of the wifi, and whether or not they have power for computers. Wifi and power should be measured on a scale of 1 to 5.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/coffee-and-wifi.git
    ```
2. Change into the project directory:
    ```
    cd coffee-and-wifi
    ```
3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```
4. Set up the database:
    ```
    python
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

## Usage

1. Run the application:
    ```
    python run.py
    ```
2. Open a web browser and navigate to `http://localhost:5000`.

## Contributing

Please open an issue to discuss the changes you would like to make. Contributions are welcome!

## Code

The main application code is in `app/views.py`:

```python
from flask import render_template, redirect, url_for, flash
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
    hotspot = Hotspot.query.get_or_404(hotspot_id)
    db.session.delete(hotspot)
    db.session.commit()
    flash('Hotspot deleted')
    return redirect(url_for('index'))
```
```

Please replace `https://github.com/yourusername/coffee-and-wifi.git` with the actual URL of your GitHub repository. The installation and usage instructions might also need to be adjusted based on your project's specific requirements and setup.
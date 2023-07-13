from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class HotspotForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    wifi_quality = IntegerField('Wifi Quality', validators=[DataRequired(), NumberRange(min=1, max=5)])
    has_power = BooleanField('Has Power')
    submit = SubmitField('Add Hotspot')
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange


class HotspotForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    wifi_quality = SelectField('Wifi Rating',
                               choices=[('None', 'None'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'),
                                        ('💪💪💪💪💪', '💪💪💪💪💪')], validators=[DataRequired()], default='None')
    power_rating = SelectField('Power Rating', choices=[('None', 'None'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                                                        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')],
                               validators=[DataRequired()], default='None')
    submit = SubmitField('Add Hotspot')

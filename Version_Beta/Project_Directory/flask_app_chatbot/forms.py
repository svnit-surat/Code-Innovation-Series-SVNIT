from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class Message(FlaskForm):
    message = StringField('Your answer:', validators=[DataRequired()])
    submit = SubmitField('Send')
    clear = SubmitField('Clear')

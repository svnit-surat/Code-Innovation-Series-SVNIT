from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class Message(FlaskForm):
    message = StringField('answer', validators=[DataRequired()])
    submit = SubmitField('send')
    clear = SubmitField('clear')
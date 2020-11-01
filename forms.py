from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class PersonalExpenses(FlaskForm):
    description = StringField('description', validators=[DataRequired()])
    amount = IntegerField('amount', validators=[DataRequired()])

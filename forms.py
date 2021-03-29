from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.fields.core import BooleanField
from wtforms.validators import InputRequired, Length, Optional, NumberRange, URL


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(),URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes', render_kw={"rows": 4, "cols": 50})

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(),URL()])
    notes = TextAreaField('Notes', render_kw={"rows": 4, "cols": 50})
    available = BooleanField("Available")
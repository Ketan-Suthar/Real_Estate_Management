from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed
# from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class RegisterVO(FlaskForm):
    registerId = IntegerField('registerId')
    register_LoginId = IntegerField('register_LoginId')
    registerFirstName = StringField('First Name',validators=[DataRequired(),Length(min=20,max=30)])
    registerLastName = StringField('registerLastName',validators=[DataRequired(),Length(min=1,max=30)])
    registerContact = IntegerField('registerContact',validators=[DataRequired(),Length(min=10,max=10)])
    registerDate = StringField('registerDate')
    registerTime = StringField('registerTime')
    registerActiveStatus = StringField('registerActiveStatus')
    registerSubmit = SubmitField('Sign Up')
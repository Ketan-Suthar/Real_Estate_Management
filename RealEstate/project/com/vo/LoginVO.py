from wtforms import IntegerField, StringField

class LoginVO():
    loginPassword = StringField
    loginRole = StringField
    loginId=IntegerField
    loginEmailId = StringField
    loginActiveStatus = StringField

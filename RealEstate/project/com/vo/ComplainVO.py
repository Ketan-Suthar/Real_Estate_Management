from wtforms import IntegerField, StringField

class ComplainVO():

    complainId = IntegerField
    complainSubject = StringField
    complainDescription = StringField
    complainTo_LoginId = IntegerField
    complainFrom_LoginId = IntegerField
    complainDate = StringField
    complainTime = StringField
    complainReply = StringField
    complainStatus = StringField
    complainActiveStatus = StringField

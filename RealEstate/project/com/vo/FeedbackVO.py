from wtforms import IntegerField, StringField


class FeedbackVO():
    feedbackId = IntegerField
    feedbackMessage = StringField
    feedbackTo_LoginId = IntegerField
    feedbackFrom_LoginId = IntegerField
    feedbackRating = StringField
    feedbackDate = StringField
    feedbackTime = StringField
    feedbackActiveStatus = StringField
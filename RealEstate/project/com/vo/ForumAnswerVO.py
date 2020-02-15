from wtforms import IntegerField, StringField

class ForumAnswerVO():
    forumAnswerId = IntegerField
    forumAnswer_LoginId = IntegerField
    forumAnswer_ForumQuestionId = IntegerField
    forumAnswer = StringField
    forumAnswerDate = StringField
    forumAnswerTime = StringField
    forumAnswerActiveStatus = StringField
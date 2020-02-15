from wtforms import IntegerField, StringField, BooleanField

class ForumQuestionVO():

    forumQuestionId = IntegerField
    forumQuestion_LoginId = IntegerField
    forumQuestion = StringField
    forumQuestionDiscussion = BooleanField
    forumQuestionDate = StringField
    forumQuestionTime = StringField
    forumQuestionActiveStatus = StringField
from wtforms import *

class PropertyReviewVO():
    propertyReviewId = IntegerField
    propertyReview_PropertyId = IntegerField
    propertyReview_LoginId = IntegerField
    propertyReviewDescription = StringField
    propertyReviewRating = IntegerField
    propertyReviewDate = StringField
    propertyReviewTime = StringField
    propertyReviewActiveStatus = StringField
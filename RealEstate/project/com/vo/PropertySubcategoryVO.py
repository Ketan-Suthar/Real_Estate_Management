from wtforms import *


class PropertySubcategoryVO():

    propertySubcategoryName =StringField
    propertySubcategoryDescription = StringField
    propertySubcategory_PropertyCategoryId=IntegerField
    propertySubcategoryActiveStatus = StringField
    propertySubcategoryId = IntegerField
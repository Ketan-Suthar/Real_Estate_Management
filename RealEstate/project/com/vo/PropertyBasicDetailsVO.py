from wtforms import IntegerField, StringField

class PropertyBasicDetailsVO():
    propertyId = IntegerField
    property_LoginId = IntegerField
    propertyOwnerType = StringField
    propertyListFor = StringField
    property_PropertyCategoryId = IntegerField
    property_PropertySubcategoryId = IntegerField
    propertyDate = StringField
    propertyTime = StringField
    propertyAtStep = StringField
    propertyStatus = StringField
    propertyAdminReply = StringField
    propertyActiveStatus = StringField

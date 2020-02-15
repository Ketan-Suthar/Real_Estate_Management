from wtforms import IntegerField, StringField

class PropertyAddressVO():
    propertyAddressId = IntegerField
    propertyAddress_PropertyId = IntegerField
    propertyStreet = StringField
    propertyLocality = StringField
    propertyStateId = IntegerField
    propertyCityId = IntegerField
    propertyPincode = IntegerField
    propertyAddressDate = StringField
    propertyAddressTime = StringField
    propertyAddressActiveStatus = StringField
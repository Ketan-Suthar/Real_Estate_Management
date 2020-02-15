from wtforms import IntegerField, StringField

class PropertyAmenitiesVO():
    propertyAmenitiesId = IntegerField
    propertyAmenities_PropertyId = IntegerField
    propertyAmenities = StringField
    propertyAmenitiesDate = StringField
    propertyAmenitiesTime = StringField
    propertyAmenitiesActiveStatus = StringField
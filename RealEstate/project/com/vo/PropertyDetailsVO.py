from wtforms import IntegerField, StringField

class PropertyDetailsVO():

    propertyDetailsId = IntegerField
    propertyDetails_PropertyId = IntegerField
    propertyName = StringField
    propertyRERANo = StringField
    propertyBuildUpArea = IntegerField
    propertyBuildUpAreaUnit = StringField
    propertyBedrooms = IntegerField
    propertyBathrooms = IntegerField
    propertyBalconies = IntegerField
    propertyWashrooms = IntegerField
    propertyOtherRooms = StringField
    propertyQualityRating = StringField
    propertyTotalRooms = IntegerField
    propertyFurnishing = StringField
    propertyOnFloor = IntegerField
    propertyTotalFloors= IntegerField
    propertyParking = StringField
    propertyDescription = StringField
    propertyDetailsDate = StringField
    propertyDetailsTime = StringField
    propertyDetailsActiveStatus = StringField
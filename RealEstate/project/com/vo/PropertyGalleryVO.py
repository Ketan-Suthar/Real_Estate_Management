from wtforms import IntegerField, StringField

class PropertyGalleryVO():
    propertyGalleryId = IntegerField
    propertyGallery_PropertyId = IntegerField
    propertyGalleryPath = StringField
    propertyVideo = StringField
    property360Image = StringField
    propertyGalleryDate = StringField
    propertyGalleryTime = StringField
    propertyGalleryActiveStatus = StringField
from wtforms import *

class PropertyPricingVO():
    propertyPricingId = IntegerField
    propertyPricing_PropertyId = IntegerField
    propertyPrice = IntegerField
    propertyMonthlyRent = IntegerField
    propertyPricingDate = StringField
    propertyPricingTime = StringField
    propertyPricingActiveStatus = StringField

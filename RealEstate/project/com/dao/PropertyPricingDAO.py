from project.com.dao import *

class PropertyPricingDAO:

    def insertPropertyPricing(self,PropertyPricingVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO propertypricingmaster \
        (propertyPricing_PropertyId,propertyPrice,propertyMonthlyRent,\
        propertyPricingDate,propertyPricingTime,\
        propertyPricingActiveStatus) VALUES \
        ('{}','{}','{}','{}','{}','{}')".format\
        (PropertyPricingVO.propertyPricing_PropertyId,\
         PropertyPricingVO.propertyPrice,\
         PropertyPricingVO.propertyMonthlyRent,\
         PropertyPricingVO.propertyPricingDate,\
         PropertyPricingVO.propertyPricingTime,\
         PropertyPricingVO.propertyPricingActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()
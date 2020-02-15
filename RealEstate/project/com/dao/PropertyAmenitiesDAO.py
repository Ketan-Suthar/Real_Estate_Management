from project.com.dao import *

class PropertyAmenitiesDAO:

    def insertPropertyAmenities(self,propertyAmenitiesVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO propertyamenitiesmaster (propertyAmenities_PropertyId,\
          propertyAmenities,propertyAmenitiesDate,propertyAmenitiesTime,\
          propertyAmenitiesActiveStatus)\
           VALUE ('{}','{}','{}','{}','{}')".format\
                (propertyAmenitiesVO.propertyAmenities_PropertyId,\
                 propertyAmenitiesVO.propertyAmenities, \
                 propertyAmenitiesVO.propertyAmenitiesDate, \
                 propertyAmenitiesVO.propertyAmenitiesTime,\
                propertyAmenitiesVO.propertyAmenitiesActiveStatus))


        connection.commit()

        cursor1.close()
        connection.close()
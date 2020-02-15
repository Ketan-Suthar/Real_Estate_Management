from project.com.dao import *

class PropertyAddressDAO:

    def insertPropertyAddress(self,propertyAddressVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO propertyaddressmaster (propertyAddress_PropertyId,\
          propertyStreet,propertyLocality,propertyStateId,\
          propertyCityId,propertyPincode,propertyAddressDate,\
          propertyAddressTime,propertyAddressActiveStatus) VALUE\
          ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format\
                (propertyAddressVO.propertyAddress_PropertyId,\
                 propertyAddressVO.propertyStreet, \
                 propertyAddressVO.propertyLocality,\
                 propertyAddressVO.propertyStateId, \
                 propertyAddressVO.propertyCityId,propertyAddressVO.propertyPincode, \
                 propertyAddressVO.propertyAddressDate,propertyAddressVO.propertyAddressTime,\
                 propertyAddressVO.propertyAddressActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()
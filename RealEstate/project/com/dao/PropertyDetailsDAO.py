from project.com.dao import *

class PropertyDetailsDAO:

    def insertPropertyDetailsLand(self,propertyDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO propertydetailsmaster (propertyDetails_PropertyId,\
        propertyBuildUpArea,propertyBuildUpAreaUnit,propertyDescription,\
        propertyDetailsDate,propertyDetailsTime,propertyDetailsActiveStatus)\
            VALUES ('{}','{}','{}','{}','{}','{}','{}') ".format\
                (propertyDetailsVO.propertyDetails_PropertyId,\
                 propertyDetailsVO.propertyBuildUpArea,\
                 propertyDetailsVO.propertyBuildUpAreaUnit, \
                 propertyDetailsVO.propertyDescription, \
                 propertyDetailsVO.propertyDetailsDate, \
                 propertyDetailsVO.propertyDetailsTime,\
                 propertyDetailsVO.propertyDetailsActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def insertPropertyDetailsHotel(self,propertyDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO propertydetailsmaster (propertyDetails_PropertyId,\
            propertyName,propertyRERANo,propertyQualityRating,\
            propertyWashrooms,propertyTotalRooms,propertyOtherRooms,\
        propertyParking,\
        propertyBuildUpArea,propertyBuildUpAreaUnit,propertyDescription,\
        propertyDetailsDate,propertyDetailsTime,propertyDetailsActiveStatus)\
            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}') ".format\
                (propertyDetailsVO.propertyDetails_PropertyId, \
                 propertyDetailsVO.propertyName,\
                propertyDetailsVO.propertyRERANo,\
                propertyDetailsVO.propertyQualityRating,\
                propertyDetailsVO.propertyWashrooms,\
                propertyDetailsVO.propertyTotalRooms,\
                propertyDetailsVO.propertyOtherRooms,\
                propertyDetailsVO.propertyParking,\
                 propertyDetailsVO.propertyBuildUpArea,\
                 propertyDetailsVO.propertyBuildUpAreaUnit, \
                 propertyDetailsVO.propertyDescription, \
                 propertyDetailsVO.propertyDetailsDate, \
                 propertyDetailsVO.propertyDetailsTime,\
                 propertyDetailsVO.propertyDetailsActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def insertPropertyDetailsCommercial(self,propertyDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO propertydetailsmaster (propertyDetails_PropertyId,\
            propertyName,propertyRERANo,propertyWashrooms,propertyParking,\
        propertyBuildUpArea,propertyBuildUpAreaUnit,propertyDescription,\
        propertyDetailsDate,propertyDetailsTime,propertyDetailsActiveStatus)\
            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format\
                (propertyDetailsVO.propertyDetails_PropertyId, \
                 propertyDetailsVO.propertyName,\
                propertyDetailsVO.propertyRERANo,\
                propertyDetailsVO.propertyWashrooms,\
                propertyDetailsVO.propertyParking,\
                 propertyDetailsVO.propertyBuildUpArea,\
                 propertyDetailsVO.propertyBuildUpAreaUnit,\
                 propertyDetailsVO.propertyDescription,\
                 propertyDetailsVO.propertyDetailsDate,\
                 propertyDetailsVO.propertyDetailsTime,\
                 propertyDetailsVO.propertyDetailsActiveStatus))
        connection.commit()
        cursor1.close()
        connection.close()

    def insertPropertyDetailsResidential(self,propertyDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO propertydetailsmaster (propertyDetails_PropertyId,\
            propertyName,propertyRERANo,propertyBedrooms,propertyBathrooms,\
            propertyBalconies,propertyOtherRooms,\
        propertyFurnishing,propertyOnFloor,propertyTotalFloors,propertyParking,\
        propertyBuildUpArea,propertyBuildUpAreaUnit,propertyDescription,\
        propertyDetailsDate,propertyDetailsTime,propertyDetailsActiveStatus)\
            VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format\
                (propertyDetailsVO.propertyDetails_PropertyId,propertyDetailsVO.propertyName,\
                propertyDetailsVO.propertyRERANo,propertyDetailsVO.propertyBedrooms, \
                 propertyDetailsVO.propertyBathrooms,propertyDetailsVO.propertyBalconies,\
                 propertyDetailsVO.propertyOtherRooms,propertyDetailsVO.propertyFurnishing, \
                 propertyDetailsVO.propertyOnFloor,propertyDetailsVO.propertyTotalFloors,\
                 propertyDetailsVO.propertyParking,\
                 propertyDetailsVO.propertyBuildUpArea,\
                 propertyDetailsVO.propertyBuildUpAreaUnit,\
                 propertyDetailsVO.propertyDescription, \
                 propertyDetailsVO.propertyDetailsDate, \
                 propertyDetailsVO.propertyDetailsTime,\
                 propertyDetailsVO.propertyDetailsActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

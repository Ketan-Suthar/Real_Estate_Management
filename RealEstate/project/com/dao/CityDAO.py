from project.com.dao import *

class CityDAO:

    def insertCity(self,cityVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO citymaster (cityName,cityDescription,city_StateId,cityActiveStatus) VALUES ('{}','{}','{}','{}')".format(cityVO.cityName,cityVO.cityDescription,cityVO.city_StateId,cityVO.cityActiveStatus))

        # cursor1.execute(
        #         'INSERT INTO %s (cityName,cityDescription,city_StateId) VALUES (\'%s\',\'%s\',\'%s\')' \
        #         % ('citymaster', cityVO.cityName,cityVO.cityDescription,cityVO.city_StateId))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchCity(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from citymaster inner join statemaster on city_StateId = stateId WHERE cityActiveStatus='active' AND StateActiveStatus='active' ")
        cityDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return cityDict

    def updateCity(self,cityVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE citymaster SET cityName='{}', cityDescription='{}',city_StateId='{}' WHERE cityId ='{}' ".format(cityVO.cityName, cityVO.cityDescription,cityVO.city_StateId,cityVO.cityId))

        connection.commit()
        cursor1.close()
        connection.close()

    def deleteCity(self,cityVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE citymaster SET cityActiveStatus='{}' WHERE cityId = '{}' " .format(cityVO.cityActiveStatus,cityVO.cityId))
        connection.commit()
        cursor1.close()
        connection.close()

    def editCity(self,cityVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from citymaster inner join statemaster on city_StateId = stateId WHERE cityId ='{}' ".format(cityVO.cityId))
        cityDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return cityDict
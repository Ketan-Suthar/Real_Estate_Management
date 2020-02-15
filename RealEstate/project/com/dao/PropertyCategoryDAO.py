from project.com.dao import *

class PropertyCategoryDAO:

    def insertPropertyCategory(self,propertyCategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO propertycategorymaster (propertyCategoryName,propertyCategoryDescription,propertyCategoryActiveStatus) VALUES ('{}','{}','{}') ".format(propertyCategoryVO.propertyCategoryName,propertyCategoryVO.propertyCategoryDescription,propertyCategoryVO.propertyCategoryActiveStatus))


        connection.commit()
        cursor1.close()
        connection.close()

    def searchPropertyCategory(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from propertycategorymaster WHERE propertyCategoryActiveStatus='active' ")
        propertyCategoryDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return propertyCategoryDict

    def updatePropertyCategory(self,propertyCategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(" UPDATE propertycategorymaster SET propertyCategoryName='{}', propertyCategoryDescription='{}' WHERE propertyCategoryId LIKE '{}' ".format(propertyCategoryVO.propertyCategoryName, propertyCategoryVO.propertyCategoryDescription,propertyCategoryVO.propertyCategoryId))

        connection.commit()
        cursor1.close()
        connection.close()

    def deletePropertyCategory(self,propertyCategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(" UPDATE propertycategorymaster SET propertyCategoryActiveStatus='{}' WHERE propertyCategoryId = '{}' ".format( propertyCategoryVO.propertyCategoryActiveStatus,propertyCategoryVO.propertyCategoryId))

        connection.commit()
        cursor1.close()
        connection.close()

    def editPropertyCategory(self,propertyCategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT  * FROM propertycategorymaster WHERE propertyCategoryId = '{}' ".format(propertyCategoryVO.propertyCategoryId))
        propertyCategoryDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return propertyCategoryDict




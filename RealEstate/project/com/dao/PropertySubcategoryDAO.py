from project.com.dao import *


class PropertySubcategoryDAO:

    def insertPropertySubcategory(self,propertySubcategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO propertysubcategorymaster (propertySubcategoryName,propertySubcategoryDescription,propertySubcategory_PropertyCategoryId,propertySubcategoryActiveStatus) VALUES ( '{}','{}','{}','{}')".format(propertySubcategoryVO.propertySubcategoryName,propertySubcategoryVO.propertySubcategoryDescription,propertySubcategoryVO.propertySubcategory_PropertyCategoryId,propertySubcategoryVO.propertySubcategoryActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchPropertySubcategory(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from propertysubcategorymaster inner join propertycategorymaster on propertySubcategory_PropertyCategoryId=propertyCategoryId WHERE  propertyCategoryActiveStatus='active' AND propertySubcategoryActiveStatus='active' ")
        propertySubcategoryDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return propertySubcategoryDict

    def deletePropertySubcategory(self,propertySubcategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE propertysubcategorymaster SET propertySubcategoryActiveStatus='{}' WHERE propertySubcategoryId = '{}' ".format(propertySubcategoryVO.propertySubcategoryActiveStatus,propertySubcategoryVO.propertySubcategoryId))

        connection.commit()
        cursor1.close()
        connection.close()

    def updatePropertySubcategory(self,propertySubcategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE propertysubcategorymaster SET propertySubcategoryName='{}', propertySubcategoryDescription='{}',propertySubcategory_propertyCategoryId='{}' WHERE propertySubcategoryId = '{}' ".format( propertySubcategoryVO.propertySubcategoryName,propertySubcategoryVO.propertySubcategoryDescription,propertySubcategoryVO.propertySubcategory_PropertyCategoryId,propertySubcategoryVO.propertySubcategoryId))


        connection.commit()
        cursor1.close()
        connection.close()

    def editPropertySubcategory(self,propertySubcategoryVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from propertysubcategorymaster inner join propertycategorymaster on propertySubcategory_PropertyCategoryId = propertyCategoryId WHERE propertySubcategoryId = '{}' ".format(propertySubcategoryVO.propertySubcategoryId))

        propertySubcategoryDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return propertySubcategoryDict

    def searchPropertySubcategory(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from propertysubcategorymaster inner join propertycategorymaster on propertySubcategory_PropertyCategoryId=propertyCategoryId WHERE  propertyCategoryActiveStatus='active' AND propertySubcategoryActiveStatus='active' ")
        propertySubcategoryDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return propertySubcategoryDict
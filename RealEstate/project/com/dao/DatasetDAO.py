from project.com.dao import *

class DatasetDAO:

    def insertDataset(self,datasetVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO datasetmaster (datasetFilename,datasetFilepath,datasetDescription,datasetActiveStatus)VALUES ('{}','{}','{}','{}')".format(datasetVO.datasetFilename,datasetVO.datasetFilepath,datasetVO.datasetDescription,datasetVO.datasetActiveStatus))


        connection.commit()
        cursor1.close()
        connection.close()


    def searchDataset(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from datasetmaster WHERE datasetActiveStatus='active'")
        datasetDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return datasetDict

    def deleteDataset(self,datasetVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE datasetmaster SET datasetActiveStatus='{}' WHERE datasetId = '{}' ".format(datasetVO.datasetActiveStatus,datasetVO.datasetId))
        connection.commit()
        cursor1.close()
        connection.close()
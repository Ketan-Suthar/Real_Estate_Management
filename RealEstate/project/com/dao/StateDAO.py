from project.com.dao import con_db


class StateDAO:

    def insertState(self, stateVO):

        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO statemaster (stateName,stateDescription,stateActiveStatus) VALUES ('{}','{}','{}')".format(stateVO.stateName, stateVO.stateDescription, stateVO.stateActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchState(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from statemaster WHERE stateActiveStatus='active' ")
        stateDict = cursor1.fetchall()

        cursor1.close()
        connection.close()

        return stateDict

    def deleteState(self, stateVO):

        connection = con_db()

        cursor1 = connection.cursor()
        cursor1.execute("UPDATE statemaster SET stateActiveStatus='{}' WHERE stateId = '{}' ".format(stateVO.stateActiveStatus, stateVO.stateId))

        connection.commit()
        cursor1.close()
        connection.close()

    def editState(self, stateVO):

        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute(" SELECT * FROM statemaster WHERE stateId = '{}' ".format(stateVO.stateId))
        stateDict = cursor1.fetchall()

        cursor1.close()
        connection.close()
        return stateDict

    def updateState(self, stateVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE statemaster SET stateName='{}', stateDescription='{}' WHERE stateId = '{}' ".format(
            stateVO.stateName, stateVO.stateDescription, stateVO.stateId))

        connection.commit()
        cursor1.close()
        connection.close()

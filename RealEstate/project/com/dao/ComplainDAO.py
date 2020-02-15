from project.com.dao import *

class ComplainDAO:

    def insertComplain(self,complainVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO complainmaster (complainSubject,complainDescription,complainFrom_LoginId,complainDate,complainTime,complainStatus,complainActiveStatus) VALUES('{}','{}','{}','{}','{}','{}','{}')".format(complainVO.complainSubject,complainVO.complainDescription,complainVO.complainFrom_LoginId,complainVO.complainDate,complainVO.complainTime,complainVO.complainStatus,complainVO.complainActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchComplain(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("select * from complainmaster inner join loginmaster on complainFrom_LoginId = loginId where complainActiveStatus = 'active' and loginActiveStatus = 'active' ")

        complainDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return complainDict

    def editComplain(self,complainVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("select * from complainmaster inner join loginmaster on complainFrom_LoginId = loginId where  complainId = '{}' ".format(complainVO.complainId))

        complainDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return complainDict

    def updateComplain(self,complainVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("update complainmaster set complainReply='{}', complainTo_LoginId='{}', complainStatus='{}' where complainId = '{}' ".format(complainVO.complainReply,complainVO.complainTo_LoginId,complainVO.complainStatus,complainVO.complainId))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchComplainById(self,complainVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("select * from complainmaster inner join loginmaster on complainFrom_LoginId = loginId where complainActiveStatus = 'active' and complainFrom_LoginId = '{}' ".format(complainVO.complainFrom_LoginId))

        complainDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return complainDict
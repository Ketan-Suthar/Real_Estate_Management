from project.com.dao import con_db
#from flask_login import UserMixin

class LoginDAO():
    def insertLogin(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO loginmaster (loginRole,loginEmailId,loginPassword,\
        loginActiveStatus) VALUES('{}','{}','{}','{}')".format\
        (loginVO.loginRole,loginVO.loginEmailId,loginVO.loginPassword,loginVO.loginActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchLogin(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM loginmaster WHERE loginEmailId ='{}'".format(loginVO.loginEmailId))

        loginDict = cursor1.fetchall()

        connection.commit()
        cursor1.close()
        connection.close()

        return loginDict

    def searchLoginById(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM loginmaster WHERE loginId ='{}'".format(loginVO.loginId))

        loginDict = cursor1.fetchall()

        connection.commit()
        cursor1.close()
        connection.close()
        return loginDict

    def searchLoginDetailsById(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM loginmaster AS lm INNER JOIN registermaster AS rm ON lm.loginId = rm.register_LoginId WHERE loginId ='{}'".format(loginVO.loginId))

        loginDict = cursor1.fetchall()

        connection.commit()
        cursor1.close()
        connection.close()
        return loginDict

    def updateLogin(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("UPDATE loginmaster SET loginEmailId = '{}',loginActiveStatus='{}' WHERE loginId = '{}'".format(loginVO.loginEmailId,loginVO.loginActiveStatus,loginVO.loginId))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchLoginByEmailId(self,loginVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM loginmaster WHERE loginEmailId ='{}'".format(loginVO.loginEmailId))

        loginDict = cursor1.fetchall()

        connection.commit()
        cursor1.close()
        connection.close()
        return loginDict

    def getMaxId(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT MAX(loginId) from loginmaster")
        loginDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return loginDict

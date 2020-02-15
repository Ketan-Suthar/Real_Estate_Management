from project.com.dao import *
#from flask_login import UserMixin

class RegisterDAO():

    def insertRegister(self,registerVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO registermaster \
        (register_LoginId,registerFirstName,registerLastName,\
        registerContact,registerDate,registerTime,registerActiveStatus)\
            VALUES ('{}','{}','{}','{}','{}','{}','{}')".format\
        (registerVO.register_LoginId,registerVO.registerFirstName, \
         registerVO.registerLastName,registerVO.registerContact,\
        registerVO.registerDate,registerVO.registerTime, \
         registerVO.registerActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def updateRegister(self,registerVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(" UPDATE registermaster SET registerFirstName= '{}', registerLastName='{}',registerContact='{}',registerActiveStatus='{}' WHERE register_LoginId='{}' ".format(registerVO.registerFirstName,registerVO.registerLastName,registerVO.registerContact,registerVO.registerActiveStatus,registerVO.register_LoginId))
        connection.commit()
        cursor1.close()
        connection.close()
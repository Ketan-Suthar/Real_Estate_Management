import pymysql

def con_db():

    return pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            db='realestate',
                            cursorclass=pymysql.cursors.DictCursor
                            )
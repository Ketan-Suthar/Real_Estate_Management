from project.com.dao import *

class PropertyReviewDAO:

    def insertPropertyReview(self,propertyReviewVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO propertyreviewmaster \
      (propertyReview_PropertyId,propertyReview_LoginId,\
      propertyReviewDescription,propertyReviewRating,propertyReviewDate,\
      propertyReviewTime,propertyReviewActiveStatus)\
      VALUE ('{}','{}','{}','{}','{}','{}','{}')".format\
       (propertyReviewVO.propertyReview_PropertyId,propertyReviewVO.propertyReview_LoginId, \
        propertyReviewVO.propertyReviewDescription,propertyReviewVO.propertyReviewRating, \
        propertyReviewVO.propertyReviewDate,propertyReviewVO.propertyReviewTime, \
        propertyReviewVO.propertyReviewActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchPropertyReviewByPropertyId(self,propertyReviewVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM propertyreviewmaster AS prm \
        INNER JOIN loginmaster AS lm ON lm.loginId = prm.propertyReview_LoginId \
        INNER JOIN registermaster AS rm ON rm.register_LoginId = lm.loginId \
         WHERE propertyReview_PropertyId = '{}' ".format(propertyReviewVO.propertyReview_PropertyId))
        propertyReviewDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return propertyReviewDict
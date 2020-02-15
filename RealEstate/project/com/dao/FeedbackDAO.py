from project.com.dao import *

class FeedbackDAO:

    def insertFeedback(self,feedbackVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO feedbackmaster  (feedbackRating,feedbackMessage,feedbackFrom_LoginId,feedbackDate,feedbackTime,feedbackActiveStatus) VALUES ('{}','{}','{}','{}','{}','{}' )".format(feedbackVO.feedbackRating,feedbackVO.feedbackMessage, feedbackVO.feedbackFrom_LoginId,feedbackVO.feedbackDate, feedbackVO.feedbackTime,feedbackVO.feedbackActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchFeedback(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from feedbackmaster inner join loginmaster on feedbackFrom_LoginId = loginId WHERE feedbackActiveStatus='active' AND loginActiveStatus='active' ")
        feebackDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return feebackDict

    def updateFeedback(self,feedbackVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE feedbackmaster SET feedbackTo_LoginId='{}' WHERE feedbackId = '{}'".format(feedbackVO.feedbackTo_LoginId,feedbackVO.feedbackId))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchFeedbackById(self, feedbackVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute(
            "select * from feedbackmaster inner join loginmaster on feedbackFrom_LoginId = loginId WHERE feedbackActiveStatus='active' AND feedbackFrom_LoginId = '{}' ".format(
                feedbackVO.feedbackFrom_LoginId))
        feebackDict = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return feebackDict


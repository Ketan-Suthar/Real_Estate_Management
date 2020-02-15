from project.com.dao import *

class ForumAnswerDAO:

    def insertForumAnswer(self,forumAnswerVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("INSERT INTO forumanswermaster (forumAnswer_LoginId,forumAnswer_ForumQuestionId,forumAnswer,forumAnswerDate,forumAnswerTime,forumAnswerActiveStatus) VALUES('{}','{}','{}','{}','{}','{}')".format(forumAnswerVO.forumAnswer_LoginId,forumAnswerVO.forumAnswer_ForumQuestionId,forumAnswerVO.forumAnswer,forumAnswerVO.forumAnswerDate,forumAnswerVO.forumAnswerTime,forumAnswerVO.forumAnswerActiveStatus))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchForumAnswer(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM forumanswermaster WHERE forumAnswerActiveStatus = 'active'")

        forumAnswerDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return forumAnswerDict
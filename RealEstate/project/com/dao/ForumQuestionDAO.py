from project.com.dao import *

class ForumQuestionDAO:

    def insertForumQuestion(self,forumQuestionVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("INSERT INTO forumquestionmaster \
        (forumQuestion_LoginId,forumQuestion,forumQuestionDiscussion,\
        forumQuestionDate,forumQuestionTime,forumQuestionActiveStatus) \
        VALUES ('{}','{}','{}','{}','{}','{}')".format\
        (forumQuestionVO.forumQuestion_LoginId,forumQuestionVO.forumQuestion, \
         forumQuestionVO.forumQuestionDiscussion,forumQuestionVO.forumQuestionDate, \
         forumQuestionVO.forumQuestionTime,forumQuestionVO.forumQuestionActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

    def searchForumQuestion(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM forumquestionmaster WHERE forumQuestionActiveStatus = 'active' AND forumQuestionDiscussion = TRUE")

        forumQuestionDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return forumQuestionDict

    def searchForumQuestionById(self,forumQuestionVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "SELECT * FROM forumquestionmaster WHERE forumQuestionId = '{}' ANd forumQuestionActiveStatus = 'active' AND forumQuestionDiscussion = TRUE".format(forumQuestionVO.forumQuestionId))

        forumQuestionDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return forumQuestionDict

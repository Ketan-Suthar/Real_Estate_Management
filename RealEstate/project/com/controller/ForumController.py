from flask import render_template, request, redirect, url_for, session
from project import app
from datetime import date, datetime
#from flask_login import login_required
from datetime import datetime

from project.com.dao.ForumAnswerDAO import ForumAnswerDAO
from project.com.dao.ForumQuestionDAO import ForumQuestionDAO

from project.com.vo.ForumAnswerVO import ForumAnswerVO
from project.com.vo.ForumQuestionVO import ForumQuestionVO

@app.route('/forum')
# @login_required
def forum():
    if session['loginRole'] != 'user':
        return render_template('admin/login.html')

    forumAnswerDAO = ForumAnswerDAO()
    forumQuestionDAO = ForumQuestionDAO()

    forumAnswerVO = ForumAnswerVO()
    forumQuestionVO = ForumQuestionVO()

    forumQuestionDict = forumQuestionDAO.searchForumQuestion()
    forumAnswerDict = forumAnswerDAO.searchForumAnswer()

    return render_template('user/forum.html',session=session,forumQuestionDict=forumQuestionDict,forumAnswerDict=forumAnswerDict)


@app.route('/insertQuestion',methods=['POST'])
def insertQuestion():

    if session['loginRole'] != 'user':
        return render_template('admin/login.html')

    forumQuestionDAO = ForumQuestionDAO()
    forumQuestionVO = ForumQuestionVO()

    forumQuestionVO.forumQuestion_LoginId = session['loginId']
    forumQuestionVO.forumQuestion = request.form['forumQuestion']
    forumQuestionVO.forumQuestionDate,forumQuestionVO.forumQuestionTime =  str(datetime.now()).split(' ')
    forumQuestionVO.forumQuestionDiscussion = 1
    forumQuestionVO.forumQuestionActiveStatus = 'active'

    forumQuestionDAO.insertForumQuestion(forumQuestionVO)

    return redirect(url_for('forum'))


@app.route('/loadForumAnswer')
# @login_required
def loadForumAnswer():
    if session['loginRole'] != 'user':
        return render_template('admin/login.html')

    forumQuestionDAO = ForumQuestionDAO()
    forumQuestionVO = ForumQuestionVO()

    forumQuestionVO.forumQuestionId = request.args.get('forumQuestionId')

    forumQuestionDict = forumQuestionDAO.searchForumQuestionById(forumQuestionVO)

    return render_template('user/forumAnswer.html',forumQuestionDict=forumQuestionDict)


@app.route('/insertAnswer',methods=['POST'])
def insertAnswer():

    if session['loginRole'] != 'user':
        return render_template('admin/login.html')

    forumAnswerDAO = ForumAnswerDAO()
    forumAnswerVO = ForumAnswerVO()

    forumAnswerVO.forumAnswer_LoginId = session['loginId']
    forumAnswerVO.forumAnswer_ForumQuestionId = request.form['forumQuestionId']
    forumAnswerVO.forumAnswer = request.form['forumAnswer']
    forumAnswerVO.forumAnswerDate,forumAnswerVO.forumAnswerTime =  str(datetime.now()).split(' ')
    forumAnswerVO.forumAnswerActiveStatus = 'active'

    forumAnswerDAO.insertForumAnswer(forumAnswerVO)

    return redirect(url_for('forum'))

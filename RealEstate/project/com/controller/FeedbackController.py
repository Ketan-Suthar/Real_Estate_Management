from flask import render_template, request, redirect, url_for, session
from project import app
from datetime import date, datetime


from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO


@app.route('/feedback')
def feedback():
    return render_template('user/feedback.html')


@app.route('/insertFeedback', methods=['POST'])
def insertFeedback():
    # try:

    if session['loginRole'] == 'user':
        feedbackDAO = FeedbackDAO()
        feedbackVO = FeedbackVO()

        feedbackVO.feedbackRating = request.form['feedbackRating']
        feedbackVO.feedbackMessage = request.form['feedbackMessage']
        #feedbackVO.feedbackDate = str(date.today())
        feedbackVO.feedbackDate,feedbackVO.feedbackTime =str(datetime.now()).split(' ')
        feedbackVO.feedbackActiveStatus = 'active'


        feedbackVO.feedbackFrom_LoginId = session['loginId']

        feedbackDAO.insertFeedback(feedbackVO)

        return redirect(url_for('feedback'))
    else:
        #print "in else"
        return redirect(url_for('login'))

        # except:
        #     print "in exception"
        #     return redirect(url_for('login'))


@app.route('/viewUserFeedback')
def viewUserFeedback():

    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    feedbackDAO = FeedbackDAO()
    feedbackVO = FeedbackVO()

    feedbackVO.feedbackFrom_LoginId = session['loginId']
    feedbackDict = feedbackDAO.searchFeedbackById(feedbackVO)

    return render_template('user/viewFeedback.html',feedbackDict=feedbackDict)



@app.route('/loadManageFeedback')
def loadManageFeedback():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    feedbackDAO = FeedbackDAO()

    feedbackDict = feedbackDAO.searchFeedback()

    return render_template('admin/manageFeedback.html',feedbackDict=feedbackDict)


@app.route('/viewFeedback')
def viewFeedback():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    feedbackDAO = FeedbackDAO()
    feedbackVO = FeedbackVO()


    feedbackVO.feedbackId = request.args.get('feedbackId')

    feedbackVO.feedbackTo_LoginId = session['loginId']
    feedbackDAO.updateFeedback(feedbackVO)

    return redirect(url_for('loadManageFeedback'))


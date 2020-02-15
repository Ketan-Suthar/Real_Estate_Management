from flask import render_template,request,url_for,redirect,session
from project import app

from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO


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


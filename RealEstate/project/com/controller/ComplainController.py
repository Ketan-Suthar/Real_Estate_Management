from flask import render_template, request, redirect, url_for, session
from project import app
from datetime import date, datetime


from project.com.dao.ComplainDAO import ComplainDAO
from project.com.vo.ComplainVO import ComplainVO


@app.route('/complain')
def complain():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    return render_template('user/complain.html')

@app.route('/insertComplain',methods=['POST'])
def insertComplain():
    if session['loginRole'] != 'user':
        return redirect(url_for('login'))

    complainDAO = ComplainDAO()
    complainVO = ComplainVO()

    complainVO.complainSubject = request.form['complainSubject']
    complainVO.complainDescription = request.form['complainDescription']
    complainVO.complainDate, complainVO.complainTime = str(datetime.now()).split(' ')
    complainVO.complainStatus = 'pending'
    complainVO.complainActiveStatus = 'active'
    complainVO.complainFrom_LoginId = session['loginId']

    complainDAO.insertComplain(complainVO)

    return redirect(url_for('complain'))

@app.route('/viewUserComplain')
def viewUserComplain():

    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    complainDAO = ComplainDAO()
    complainVO = ComplainVO()

    complainVO.complainFrom_LoginId = session['loginId']
    complainDict = complainDAO.searchComplainById(complainVO)

    return render_template('user/viewComplain.html',complainDict=complainDict)




@app.route('/loadManageComplain')
def loadManageComplain():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    complainDAO = ComplainDAO()

    complainDict = complainDAO.searchComplain()

    return render_template('admin/manageComplain.html',complainDict=complainDict)

@app.route('/loadComplainReply')
def loadComplainReply():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    complainDAO = ComplainDAO()
    complainVO = ComplainVO()

    complainVO.complainId = request.args.get('complainId')

    complainDict = complainDAO.editComplain(complainVO)

    return render_template('admin/complainReply.html',complainDict=complainDict)


@app.route('/complainReply',methods=['POST'])
def complainReply():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    complainDAO = ComplainDAO()
    complainVO = ComplainVO()

    complainVO.complainStatus = 'replied'
    complainVO.complainReply = request.form['complainReply']
    complainVO.complainTo_LoginId = session['loginId']
    complainVO.complainId = request.form['complainId']

    complainDAO.updateComplain(complainVO)

    return redirect(url_for('loadManageComplain'))
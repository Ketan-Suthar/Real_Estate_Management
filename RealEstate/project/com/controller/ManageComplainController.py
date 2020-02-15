from flask import render_template, request, redirect, url_for, session
from project import app

from project.com.dao.ComplainDAO import ComplainDAO
from project.com.vo.ComplainVO import ComplainVO

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
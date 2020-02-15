from flask import render_template,request,url_for,redirect, session, flash
from project import app
from datetime import  datetime

import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart

from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO

from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO

@app.route('/loadRegister')
def loadRegister():
    registerVO = RegisterVO()

    return render_template('admin/register.html',registerVO=registerVO)


@app.route('/insertRegister',methods=['POST'])
def insertRegister():
    registerDAO = RegisterDAO()
    registerVO = RegisterVO()

    loginDAO = LoginDAO()
    loginVO = LoginVO()

    loginVO.loginEmailId = request.form['registerEmailId']

    loginDict = loginDAO.searchLoginByEmailId(loginVO)

    if loginDict:
        flash('EmailAddress Is Already Taken', 'success')
        return render_template('admin/register.html')

    registerVO.registerFirstName = request.form['registerFirstName']
    registerVO.registerLastName = request.form['registerLastName']
    registerVO.registerContact = request.form['registerContact']
    registerVO.registerDate,registerVO.registerTime = str(datetime.now()).split(' ')
    registerVO.registerActiveStatus = 'active'


    loginVO.loginRole = 'user'
    loginVO.loginActiveStatus = 'active'
    loginVO.loginPassword = 'abc@123'

    loginDAO.insertLogin(loginVO)
    loginDict = loginDAO.getMaxId()

    registerVO.register_LoginId = loginDict[0]['MAX(loginId)']
    registerDAO.insertRegister(registerVO)

    loginDict = loginDAO.searchLoginByEmailId(loginVO)
    session['loginRole'] = loginDict[0]['loginRole']
    session['loginId'] = loginDict[0]['loginId']

    fromaddr = "noreply@gmail.com"
    toaddr = loginVO.loginEmailId
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "welcome to lemanhouse"
    msg.attach(MIMEText(loginVO.loginPassword, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("heisenberg1102008@gmail.com", "HeisenBerg_1102008")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

    return redirect(url_for('home'))
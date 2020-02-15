from flask import render_template,request,url_for,redirect,session
from project import app

from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO

from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.RegisterVO import RegisterVO

from project.com.dao.PropertyBasicDetailsDAO import PropertyBasicDetailsDAO
from project.com.vo.PropertyBasicDetailsVO import PropertyBasicDetailsVO

@app.route('/userProfile')
def userProfile():

    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    loginDAO = LoginDAO()
    loginVO = LoginVO()

    loginVO.loginId = session['loginId']
    loginDict = loginDAO.searchLoginDetailsById(loginVO)
    print "loginDict : ",loginDict
    return render_template('user/user-profile.html',loginDict=loginDict)


@app.route('/updateProfile',methods=['POST'])
def updateProfile():

    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    loginDAO = LoginDAO()
    loginVO = LoginVO()

    registerDAO = RegisterDAO()
    registerVO = RegisterVO()

    loginVO.loginId = session['loginId']
    loginVO.loginEmailId = request.form['registerEmailId']
    loginVO.loginActiveStatus = 'active'

    registerVO.register_LoginId = session['loginId']
    registerVO.registerFirstName = request.form['registerFirstName']
    registerVO.registerLastName = request.form['registerLastName']
    registerVO.registerContact = request.form['registerContact']
    registerVO.registerActiveStatus = 'active'

    registerDAO.updateRegister(registerVO)
    loginDAO.updateLogin(loginVO)

    return redirect(url_for('userProfile'))



@app.route('/userFavouriteProperties')
def userFavouriteProperties():

    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    loginDAO = LoginDAO()
    loginVO = LoginVO()

    loginVO.loginId = session['loginId']
    loginDict = loginDAO.searchLoginDetailsById(loginVO)

    return render_template('user/favourite-properties.html',loginDict=loginDict)


@app.route('/userProperties')
def userProperties():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    loginDAO = LoginDAO()
    loginVO = LoginVO()

    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    loginVO.loginId = propertyBasicDetailsVO.property_LoginId = session['loginId']
    loginDict = loginDAO.searchLoginDetailsById(loginVO)

    propertyDict = propertyBasicDetailsDAO.serachPropertyDetailsByLoginId(propertyBasicDetailsVO)

    return render_template('user/my-properties.html', loginDict=loginDict,propertyDict=propertyDict)





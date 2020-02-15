from flask import render_template,request,url_for,redirect,session
from project import app
from os import walk
#from flask_login import current_user, UserMixin, login_user, login_required

from project.com.dao.PropertyBasicDetailsDAO import PropertyBasicDetailsDAO

from project.com.dao.LoginDAO import LoginDAO
from project.com.vo.LoginVO import LoginVO


# @login_manager.user_loader
# def load_user(user_id):
#     loginDAO = LoginDAO()
#     loginVO = LoginVO()
#
#     loginVO.loginId = int(user_id)
#     loginDict = loginDAO.searchLoginById(loginVO)
#
#     return loginDict

@app.route('/')
def home():
    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    try:
        if session['loginRole']=='admin':
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else render_template('admin/index.html')
        else:
            propertyDict = propertyBasicDetailsDAO.serachProperty()
            return  render_template('user/index.html',propertyDict=propertyDict,walk=walk,session=session)
    except Exception(e):
        print (str(e))
        propertyDict = propertyBasicDetailsDAO.serachProperty()
        return render_template('user/index.html',propertyDict=propertyDict,walk=walk,session=session)

@app.route('/loadIndex')
def loadIndex():
    try:
        if session['loginRole']=='admin':
            return render_template('admin/index.html')
        else:
            return  render_template('user/index.html')
    except:
        return redirect(url_for('home'))


@app.route('/loadLogin')
def loadLogin():

    return render_template('admin/login.html')

@app.route('/checkLogin',methods=['POST'])
def checkLogin():

    logindao = LoginDAO()
    loginvo = LoginVO()

    loginvo.loginEmailId = request.form['loginEmailId']

    loginDict = logindao.searchLogin(loginvo)
    # print ("loginDict : ",loginDict)

    if (loginDict):
        password = request.form['loginPassword']
        # session['loginDict']=loginDict[0]

        session['loginRole']=loginDict[0]['loginRole']
        session['loginId']=loginDict[0]['loginId']

        if (password == loginDict[0]['loginPassword']):
            # if(loginDict[0]['loginRole']=='admin'):
            print ("login dict : ",loginDict)
            # login_user(loginDict)
            return redirect(url_for('home'))
            # else:
            #     return render_template('admin/login.html')
        else:
            return render_template('admin/login.html')
    else:
        return render_template('admin/register.html')


@app.route('/logout')
# @login_required
def logout():
    session.clear()

    print ("in logout")
    return redirect(url_for('home'))

@app.route('/about')
def about():
    return render_template('admin/about.html')
from flask import render_template,request,url_for,redirect,session
from project import app
from project.com.vo.StateVO import StateVO
from project.com.dao.StateDAO import StateDAO




@app.route('/loadState')
def loadState():

    return render_template('admin/addState.html')


@app.route('/insertState', methods=['POST'])
def insertState():

    stateVO = StateVO()
    stateDAO = StateDAO()

    stateVO.stateName= request.form['stateName']
    stateVO.stateDescription= request.form['stateDescription']
    stateVO.stateActiveStatus = "active"

    stateDAO.insertState(stateVO)

    return redirect(url_for('loadState'))


@app.route('/viewState')
def viewState():

    stateDAO = StateDAO()

    stateDict = stateDAO.searchState()

    return render_template('admin/viewState.html',stateDict=stateDict)


@app.route('/deleteState', methods=['POST','GET'])
def deleteState():

    stateDAO = StateDAO()
    stateVO  = StateVO()
    stateVO.stateId = request.args.get('stateId')
    stateVO.stateActiveStatus = 'deactive'

    stateDAO.deleteState(stateVO)

    return redirect(url_for('viewState'))


@app.route('/editState', methods=['GET'])
def editState():

    stateDAO = StateDAO()
    stateVO = StateVO()

    stateVO.stateId = request.args.get('stateId')

    stateDict = stateDAO.editState(stateVO)

    return render_template('admin/editState.html', stateDict=stateDict)


@app.route('/updateState', methods=['POST'])
def updateState():

    stateVO = StateVO()
    stateDAO = StateDAO()

    stateVO.stateName = request.form['stateName']
    stateVO.stateDescription=request.form['stateDescription']
    stateVO.stateId= request.form['stateId']

    stateDAO.updateState(stateVO)

    return redirect(url_for('viewState'))



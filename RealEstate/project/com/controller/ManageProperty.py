from flask import render_template, request, redirect, url_for, session, send_from_directory
from project import app
from os import walk,path
from project.com.dao.PropertyBasicDetailsDAO import PropertyBasicDetailsDAO
from project.com.vo.PropertyBasicDetailsVO import PropertyBasicDetailsVO


@app.route('/loadManageProperty')
def loadManageProperty():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()

    propertyDict = propertyBasicDetailsDAO.serachPropertyAll()

    return render_template('admin/manageProperty.html',propertyDict=propertyDict)


@app.route('/viewManageProperty')
def viewManageProperty():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    propertyBasicDetailsVO = PropertyBasicDetailsVO()
    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()

    propertyBasicDetailsVO.propertyId = request.args.get('propertyId')

    propertyDict = propertyBasicDetailsDAO.serachPropertyDetailsById(propertyBasicDetailsVO)

    return render_template('admin/viewManageProperty.html',propertyDict=propertyDict,walk=walk,path=path)


@app.route('/propertyAdminReply',methods=['POST'])
def propertyAdminReply():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    if request.form['propertyStatus'] != 'cancel':
        propertyBasicDetailsVO = PropertyBasicDetailsVO()
        propertyBasicDetailsDAO = PropertyBasicDetailsDAO()

        propertyBasicDetailsVO.propertyStatus = request.form['propertyStatus']
        if request.form['propertyReply']:
            propertyBasicDetailsVO.propertyAdminReply = request.form['propertyReply']
        else:
            propertyBasicDetailsVO.propertyAdminReply = 'Thank You'
        propertyBasicDetailsVO.propertyId = request.form['propertyId']

        propertyBasicDetailsDAO.updatePropertyStatus(propertyBasicDetailsVO)

    return redirect(url_for('loadManageProperty'))
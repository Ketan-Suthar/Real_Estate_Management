from flask import render_template, request, redirect, url_for,session
from project import app
from project.com.dao.PropertyCategoryDAO import PropertyCategoryDAO
from project.com.vo.PropertyCategoryVO import PropertyCategoryVO


@app.route('/loadPropertyCategory')
def loadPropertyCategory():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    return render_template('admin/addPropertyCategory.html')


@app.route('/insertPropertyCategory', methods=['POST'])
def insertPropertyCategory():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    propertyCategoryVO = PropertyCategoryVO()
    propertyCategoryDAO = PropertyCategoryDAO()

    propertyCategoryVO.propertyCategoryName = request.form['propertyCategoryName']
    propertyCategoryVO.propertyCategoryDescription = request.form['propertyCategoryDescription']
    propertyCategoryVO.propertyCategoryActiveStatus = 'active'

    propertyCategoryDAO.insertPropertyCategory(propertyCategoryVO)

    return redirect(url_for('loadPropertyCategory'))


@app.route('/viewPropertyCategory')
def viewPropertyCategory():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    propertyCategoryDAO = PropertyCategoryDAO()

    propertyCategoryDict=propertyCategoryDAO.searchPropertyCategory()

    return render_template('admin/viewPropertyCategory.html',propertyCategoryDict=propertyCategoryDict)


@app.route('/editPropertyCategory', methods=['GET'])
def editPropertyCategory():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    propertyCategoryDAO = PropertyCategoryDAO()
    propertyCategoryVO = PropertyCategoryVO()
    propertyCategoryVO.propertyCategoryId = request.args.get('propertyCategoryId')
    propertyCategoryDict=propertyCategoryDAO.editPropertyCategory(propertyCategoryVO)

    return render_template('admin/editPropertyCategory.html', propertyCategoryDict=propertyCategoryDict)


@app.route('/updatePropertyCategory', methods=['POST'])
def updatePropertyCategory():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    propertyCategoryVO = PropertyCategoryVO()
    propertyCategoryDAO = PropertyCategoryDAO()

    propertyCategoryVO.propertyCategoryName = request.form['propertyCategoryName']
    propertyCategoryVO.propertyCategoryDescription = request.form['propertyCategoryDescription']
    propertyCategoryVO.propertyCategoryId = request.form['propertyCategoryId']

    propertyCategoryDAO.updatePropertyCategory(propertyCategoryVO)

    return redirect(url_for('viewPropertyCategory'))


@app.route('/deletePropertyCategory', methods=['GET'])
def deletePropertyCategory():
    propertyCategoryDAO = PropertyCategoryDAO()
    propertyCategoryVO = PropertyCategoryVO()
    propertyCategoryVO.propertyCategoryId = request.args.get('propertyCategoryId')
    propertyCategoryVO.propertyCategoryActiveStatus = 'deactive'

    propertyCategoryDAO.deletePropertyCategory(propertyCategoryVO)

    return redirect(url_for('viewPropertyCategory'))
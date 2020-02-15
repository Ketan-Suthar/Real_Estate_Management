from flask import render_template, request, redirect, url_for
from project import app

from project.com.dao.PropertySubcategoryDAO import PropertySubcategoryDAO
from project.com.vo.PropertySubcategoryVO import PropertySubcategoryVO

from project.com.dao.PropertyCategoryDAO import PropertyCategoryDAO


@app.route('/loadPropertySubcategory')
def loadPropertySubcategory():
    propertyCategoryDAO = PropertyCategoryDAO()
    propertyCategoryDict = propertyCategoryDAO.searchPropertyCategory()

    return render_template('admin/addPropertySubcategory.html',propertyCategoryDict=propertyCategoryDict)


@app.route('/insertPropertySubcategory', methods=['POST'])
def insertPropertySubcategory():

    propertySubcategoryDAO= PropertySubcategoryDAO()
    propertySubcategoryVO= PropertySubcategoryVO()

    propertySubcategoryVO.propertySubcategoryName= request.form['propertySubcategoryName']
    propertySubcategoryVO.propertySubcategoryDescription= request.form['propertySubcategoryDescription']
    propertySubcategoryVO.propertySubcategory_PropertyCategoryId= request.form['propertyCategoryId']
    propertySubcategoryVO.propertySubcategoryActiveStatus = 'active'

    propertySubcategoryDAO.insertPropertySubcategory(propertySubcategoryVO)

    return redirect(url_for('loadPropertySubcategory'))


@app.route('/viewPropertySubcategory')
def viewPropertySubcategory():

    propertySubcategoryDAO = PropertySubcategoryDAO()
    propertySubcategoryDict = propertySubcategoryDAO.searchPropertySubcategory()

    return render_template('admin/viewPropertySubcategory.html',propertySubcategoryDict=propertySubcategoryDict)


@app.route('/editPropertySubcategory', methods=['GET'])
def editPropertySubcategory():

    propertyCategoryDAO = PropertyCategoryDAO()
    propertySubcategoryDAO = PropertySubcategoryDAO()
    propertySubcategoryVO = PropertySubcategoryVO()
    propertySubcategoryVO.propertySubcategoryId= request.args.get('propertySubcategoryId')
    propertySubcategoryDict = propertySubcategoryDAO.editPropertySubcategory(propertySubcategoryVO)
    propertyCategoryDict = propertyCategoryDAO.searchPropertyCategory()

    return render_template('admin/editPropertySubcategory.html', propertySubcategoryDict=propertySubcategoryDict,propertyCategoryDict=propertyCategoryDict,propertySubcategoryId=propertySubcategoryVO.propertySubcategoryId)


@app.route('/updatePropertySubcategory', methods=['POST'])
def updatePropertySubcategory():

    propertySubcategoryDAO= PropertySubcategoryDAO()
    propertySubcategoryVO= PropertySubcategoryVO()

    propertySubcategoryVO.propertySubcategoryName= request.form['propertySubcategoryName']
    propertySubcategoryVO.propertySubcategoryDescription= request.form['propertySubcategoryDescription']
    propertySubcategoryVO.propertySubcategory_PropertyCategoryId= request.form['propertyCategoryId']
    propertySubcategoryVO.propertySubcategoryId = request.form['propertySubcategoryId']

    propertySubcategoryDAO.updatePropertySubcategory(propertySubcategoryVO)

    return redirect(url_for('viewPropertySubcategory'))



@app.route('/deletePropertySubcategory')
def deletePropertySubcategory():
    propertySubcategoryDAO = PropertySubcategoryDAO()
    propertySubcategoryVO = PropertySubcategoryVO()
    propertySubcategoryVO.propertySubcategoryId = request.args.get('propertySubcategoryId')
    propertySubcategoryVO.propertySubcategoryActiveStatus = 'deactive'
    propertySubcategoryDAO.deletePropertySubcategory(propertySubcategoryVO)

    return redirect(url_for('viewPropertySubcategory'))
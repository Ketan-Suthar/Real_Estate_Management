from flask import render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from project import app
import os
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO


@app.route('/loadDataset')
def loadDataset():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    return render_template('admin/addDataset.html')


@app.route('/insertDataset',methods=['POST'])
def insertDataset():

    try:
        if session['loginRole']=='admin':

            datasetVO = DatasetDAO()
            datasetDAO = DatasetDAO()
            UPLOAD_FOLDER = 'C:/Users/Admin/Desktop/admin/project/static/adminResources/dataset'

            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            file = request.files['file']
            print(file)

            filename = secure_filename(file.filename)
            # print(filename)

            filepath = os.path.join(app.config['UPLOAD_FOLDER'])
            # print(filepath)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            datasetVO.datasetFilename = filename
            datasetVO.datasetFilepath = filepath
            datasetVO.datasetDescription = request.form['datasetDescription']
            datasetVO.datasetActiveStatus = 'active'

            datasetDAO.insertDataset(datasetVO)

        return redirect(url_for('loadDataset'))
    except:
        return redirect(url_for('login'))

@app.route('/viewDataset')
def viewDataset():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    datasetDAO = DatasetDAO()
    datasetDict=datasetDAO.searchDataset()
    return render_template('admin/viewDataset.html',datasetDict=datasetDict)

@app.route('/deleteDataset',methods=['GET'])
def deleteDataset():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    datasetVO = DatasetVO()
    datasetDAO = DatasetDAO()
    datasetVO.datasetId=request.args.get('datasetId')
    datasetVO.datasetActiveStatus ='deactive'
    datasetDAO.deleteDataset(datasetVO)

    return redirect(url_for('viewDataset'))


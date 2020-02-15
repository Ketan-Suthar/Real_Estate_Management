from flask import render_template, request, redirect, url_for, session
from project import app

from project.com.dao.CityDAO import CityDAO
from project.com.vo.CityVO import CityVO

from project.com.dao.StateDAO import StateDAO


@app.route('/loadCity')
def loadCity():
    try:
        if session['loginRole']!= 'admin':
            return redirect(url_for('loadLogin'))
    except:
        return redirect(url_for('loadLogin'))

    stateDAO = StateDAO()
    stateDict = stateDAO.searchState()

    return render_template('admin/addCity.html',stateDict=stateDict)


@app.route('/insertCity', methods=['POST'])
def insertCity():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    cityDAO= CityDAO()
    cityVO= CityVO()

    cityVO.cityName= request.form['cityName']
    cityVO.cityDescription= request.form['cityDescription']
    cityVO.city_StateId=request.form['stateId']
    cityVO.cityActiveStatus='active'

    cityDAO.insertCity(cityVO)

    return redirect(url_for('loadCity'))


@app.route('/viewCity')
def viewCity():

    if session['loginRole']!='admin':
        return render_template('admin/login.html')

    cityDAO = CityDAO()
    cityDict=cityDAO.searchCity()
    
    return render_template('admin/viewCity.html',cityDict=cityDict)



@app.route('/editCity', methods=['GET'])
def editCity():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    cityDAO = CityDAO()
    stateDAO = StateDAO()

    cityVO = CityVO()
    cityVO.cityId = request.args.get('cityId')
    cityDict = cityDAO.editCity(cityVO)
    stateDict = stateDAO.searchState()

    print (cityDict)

    return render_template('admin/editCity.html', cityDict=cityDict, stateDict=stateDict)


@app.route('/updateCity', methods=['POST'])
def updateCity():

    if session['loginRole']!= 'admin':
        return redirect(url_for('login'))

    cityDAO= CityDAO()
    cityVO= CityVO()

    cityVO.cityName= request.form['cityName']
    cityVO.cityDescription= request.form['cityDescription']
    cityVO.city_StateId= request.form['stateId']
    cityVO.cityId= request.form['cityId']

    cityDAO.updateCity(cityVO)

    return redirect(url_for('viewCity'))

from flask import render_template, request, redirect, url_for, session, send_from_directory
from project import app
from datetime import date, datetime
from os import walk
from os import path
import os

from werkzeug.utils import secure_filename

from project.com.dao.PropertyCategoryDAO import PropertyCategoryDAO
from project.com.dao.PropertySubcategoryDAO import PropertySubcategoryDAO
from project.com.vo.PropertySubcategoryVO import PropertySubcategoryVO
from project.com.vo.PropertyCategoryVO import PropertyCategoryVO

from project.com.dao.StateDAO import StateDAO
from project.com.dao.CityDAO import CityDAO
from project.com.vo.CityVO import CityVO

from project.com.dao.PropertyBasicDetailsDAO import PropertyBasicDetailsDAO
from project.com.vo.PropertyBasicDetailsVO import PropertyBasicDetailsVO

from project.com.dao.PropertyAddressDAO import PropertyAddressDAO
from project.com.vo.PropertyAddressVO import PropertyAddressVO

from project.com.dao.PropertyDetailsDAO import PropertyDetailsDAO
from project.com.vo.propertyDetailsVO import PropertyDetailsVO

from project.com.dao.PropertyPricingDAO import PropertyPricingDAO
from project.com.vo.PropertyPricingVO import PropertyPricingVO

from project.com.dao.PropertyAmenitiesDAO import PropertyAmenitiesDAO
from project.com.vo.PropertyAmenitiesVO import PropertyAmenitiesVO

from project.com.dao.PropertyGalleryDAO import PropertyGalleryDAO
from project.com.vo.PropertyGalleryVO import PropertyGalleryVO

from project.com.dao.PropertyReviewDAO import PropertyReviewDAO
from project.com.vo.PropertyReviewVO import PropertyReviewVO



# This is the path to the upload directory

# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

# For a given file, return whether it's an allowed type or not
def allowed_images(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/loadPostProperty')
def loadPostProperty():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    propertyCategoryDAO = PropertyCategoryDAO()
    propertySubcategoryDAO = PropertySubcategoryDAO()

    propertyCategoryDict = propertyCategoryDAO.searchPropertyCategory()
    propertySubcategoryDict = propertySubcategoryDAO.searchPropertySubcategory()

    return render_template('user/propertyBasicDetails.html',propertyCategoryDict=propertyCategoryDict,propertySubcategoryDict=propertySubcategoryDict)


@app.route('/insertPropertyBasicDetails',methods=['POST'])
def insertPropertyBasicDetails():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()
    propertySubcategoryDAO = PropertySubcategoryDAO()
    propertySubcategoryVO = PropertySubcategoryVO()

    propertyBasicDetailsVO.property_LoginId = session['loginId']
    propertyBasicDetailsVO.propertyOwnerType = request.form['propertyOwnerType']
    propertyBasicDetailsVO.propertyListFor = request.form['propertyListFor']

    propertyBasicDetailsVO.property_PropertySubcategoryId = request.form['property_PropertySubcategoryId']
    propertyBasicDetailsVO.propertyAtStep = '2'
    propertyBasicDetailsVO.propertyStatus = 'pending'
    propertyBasicDetailsVO.propertyActiveStatus = 'active'

    propertySubcategoryVO.propertySubcategoryId = propertyBasicDetailsVO.property_PropertySubcategoryId
    propertySubcategoryDict = propertySubcategoryDAO.editPropertySubcategory(propertySubcategoryVO)
    propertyBasicDetailsVO.propertyDate,propertyBasicDetailsVO.propertyTime = str(datetime.now()).split(' ')
    propertyBasicDetailsVO.property_PropertyCategoryId = propertySubcategoryDict[0]['propertySubcategory_PropertyCategoryId']


    propertyBasicDetailsDAO.insertPropertyBasicDetails(propertyBasicDetailsVO)

    return redirect(url_for('loadPropertyAddress'))


@app.route('/loadPropertyAddress')
def loadPropertyAddress():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    stateDAO = StateDAO()
    cityDAO = CityDAO()
    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()

    stateDict = stateDAO.searchState()
    cityDict = cityDAO.searchCity()
    propertyDict = propertyBasicDetailsDAO.getMaxId()

    return render_template('user/propertyAddress.html',cityDict=cityDict,stateDict=stateDict,propertyDict=propertyDict)

def setStep(atStep,propertyId):

    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyBasicDetailsVO.propertyAtStep = atStep
    propertyBasicDetailsVO.propertyId = propertyId

    propertyBasicDetailsDAO.updateAtStep(propertyBasicDetailsVO)

@app.route('/insertPropertyAddress',methods=['POST'])
def insertPropertyAddress():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    propertyAddressDAO = PropertyAddressDAO()
    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertySubcategoryDAO = PropertySubcategoryDAO()

    propertySubcategoryVO = PropertySubcategoryVO()

    propertyAddressVO = PropertyAddressVO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyDict = {}

    propertyAddressVO.propertyAddress_PropertyId = request.form['propertyId']
    propertyAddressVO.propertyStreet = request.form['propertyStreet']
    propertyAddressVO.propertyLocality = request.form['propertyLocality']
    propertyAddressVO.propertyCityId = request.form['propertyCityId']
    propertyAddressVO.propertyStateId = request.form['propertyStateId']
    propertyAddressVO.propertyPincode = request.form['propertyPincode']

    propertyAddressVO.propertyAddressDate, propertyAddressVO.propertyAddressTime = str(datetime.now()).split(' ')
    propertyAddressVO.propertyAddressActiveStatus = 'active'

    propertyDict['propertyId'] = request.form['propertyId']
    propertyBasicDetailsVO.propertyId = propertyDict['propertyId']
    propertyDict = propertyBasicDetailsDAO.searchPropertyById(propertyBasicDetailsVO)

    propertyAddressDAO.insertPropertyAddress(propertyAddressVO)
    # print "pDict",propertyDict

    propertySubcategoryVO.propertySubcategoryId = propertyDict[0]['property_PropertySubcategoryId']

    propertySubcategoryDict = propertySubcategoryDAO.editPropertySubcategory(propertySubcategoryVO)
    # print "propertySubcategoryDict", propertySubcategoryDict

    setStep('3',request.form['propertyId'])

    if(propertySubcategoryDict[0]['propertyCategoryName']=='land'):
        return render_template('user/propertyDetailsLand.html', propertyDict=propertyDict)
    elif (propertySubcategoryDict[0]['propertyCategoryName'] == 'commercial'):
        if (propertySubcategoryDict[0]['propertySubcategoryName']=='hotel' or propertySubcategoryDict[0]['propertySubcategoryName']=='resort'):
            return render_template('user/propertyDetailsHotel.html', propertyDict=propertyDict)
        else:
            return render_template('user/propertyDetailsCommercial.html', propertyDict=propertyDict)
    else:
        return render_template('user/propertyDetailsResidential.html', propertyDict=propertyDict)



@app.route('/insertPropertyDetailsLand',methods=['POST'])
def insertPropertyDetailsLand():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    propertyDetailsDAO = PropertyDetailsDAO()
    propertyDetailsVO = PropertyDetailsVO()
    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyDetailsVO.propertyDetails_PropertyId = request.form['propertyId']
    propertyDetailsVO.propertyBuildUpArea = request.form['propertyBuildUpArea']
    propertyDetailsVO.propertyBuildUpAreaUnit = request.form['propertyBuildUpAreaUnit']
    propertyDetailsVO.propertyDescription = request.form['propertyDescription']
    propertyDetailsVO.propertyDetailsDate, propertyDetailsVO.propertyDetailsTime = str(datetime.now()).split(' ')
    propertyDetailsVO.propertyDetailsActiveStatus = 'active'
    propertyBasicDetailsVO.propertyId = request.form['propertyId']

    propertyDetailsDAO.insertPropertyDetailsLand(propertyDetailsVO)

    setStep('4', request.form['propertyId'])

    propertyDict = propertyBasicDetailsDAO.searchPropertyById(propertyBasicDetailsVO)

    return render_template('user/propertyPricing.html',propertyDict=propertyDict)


@app.route('/insertPropertyDetailsHotel',methods=['POST'])
def insertPropertyDetailsHotel():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    otherRooms = ''
    propertyDetailsDAO = PropertyDetailsDAO()
    propertyDetailsVO = PropertyDetailsVO()
    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyDetailsVO.propertyDetails_PropertyId = request.form['propertyId']
    propertyDetailsVO.propertyName = request.form['propertyName']
    propertyDetailsVO.propertyRERANo = request.form['propertyRERANo']
    propertyDetailsVO.propertyBuildUpArea = request.form['propertyBuildUpArea']
    propertyDetailsVO.propertyBuildUpAreaUnit = request.form['propertyBuildUpAreaUnit']
    propertyDetailsVO.propertyQualityRating = request.form['propertyQualityRating']
    propertyDetailsVO.propertyWashrooms = request.form['propertyWashrooms']
    propertyDetailsVO.propertyTotalRooms = request.form['propertyTotalRooms']

    temp = request.form.getlist('propertyOtherRooms')

    for i in temp:
        otherRooms = otherRooms + ' ' + i

    propertyDetailsVO.propertyOtherRooms = otherRooms
    propertyDetailsVO.propertyParking = request.form['propertyParking']
    propertyDetailsVO.propertyDescription = request.form['propertyDescription']
    propertyDetailsVO.propertyDetailsDate, propertyDetailsVO.propertyDetailsTime = str(datetime.now()).split(' ')
    propertyDetailsVO.propertyDetailsActiveStatus = 'active'

    propertyDetailsDAO.insertPropertyDetailsHotel(propertyDetailsVO)

    setStep('4', request.form['propertyId'])

    propertyBasicDetailsVO.propertyId = request.form['propertyId']
    propertyDict = propertyBasicDetailsDAO.searchPropertyById(propertyBasicDetailsVO)

    return render_template('user/propertyPricing.html',propertyDict=propertyDict)



@app.route('/insertPropertyDetailsCommercial',methods=['POST'])
def insertPropertyDetailsCommercial():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))


    propertyDetailsDAO = PropertyDetailsDAO()
    propertyDetailsVO = PropertyDetailsVO()
    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyDetailsVO.propertyDetails_PropertyId = request.form['propertyId']
    propertyDetailsVO.propertyName = request.form['propertyName']
    propertyDetailsVO.propertyRERANo = request.form['propertyRERANo']
    propertyDetailsVO.propertyBuildUpArea = request.form['propertyBuildUpArea']
    propertyDetailsVO.propertyBuildUpAreaUnit = request.form['propertyBuildUpAreaUnit']

    propertyDetailsVO.propertyWashrooms = request.form['propertyWashrooms']

    propertyDetailsVO.propertyParking = request.form['propertyParking']
    propertyDetailsVO.propertyDescription = request.form['propertyDescription']
    propertyDetailsVO.propertyDetailsDate, propertyDetailsVO.propertyDetailsTime = str(datetime.now()).split(' ')
    propertyDetailsVO.propertyDetailsActiveStatus = 'active'

    propertyDetailsDAO.insertPropertyDetailsCommercial(propertyDetailsVO)

    setStep('4', request.form['propertyId'])

    propertyBasicDetailsVO.propertyId = request.form['propertyId']
    propertyDict = propertyBasicDetailsDAO.searchPropertyById(propertyBasicDetailsVO)

    return render_template('user/propertyPricing.html',propertyDict=propertyDict)



@app.route('/insertPropertyDetailsResidential',methods=['POST'])
def insertPropertyDetailsResidential():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    otherRooms = ''
    propertyDetailsDAO = PropertyDetailsDAO()
    propertyDetailsVO = PropertyDetailsVO()
    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyDetailsVO.propertyDetails_PropertyId = request.form['propertyId']
    propertyDetailsVO.propertyName = request.form['propertyName']
    propertyDetailsVO.propertyRERANo = request.form['propertyRERANo']
    propertyDetailsVO.propertyBuildUpArea = request.form['propertyBuildUpArea']
    propertyDetailsVO.propertyBuildUpAreaUnit = request.form['propertyBuildUpAreaUnit']
    propertyDetailsVO.propertyBedrooms = request.form['propertyBedrooms']
    propertyDetailsVO.propertyBathrooms = request.form['propertyBathrooms']
    propertyDetailsVO.propertyBalconies = request.form['propertyBalconies']
    propertyDetailsVO.propertyFurnishing = request.form['propertyFurnishing']
    propertyDetailsVO.propertyOnFloor = request.form['propertyOnFloor']
    propertyDetailsVO.propertyTotalFloors = request.form['propertyTotalFloors']

    temp = request.form.getlist('propertyOtherRooms')

    for i in temp:
        otherRooms = otherRooms + ' ' + i

    propertyDetailsVO.propertyOtherRooms = otherRooms
    propertyDetailsVO.propertyParking = request.form['propertyParking']
    propertyDetailsVO.propertyDescription = request.form['propertyDescription']
    propertyDetailsVO.propertyDetailsDate, propertyDetailsVO.propertyDetailsTime = str(datetime.now()).split(' ')
    propertyDetailsVO.propertyDetailsActiveStatus = 'active'

    propertyDetailsDAO.insertPropertyDetailsResidential(propertyDetailsVO)

    setStep('4', request.form['propertyId'])

    propertyBasicDetailsVO.propertyId = request.form['propertyId']
    propertyDict = propertyBasicDetailsDAO.searchPropertyById(propertyBasicDetailsVO)

    return render_template('user/propertyPricing.html',propertyDict=propertyDict)





@app.route('/insertPropertyPricing',methods=['POST'])
def insertPropertyPricing():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    propertyPricingVO = PropertyPricingVO()
    propertyPricingDAO = PropertyPricingDAO()

    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyPricingVO.propertyPricing_PropertyId = request.form['propertyId']
    propertyPricingVO.propertyPricingDate,propertyPricingVO.propertyPricingTime = str(datetime.now()).split(' ')

    propertyPricingVO.propertyPricingActiveStatus = 'active'

    propertyBasicDetailsVO.propertyId = request.form['propertyId']
    propertyDict = propertyBasicDetailsDAO.searchPropertyById(propertyBasicDetailsVO)
    if(propertyDict[0]['propertyListFor']=='sell'):
        propertyPricingVO.propertyPrice = request.form['propertyPrice']
        propertyPricingVO.propertyMonthlyRent = -1
    else:
        propertyPricingVO.propertyMonthlyRent = request.form['propertyMonthlyRent']
        propertyPricingVO.propertyPrice = -1

    propertyPricingDAO.insertPropertyPricing(propertyPricingVO)

    setStep('5', request.form['propertyId'])

    propertyDict = propertyBasicDetailsDAO.searchPropertyById(propertyBasicDetailsVO)

    return render_template('user/propertyGallery.html',propertyDict=propertyDict)


@app.route('/insertPropertyGallery',methods=['GET','POST'])
def insertPropertyGallery():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    propertyGalleryVO = PropertyGalleryVO()
    propertyGalleryDAO = PropertyGalleryDAO()
    propertyDict = {}
    uploaded_files = request.files.getlist("propertyCoverImages")
    if uploaded_files:
        coverImages = []
        propertyId = request.form['propertyId']
        pathToImages = 'C:/Users/Admin/Desktop/admin/project/static/userResources/propertyGallery'
        os.chdir(pathToImages)
        os.makedirs(propertyId + '/coverImages')
        filePath = pathToImages + '/' + propertyId + '/coverImages'
        app.config['UPLOAD_FOLDER'] = filePath
        for file in uploaded_files:
            if file and allowed_images(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                coverImages.append(filename)
        # print coverImages

    uploaded_files = request.files.getlist("propertyInsideImages")
    if uploaded_files:
        insideImages = []
        os.chdir(pathToImages)
        os.makedirs(propertyId + '/insideImages')
        filePath = pathToImages + '/' + propertyId + '/insideImages'
        app.config['UPLOAD_FOLDER'] = filePath
        for file in uploaded_files:
            if file and allowed_images(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                insideImages.append(filename)
        # print insideImages

    uploaded_files = request.files.getlist("propertyOutsideImages")
    if uploaded_files:
        outsideImages = []
        os.chdir(pathToImages)
        os.makedirs(propertyId + '/outsideImages')
        filePath = pathToImages + '/' + propertyId + '/outsideImages'
        app.config['UPLOAD_FOLDER'] = filePath
        for file in uploaded_files:
            if file and allowed_images(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                outsideImages.append(filename)
        # print outsideImages

    uploaded_files = request.files.getlist("propertyFloorPlanImages")
    if uploaded_files:
        propertyFloorPlanImages = []
        os.chdir(pathToImages)
        os.makedirs(propertyId + '/floorPlanImages')
        filePath = pathToImages + '/' + propertyId + '/floorPlanImages'
        app.config['UPLOAD_FOLDER'] = filePath
        for file in uploaded_files:
            if file and allowed_images(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                propertyFloorPlanImages.append(filename)
        # print propertyFloorPlanImages

    file = request.files['propertyBroucher']
    if file:

        os.chdir(pathToImages)
        os.makedirs(propertyId + '/broucher')
        filePath = pathToImages + '/' + propertyId + '/broucher'
        app.config['UPLOAD_FOLDER'] = filePath

        filename = secure_filename(file.filename)

        filepath = os.path.join(app.config['UPLOAD_FOLDER'])
        # print(filepath)

        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # rename =  propertyId + '-' + 'broucher-1.pdf'
        # os.rename(file.filename,rename)

    propertyGalleryVO.propertyGallery_PropertyId = propertyId
    propertyGalleryVO.propertyGalleryPath = pathToImages + '/' + propertyId
    propertyGalleryVO.property360Image = request.form['property360Image']
    propertyGalleryVO.propertyVideo = request.form['propertyVideo']
    propertyGalleryVO.propertyGalleryDate, propertyGalleryVO.propertyGalleryTime = str(datetime.now()).split(' ')
    propertyGalleryVO.propertyGalleryActiveStatus = 'active'

    propertyGalleryDAO.insertPropertyGallery(propertyGalleryVO)

    setStep('6', request.form['propertyId'])

    propertyDict['propertyId'] = propertyId
    return render_template('user/propertyAmenities.html',propertyDict=propertyDict)


@app.route('/insertPropertyAmenities',methods=['POST'])
def insertPropertyAmenities():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    aminities = ''

    propertyAmenitiesDAO = PropertyAmenitiesDAO()
    propertyAmenitiesVO = PropertyAmenitiesVO()

    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyAmenitiesVO.propertyAmenities_PropertyId =  request.form['propertyId']
    propertyAmenitiesVO.propertyAmenitiesActiveStatus = 'active'
    propertyAmenitiesVO.propertyAmenitiesDate,propertyAmenitiesVO.propertyAmenitiesTime = str(datetime.now()).split(' ')

    temp = request.form.getlist('propertyAmenityName')

    for i in temp:
        aminities = aminities +' '+i
    propertyAmenitiesVO.propertyAmenities = aminities
    #print "amenities",aminities
    #print "PId",request.form['propertyId']

    propertyAmenitiesDAO.insertPropertyAmenities(propertyAmenitiesVO)

    setStep('complete', request.form['propertyId'])

    propertyBasicDetailsVO.propertyId = request.form['propertyId']
    propertyDict = propertyBasicDetailsDAO.searchPropertyById(propertyBasicDetailsVO)

    return render_template('user/propertySubmited.html',propertyDict=propertyDict)

@app.route('/loadPropertyDetails')
def loadPropertyDetails():

    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()
    propertyBasicDetailsVO = PropertyBasicDetailsVO()

    propertyReviewVO = PropertyReviewVO()
    propertyReviewDAO = PropertyReviewDAO()

    propertyBasicDetailsVO.propertyId = propertyReviewVO.propertyReview_PropertyId = request.args.get('propertyId')

    propertyDict = propertyBasicDetailsDAO.serachPropertyDetailsById(propertyBasicDetailsVO)
    propertyReviewDict = propertyReviewDAO.searchPropertyReviewByPropertyId(propertyReviewVO)
    # print propertyDict[0]['propertyCategoryName']
    if propertyDict[0]['propertyCategoryName'] == 'residential':
        return render_template('user/viewPropertyDetailsResidential.html',propertyDict=propertyDict,propertyReviewDict=propertyReviewDict,walk=walk,path=path)
    elif propertyDict[0]['propertyCategoryName'] == 'land':
        return render_template('user/viewPropertyDetailsLand.html', propertyDict=propertyDict,propertyReviewDict=propertyReviewDict,walk=walk,path=path)
    elif propertyDict[0]['propertyCategoryName'] == 'commercial':
        if propertyDict[0]['propertySubcategoryName'] == 'hotel' or propertyDict[0]['propertySubcategoryName'] == 'resort':
            return render_template('user/viewPropertyDetailsHotel.html', propertyDict=propertyDict,propertyReviewDict=propertyReviewDict,walk=walk,path=path)
        else:
            return render_template('user/viewPropertyDetailsCommercial.html', propertyDict=propertyDict,propertyReviewDict=propertyReviewDict,walk=walk,path=path)
    else:
        return redirect(url_for('home'))


@app.route('/insertPropertyReview',methods=['POST'])
def insertPropertyReview():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    propertyReviewVO =PropertyReviewVO()
    propertyReviewDAO = PropertyReviewDAO()

    propertyReviewVO.propertyReview_LoginId = session['loginId']
    propertyReviewVO.propertyReview_PropertyId = request.form['propertyId']
    propertyReviewVO.propertyReviewDescription = request.form['propertyReviewDescription']
    propertyReviewVO.propertyReviewRating = request.form['propertyReviewRating']
    propertyReviewVO.propertyReviewDate,propertyReviewVO.propertyReviewTime = str(datetime.now()).split(' ')
    propertyReviewVO.propertyReviewActiveStatus = 'active'

    propertyReviewDAO.insertPropertyReview(propertyReviewVO)

    return redirect(url_for('home'))


@app.route('/viewProperies')
def viewProperies():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    propertyBasicDetailsDAO = PropertyBasicDetailsDAO()

    propertyDict = propertyBasicDetailsDAO.serachProperty()

    return render_template('user/properties-grid.html',propertyDict=propertyDict,walk=walk)


@app.route('/contactUs')
def contactUs():
    if session['loginRole']!= 'user':
        return redirect(url_for('login'))

    return render_template('user/contact.html')


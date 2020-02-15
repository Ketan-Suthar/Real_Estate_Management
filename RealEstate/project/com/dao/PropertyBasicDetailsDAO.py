from project.com.dao import *

class PropertyBasicDetailsDAO:

    def insertPropertyBasicDetails(self,propertyBasicDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO propertybasicdetailsmaster (property_LoginId,\
        propertyOwnerType,\
        propertyListFor,property_PropertyCategoryId,\
        property_PropertySubcategoryId,propertyDate,propertyTime,\
        propertyAtStep,propertyStatus,\
        propertyActiveStatus) VALUES \
        ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".\
        format(propertyBasicDetailsVO.property_LoginId,\
               propertyBasicDetailsVO.propertyOwnerType,\
               propertyBasicDetailsVO.propertyListFor, \
               propertyBasicDetailsVO.property_PropertyCategoryId,\
               propertyBasicDetailsVO.property_PropertySubcategoryId, \
               propertyBasicDetailsVO.propertyDate,propertyBasicDetailsVO.propertyTime, \
               propertyBasicDetailsVO.propertyAtStep,\
               propertyBasicDetailsVO.propertyStatus,\
               propertyBasicDetailsVO.propertyActiveStatus))
        connection.commit()
        cursor1.close()
        connection.close()

    def getMaxId(self):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT max(propertyId) FROM propertybasicdetailsmaster")
        propertyDict = cursor1.fetchall()
        cursor1.close()
        connection.close()

        return propertyDict

    def updateAtStep(self,propertyBasicDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE propertybasicdetailsmaster SET propertyAtStep = '{}' WHERE propertyId = '{}'".format(propertyBasicDetailsVO.propertyAtStep,propertyBasicDetailsVO.propertyId))
        connection.commit()
        cursor1.close()
        connection.close()

    def searchPropertyById(self,propertyBasicDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("SELECT * FROM propertybasicdetailsmaster WHERE propertyId = '{}' AND propertyActiveStatus='active'".format(propertyBasicDetailsVO.propertyId))
        propertyDict = cursor1.fetchall()
        cursor1.close()
        connection.close()

        return propertyDict

    def serachProperty(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM propertybasicdetailsmaster AS pbdm INNER JOIN propertycategorymaster AS pcm \
            ON pbdm.`property_PropertyCategoryId` = pcm.`propertyCategoryId` INNER JOIN propertysubcategorymaster AS pscm \
             ON pbdm.`property_PropertySubcategoryId` = pscm.`propertySubcategoryId`\
             INNER JOIN propertyaddressmaster AS pam ON pbdm.`propertyId` = pam.`propertyAddress_PropertyId`\
             INNER JOIN statemaster AS sm ON pam.`propertyStateId` = sm.`stateId`\
             INNER JOIN citymaster AS cm ON pam.`propertyCityId` = cm.`cityId`\
             INNER JOIN propertydetailsmaster AS pdm ON pbdm.`propertyId` = pdm.`propertyDetails_PropertyId`\
             INNER JOIN propertypricingmaster AS ppm ON pbdm.`propertyId` = ppm.`propertyPricing_PropertyId`\
             INNER JOIN propertygallerymaster AS pgm ON pbdm.`propertyId` = pgm.`propertyGallery_PropertyId`\
             INNER JOIN propertyamenitiesmaster AS pamm ON pbdm.`propertyId` = pamm.`propertyAmenities_PropertyId`\
             INNER JOIN loginmaster AS lm ON pbdm.`property_LoginId` = lm.`loginId` WHERE propertyAtStep='complete' AND propertyActiveStatus = 'active' AND propertyStatus = 'accepted' ")

        propertyDict = cursor1.fetchall()
        cursor1.close()
        connection.close()

        return propertyDict

    def serachPropertyDetailsById(self,propertyBasicDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM propertybasicdetailsmaster AS pbdm INNER JOIN propertycategorymaster AS pcm \
                    ON pbdm.`property_PropertyCategoryId` = pcm.`propertyCategoryId` INNER JOIN propertysubcategorymaster AS pscm \
                     ON pbdm.`property_PropertySubcategoryId` = pscm.`propertySubcategoryId`\
                     INNER JOIN propertyaddressmaster AS pam ON pbdm.`propertyId` = pam.`propertyAddress_PropertyId`\
                     INNER JOIN statemaster AS sm ON pam.`propertyStateId` = sm.`stateId`\
                     INNER JOIN citymaster AS cm ON pam.`propertyCityId` = cm.`cityId`\
                     INNER JOIN propertydetailsmaster AS pdm ON pbdm.`propertyId` = pdm.`propertyDetails_PropertyId`\
                     INNER JOIN propertypricingmaster AS ppm ON pbdm.`propertyId` = ppm.`propertyPricing_PropertyId`\
                     INNER JOIN propertygallerymaster AS pgm ON pbdm.`propertyId` = pgm.`propertyGallery_PropertyId`\
                     INNER JOIN propertyamenitiesmaster AS pamm ON pbdm.`propertyId` = pamm.`propertyAmenities_PropertyId`\
                     INNER JOIN loginmaster AS lm ON pbdm.`property_LoginId` = lm.`loginId` WHERE pbdm.propertyId={} AND propertyAtStep = 'complete'".format(propertyBasicDetailsVO.propertyId))

        propertyDict = cursor1.fetchall()
        cursor1.close()
        connection.close()

        return propertyDict

    def serachPropertyDetailsByLoginId(self,propertyBasicDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM propertybasicdetailsmaster AS pbdm INNER JOIN propertycategorymaster AS pcm \
                    ON pbdm.`property_PropertyCategoryId` = pcm.`propertyCategoryId` INNER JOIN propertysubcategorymaster AS pscm \
                     ON pbdm.`property_PropertySubcategoryId` = pscm.`propertySubcategoryId`\
                     INNER JOIN propertyaddressmaster AS pam ON pbdm.`propertyId` = pam.`propertyAddress_PropertyId`\
                     INNER JOIN statemaster AS sm ON pam.`propertyStateId` = sm.`stateId`\
                     INNER JOIN citymaster AS cm ON pam.`propertyCityId` = cm.`cityId`\
                     INNER JOIN propertydetailsmaster AS pdm ON pbdm.`propertyId` = pdm.`propertyDetails_PropertyId`\
                     INNER JOIN propertypricingmaster AS ppm ON pbdm.`propertyId` = ppm.`propertyPricing_PropertyId`\
                     INNER JOIN propertygallerymaster AS pgm ON pbdm.`propertyId` = pgm.`propertyGallery_PropertyId`\
                     INNER JOIN propertyamenitiesmaster AS pamm ON pbdm.`propertyId` = pamm.`propertyAmenities_PropertyId`\
                     INNER JOIN loginmaster AS lm ON pbdm.`property_LoginId` = lm.`loginId` WHERE pbdm.property_LoginId={} AND propertyAtStep = 'complete'".format(propertyBasicDetailsVO.property_LoginId))

        propertyDict = cursor1.fetchall()
        cursor1.close()
        connection.close()

        return propertyDict

    def serachPropertyAll(self):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute("SELECT * FROM propertybasicdetailsmaster AS pbdm INNER JOIN propertycategorymaster AS pcm \
            ON pbdm.`property_PropertyCategoryId` = pcm.`propertyCategoryId` INNER JOIN propertysubcategorymaster AS pscm \
             ON pbdm.`property_PropertySubcategoryId` = pscm.`propertySubcategoryId`\
             INNER JOIN propertyaddressmaster AS pam ON pbdm.`propertyId` = pam.`propertyAddress_PropertyId`\
             INNER JOIN statemaster AS sm ON pam.`propertyStateId` = sm.`stateId`\
             INNER JOIN citymaster AS cm ON pam.`propertyCityId` = cm.`cityId`\
             INNER JOIN propertydetailsmaster AS pdm ON pbdm.`propertyId` = pdm.`propertyDetails_PropertyId`\
             INNER JOIN propertypricingmaster AS ppm ON pbdm.`propertyId` = ppm.`propertyPricing_PropertyId`\
             INNER JOIN propertygallerymaster AS pgm ON pbdm.`propertyId` = pgm.`propertyGallery_PropertyId`\
             INNER JOIN propertyamenitiesmaster AS pamm ON pbdm.`propertyId` = pamm.`propertyAmenities_PropertyId`\
             INNER JOIN loginmaster AS lm ON pbdm.`property_LoginId` = lm.`loginId` WHERE propertyAtStep='complete' AND propertyActiveStatus = 'active' ")

        propertyDict = cursor1.fetchall()
        cursor1.close()
        connection.close()
        return propertyDict


    def updatePropertyStatus(self,propertyBasicDetailsVO):
        connection = con_db()
        cursor1 = connection.cursor()
        cursor1.execute("UPDATE propertybasicdetailsmaster SET propertyStatus = '{}',propertyAdminReply='{}'  WHERE propertyId = '{}'".format(propertyBasicDetailsVO.propertyStatus,propertyBasicDetailsVO.propertyAdminReply,propertyBasicDetailsVO.propertyId))
        connection.commit()
        cursor1.close()
        connection.close()

from project.com.dao import *

class PropertyGalleryDAO:

    def insertPropertyGallery(self,propertyGalleryVO):
        connection = con_db()
        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO propertygallerymaster (propertyGallery_PropertyId,propertyGalleryPath,\
            propertyVideo,property360Image,propertyGalleryDate,propertyGalleryTime,\
            propertyGalleryActiveStatus)\
             VALUE ('{}','{}','{}','{}','{}','{}','{}')".format\
                (propertyGalleryVO.propertyGallery_PropertyId,propertyGalleryVO.propertyGalleryPath, \
                 propertyGalleryVO.propertyVideo,propertyGalleryVO.property360Image, \
                 propertyGalleryVO.propertyGalleryDate,propertyGalleryVO.propertyGalleryTime, \
                propertyGalleryVO.propertyGalleryActiveStatus))

        connection.commit()
        cursor1.close()
        connection.close()

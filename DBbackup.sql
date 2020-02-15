/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.0.27-community-nt : Database - realestate
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`realestate` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `realestate`;

/*Table structure for table `citymaster` */

DROP TABLE IF EXISTS `citymaster`;

CREATE TABLE `citymaster` (
  `city_StateId` int(8) NOT NULL,
  `cityId` int(8) NOT NULL auto_increment,
  `cityName` varchar(20) NOT NULL,
  `cityDescription` varchar(255) default NULL,
  `cityActiveStatus` varchar(10) default NULL,
  PRIMARY KEY  (`cityId`),
  KEY `city_StateId` (`city_StateId`),
  CONSTRAINT `citymaster_ibfk_1` FOREIGN KEY (`city_StateId`) REFERENCES `statemaster` (`stateId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `citymaster` */

insert  into `citymaster`(`city_StateId`,`cityId`,`cityName`,`cityDescription`,`cityActiveStatus`) values (2,1,'Ahmedabad','bxcgng','active'),(1,2,'chennai','fbdgbn','active'),(3,3,'kolkatta','kkr','active'),(4,4,'shrinagar','cold','active');

/*Table structure for table `complainmaster` */

DROP TABLE IF EXISTS `complainmaster`;

CREATE TABLE `complainmaster` (
  `complainId` int(8) NOT NULL auto_increment,
  `complainSubject` varchar(50) default NULL,
  `complainDescription` text,
  `complainTo_LoginId` int(8) default NULL,
  `complainFrom_LoginId` int(8) default NULL,
  `complainDate` varchar(20) default NULL,
  `complainTime` varchar(20) default NULL,
  `complainReply` text,
  `complainStatus` varchar(10) default NULL,
  `complainActiveStatus` varchar(10) default NULL,
  PRIMARY KEY  (`complainId`),
  KEY `complainTo_LoginId` (`complainTo_LoginId`),
  KEY `complainFrom_LoginId` (`complainFrom_LoginId`),
  CONSTRAINT `complainmaster_ibfk_1` FOREIGN KEY (`complainTo_LoginId`) REFERENCES `loginmaster` (`loginId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `complainmaster_ibfk_2` FOREIGN KEY (`complainFrom_LoginId`) REFERENCES `loginmaster` (`loginId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `complainmaster` */

insert  into `complainmaster`(`complainId`,`complainSubject`,`complainDescription`,`complainTo_LoginId`,`complainFrom_LoginId`,`complainDate`,`complainTime`,`complainReply`,`complainStatus`,`complainActiveStatus`) values (1,'first complain','verry goood sit',1,3,'2019-02-24','00:24:32.125000','very nice','replied','active'),(2,'about sit','no complain',2,2,'2019-02-24','21:46:45.933000','thanks','replied','active');

/*Table structure for table `datasetmaster` */

DROP TABLE IF EXISTS `datasetmaster`;

CREATE TABLE `datasetmaster` (
  `datasetId` int(8) NOT NULL auto_increment,
  `datasetFilename` varchar(255) NOT NULL,
  `datasetFilepath` varchar(255) NOT NULL,
  `datasetDescription` varchar(255) default NULL,
  `datasetActiveStatus` varchar(10) NOT NULL,
  PRIMARY KEY  (`datasetId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `datasetmaster` */

insert  into `datasetmaster`(`datasetId`,`datasetFilename`,`datasetFilepath`,`datasetDescription`,`datasetActiveStatus`) values (1,'resume_jay.docx','C:/Users/Kishan/Desktop/RealEstate/project/static/adminResources/dataset','oko','active');

/*Table structure for table `feedbackmaster` */

DROP TABLE IF EXISTS `feedbackmaster`;

CREATE TABLE `feedbackmaster` (
  `feedbackId` int(8) NOT NULL auto_increment,
  `feedbackMessage` varchar(255) default NULL,
  `feedbackTo_LoginId` int(8) default NULL,
  `feedbackFrom_LoginId` int(8) default NULL,
  `feedbackRating` varchar(5) default NULL,
  `feedbackDate` varchar(20) default NULL,
  `feedbackTime` varchar(20) default NULL,
  `feedbackActiveStatus` varchar(10) default NULL,
  PRIMARY KEY  (`feedbackId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedbackmaster` */

insert  into `feedbackmaster`(`feedbackId`,`feedbackMessage`,`feedbackTo_LoginId`,`feedbackFrom_LoginId`,`feedbackRating`,`feedbackDate`,`feedbackTime`,`feedbackActiveStatus`) values (1,'hiii',2,3,'1','2019-02-23','21:52:17.443000','active'),(2,'hiii',2,3,'1','2019-02-23','21:52:18.014000','active'),(3,'hiii',NULL,3,'1','2019-02-23','22:58:59.661000','active');

/*Table structure for table `loginmaster` */

DROP TABLE IF EXISTS `loginmaster`;

CREATE TABLE `loginmaster` (
  `loginId` int(8) NOT NULL auto_increment,
  `loginRole` varchar(10) NOT NULL,
  `loginEmailId` varchar(30) NOT NULL,
  `loginPassword` varchar(16) NOT NULL,
  `loginActiveStatus` varchar(10) NOT NULL,
  PRIMARY KEY  (`loginId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `loginmaster` */

insert  into `loginmaster`(`loginId`,`loginRole`,`loginEmailId`,`loginPassword`,`loginActiveStatus`) values (1,'admin','ks@gmail.com','123','active'),(2,'admin','rv@gmail.com','456','active'),(3,'user','dp@gmail.com','789','active'),(4,'user','jp@gmail.com','147','active');

/*Table structure for table `propertyaddressmaster` */

DROP TABLE IF EXISTS `propertyaddressmaster`;

CREATE TABLE `propertyaddressmaster` (
  `propertyAddressId` int(8) NOT NULL auto_increment,
  `propertyAddress_PropertyId` int(8) default NULL,
  `propertyStreet` varchar(255) default NULL,
  `propertyLocality` varchar(255) default NULL,
  `propertyStateId` int(8) default NULL,
  `propertyCityId` int(8) default NULL,
  `propertyPincode` int(6) default NULL,
  `propertyAddressActiveStatus` varchar(10) default NULL,
  PRIMARY KEY  (`propertyAddressId`),
  KEY `propertyAddress_PropertyId` (`propertyAddress_PropertyId`),
  KEY `propertyStateId` (`propertyStateId`),
  KEY `propertyCityId` (`propertyCityId`),
  CONSTRAINT `propertyaddressmaster_ibfk_1` FOREIGN KEY (`propertyAddress_PropertyId`) REFERENCES `propertybasicdetailsmaster` (`propertyId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `propertyaddressmaster_ibfk_2` FOREIGN KEY (`propertyStateId`) REFERENCES `statemaster` (`stateId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `propertyaddressmaster_ibfk_3` FOREIGN KEY (`propertyCityId`) REFERENCES `citymaster` (`cityId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `propertyaddressmaster` */

insert  into `propertyaddressmaster`(`propertyAddressId`,`propertyAddress_PropertyId`,`propertyStreet`,`propertyLocality`,`propertyStateId`,`propertyCityId`,`propertyPincode`,`propertyAddressActiveStatus`) values (1,1,'104 dhwani','nead GW',2,1,382443,'active'),(2,3,'104 dhwani','nead GW',2,1,382443,'active'),(3,3,'104 dhwani','nead GW',2,1,382443,'active'),(4,3,'104 dhwani','nead GW',2,1,382443,'active'),(5,4,'104 dhwani','near home',1,2,165151,'active'),(6,4,'104 dhwani','near home',1,2,165151,'active'),(7,4,'104 dhwani','near home',1,2,165151,'active'),(8,5,'104 dhwani','near office',3,3,382443,'active'),(9,6,'104 dhwani','nead GW',4,4,256314,'active'),(10,6,'104 dhwani','nead GW',4,4,256314,'active'),(11,6,'104 dhwani','nead GW',4,4,256314,'active'),(12,6,'104 dhwani','nead GW',4,4,256314,'active'),(13,6,'Ahmedabad, Gujarat, India','near office',2,3,382445,'active'),(14,6,'Ahmedabad, Gujarat, India','near office',2,3,382445,'active');

/*Table structure for table `propertyamenitiesmaster` */

DROP TABLE IF EXISTS `propertyamenitiesmaster`;

CREATE TABLE `propertyamenitiesmaster` (
  `propertyAmenitiesId` int(8) NOT NULL auto_increment,
  `propertyAmenities_PropertyId` int(8) default NULL,
  `propertyAmenityName` text,
  `propertyAmenitiesActiveStatus` varchar(10) default NULL,
  PRIMARY KEY  (`propertyAmenitiesId`),
  KEY `propertyAmenities_PropertyId` (`propertyAmenities_PropertyId`),
  CONSTRAINT `propertyamenitiesmaster_ibfk_2` FOREIGN KEY (`propertyAmenities_PropertyId`) REFERENCES `propertybasicdetailsmaster` (`propertyId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `propertyamenitiesmaster` */

insert  into `propertyamenitiesmaster`(`propertyAmenitiesId`,`propertyAmenities_PropertyId`,`propertyAmenityName`,`propertyAmenitiesActiveStatus`) values (1,4,' Oven Coffee Pot','active');

/*Table structure for table `propertybasicdetailsmaster` */

DROP TABLE IF EXISTS `propertybasicdetailsmaster`;

CREATE TABLE `propertybasicdetailsmaster` (
  `propertyId` int(8) NOT NULL auto_increment,
  `propertyOwnerType` varchar(20) default NULL,
  `propertyListFor` varchar(20) default NULL,
  `property_CategoryId` int(8) default NULL,
  `property_SubcategoryId` int(8) default NULL,
  `propertyDate` varchar(20) default NULL,
  `propertyTime` varchar(20) default NULL,
  `propertyActiveStatus` varchar(10) default NULL,
  PRIMARY KEY  (`propertyId`),
  KEY `property_CategoryId` (`property_CategoryId`),
  KEY `property_SubcategoryId` (`property_SubcategoryId`),
  CONSTRAINT `propertybasicdetailsmaster_ibfk_1` FOREIGN KEY (`property_CategoryId`) REFERENCES `propertycategorymaster` (`propertyCategoryId`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `propertybasicdetailsmaster_ibfk_2` FOREIGN KEY (`property_SubcategoryId`) REFERENCES `propertysubcategorymaster` (`propertySubcategoryId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `propertybasicdetailsmaster` */

insert  into `propertybasicdetailsmaster`(`propertyId`,`propertyOwnerType`,`propertyListFor`,`property_CategoryId`,`property_SubcategoryId`,`propertyDate`,`propertyTime`,`propertyActiveStatus`) values (1,'owner','sell',3,3,'2019-02-28','23:13:33.365000','active'),(2,'dealer','rent',1,10,'2019-02-28','23:15:16.649000','active'),(3,'dealer','sell',1,8,'2019-02-28','23:24:27.030000','active'),(4,'dealer','sell',1,9,'2019-02-28','23:31:32.328000','active'),(5,'owner','sell',2,1,'2019-02-28','23:48:17.738000','active'),(6,'builder','rent',3,4,'2019-03-01','00:03:32.482000','active');

/*Table structure for table `propertycategorymaster` */

DROP TABLE IF EXISTS `propertycategorymaster`;

CREATE TABLE `propertycategorymaster` (
  `propertyCategoryId` int(8) NOT NULL auto_increment,
  `propertyCategoryName` varchar(20) NOT NULL,
  `propertyCategoryDescription` varchar(255) default NULL,
  `propertyCategoryActiveStatus` varchar(10) NOT NULL,
  PRIMARY KEY  (`propertyCategoryId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `propertycategorymaster` */

insert  into `propertycategorymaster`(`propertyCategoryId`,`propertyCategoryName`,`propertyCategoryDescription`,`propertyCategoryActiveStatus`) values (1,'commercial','commercial','active'),(2,'land','this is land','active'),(3,'residential','vnch','active');

/*Table structure for table `propertysubcategorymaster` */

DROP TABLE IF EXISTS `propertysubcategorymaster`;

CREATE TABLE `propertysubcategorymaster` (
  `propertySubcategory_PropertyCategoryId` int(8) NOT NULL,
  `propertySubcategoryId` int(8) NOT NULL auto_increment,
  `propertySubcategoryName` varchar(20) NOT NULL,
  `propertySubcategoryDescription` varchar(255) default NULL,
  `propertySubcategoryActiveStatus` varchar(10) NOT NULL,
  PRIMARY KEY  (`propertySubcategoryId`),
  KEY `propertySubcategory_PropertyCategoryId` (`propertySubcategory_PropertyCategoryId`),
  CONSTRAINT `propertysubcategorymaster_ibfk_1` FOREIGN KEY (`propertySubcategory_PropertyCategoryId`) REFERENCES `propertycategorymaster` (`propertyCategoryId`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `propertysubcategorymaster` */

insert  into `propertysubcategorymaster`(`propertySubcategory_PropertyCategoryId`,`propertySubcategoryId`,`propertySubcategoryName`,`propertySubcategoryDescription`,`propertySubcategoryActiveStatus`) values (2,1,'farm','hmghm','active'),(3,3,'villa','gbxgfb','active'),(3,4,'apaerment','apartments only','active'),(3,5,'bunglow','very expensive','active'),(2,6,'party plot','plots','active'),(2,7,'golf club','only golf','active'),(1,8,'office','business','active'),(1,9,'studio','for filming','active'),(1,10,'shopping mall','not big mall','active');

/*Table structure for table `statemaster` */

DROP TABLE IF EXISTS `statemaster`;

CREATE TABLE `statemaster` (
  `stateId` int(8) NOT NULL auto_increment,
  `stateName` varchar(20) NOT NULL,
  `stateDescription` varchar(255) default NULL,
  `stateActiveStatus` varchar(10) NOT NULL,
  PRIMARY KEY  (`stateId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `statemaster` */

insert  into `statemaster`(`stateId`,`stateName`,`stateDescription`,`stateActiveStatus`) values (1,'tamilnadu','south india','active'),(2,'gujarat','hiiii','active'),(3,'west bangal','wi','active'),(4,'jammu',' j&k','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
--
-- Host: wedx.mysql.pythonanywhere-services.com    Database: wedx$wedx
-- ------------------------------------------------------
-- Server version	5.6.27-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Body`
--

DROP TABLE IF EXISTS `Body`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Body` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `height` int(11) DEFAULT NULL,
  `weight` int(11) DEFAULT NULL,
  `complexion` varchar(30) DEFAULT NULL,
  `hair_colour` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `Body_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Body`
--

LOCK TABLES `Body` WRITE;
/*!40000 ALTER TABLE `Body` DISABLE KEYS */;
INSERT INTO `Body` VALUES (1,'Shreyas_shreyas',160,60,'brown','black'),(2,'1RV15EC043',NULL,NULL,'Pale','Black'),(3,'Shankrith',170,73,'Brown','Black'),(4,'spap',164,53,'Fair','Black'),(5,'RS',160,65,'Fair','Black'),(6,'sahr',176,65,'Fair','Red'),(7,'Ashana',159,52,'Brown','Black'),(8,'dubby',NULL,NULL,'Pale','Black'),(9,'Dp',165,43,'Brown','Black'),(10,'Rahul',189,69,'Dark','Black'),(11,'anirudhkm',173,70,'Brown','Black'),(12,'Balaji Vignesh',178,70,'Fair','Black'),(13,'Kermit',30,2,'Dark','Black'),(14,'aravindbs',178,72,'Dark','Black'),(15,'Deesiya',NULL,NULL,'Pale','Black'),(16,'ashmita',160,NULL,'Pale','Black'),(17,'raviaravindravi',167,45,'Fair','Black'),(18,'Amit',162,59,'Dark','Blonde'),(19,'Vindhya',152,44,'Pale','Black'),(20,'Srüjan ',180,78,'Brown','Black'),(21,'anirudh',175,70,'Brown','Black'),(22,'vindhya2',10,5,'Fair','Black'),(23,'varier',177,65,'Fair','Black'),(24,'Rajnee',NULL,NULL,'Pale','Black'),(25,'allbright',174,68,'Fair','Black');
/*!40000 ALTER TABLE `Body` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Education`
--

DROP TABLE IF EXISTS `Education`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Education` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `school` varchar(150) NOT NULL,
  `under_grad` varchar(150) DEFAULT NULL,
  `post_grad` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `Education_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Education`
--

LOCK TABLES `Education` WRITE;
/*!40000 ALTER TABLE `Education` DISABLE KEYS */;
INSERT INTO `Education` VALUES (1,'Shankrith','The Brigade School','RVCE',''),(2,'1RV15EC043','Cluny Convent High School','RVCE',''),(3,'RS','','',''),(4,'Ashana','KV malleshwaram','Mount Carmel','At Josephs'),(5,'Akarshita Shankar','','B.E',''),(6,'sahr','NPS','CMRIT','Hopefully Stanford '),(7,'dubby','SKCH','RVCE',''),(8,'Dp','Vagdevi','NITK',''),(9,'anirudhkm','Jain Heritage','RVCE',''),(10,'Rahul','Little lillies school ','St Xaviers','St Xaviers'),(11,'Balaji Vignesh','Deeksha centre for learning','RV College of Engineering',''),(12,'Tequila','Sanskriti school ','SanskritH College','Sanskritham College'),(13,'Kermit','Lake view high','Bellandur lake',''),(14,'Madhulika ','Sree Cauvery School ','R. V. College of Engineering ','University of Michigan '),(15,'Mandara','','',''),(16,'aravindbs','NPS','RVCE',''),(17,'Deesiya','','',''),(18,'ashmita','NPS','RVCE',''),(19,'Amit','','',''),(20,'studboi','','',''),(21,'Vindhya','Ghgshhs','Jjsjssj','Dhjsjsks'),(22,'Srüjan ','NHVPS','RVCE','yell seat sigatho alli'),(23,'anirudh','Sindhi','RVCE',''),(24,'vindhya2','Carmel','RVCE',''),(25,'varier','DPS East','RVCE',''),(26,'Rajnee','Who do you want me to teach? ','Before I was born ','Lol'),(27,'allbright','Indian High School','RVCE','');
/*!40000 ALTER TABLE `Education` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employment`
--

DROP TABLE IF EXISTS `Employment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Employment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `occupation` varchar(150) DEFAULT NULL,
  `designation` varchar(150) DEFAULT NULL,
  `company_name` varchar(150) DEFAULT NULL,
  `salary` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `Employment_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employment`
--

LOCK TABLES `Employment` WRITE;
/*!40000 ALTER TABLE `Employment` DISABLE KEYS */;
INSERT INTO `Employment` VALUES (1,'Shankrith','','','',NULL),(2,'RS','A','Software engineer','WEDx',10000),(3,'Akarshita Shankar','','','',NULL),(4,'sahr','Full time hogger','Singer','Earth',9223372036854775807),(5,'dubby','student','','',NULL),(6,'Dp','','','',NULL),(7,'anirudhkm','','','',NULL),(8,'Balaji Vignesh','','','',NULL),(9,'ashmita','','','',NULL),(10,'Kermit','Seducer','The best ','Love. Inc',0),(11,'Madhulika ','','','',NULL),(12,'aravindbs','Student ','','',NULL),(13,'Deesiya','','','',NULL),(14,'Amit','Engineer','Enginner','ABCD',99999999999999999),(15,'studboi','','','',NULL),(16,'Vindhya','','','',NULL),(17,'Srüjan ','Student','None','Nang yaar kelsa kodthare ?',404),(18,'anirudh','Engineer','Software Engineer','EXPEDIA',100000),(19,'vindhya2','dancer','','footprints',NULL),(20,'varier','Student','Good Student','Agam',20000),(21,'Rajnee','','','',NULL),(22,'allbright','God','Christian God','Christianity',0);
/*!40000 ALTER TABLE `Employment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ImageGallery`
--

DROP TABLE IF EXISTS `ImageGallery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ImageGallery` (
  `imgid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) DEFAULT NULL,
  `image_filename` varchar(60) NOT NULL,
  `image_path` text NOT NULL,
  PRIMARY KEY (`imgid`),
  KEY `username` (`username`),
  CONSTRAINT `ImageGallery_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ImageGallery`
--

LOCK TABLES `ImageGallery` WRITE;
/*!40000 ALTER TABLE `ImageGallery` DISABLE KEYS */;
INSERT INTO `ImageGallery` VALUES (1,NULL,'dummy_dp.png','../static/img/dummy_dp.png'),(3,'Shreyas_shreyas','1511699361893735097495.jpg','../static/img/1511699361893735097495.jpg'),(4,'aravindbs','DSC_1417.jpg','../static/img/DSC_1417.jpg'),(5,'Balaji Vignesh','2017-11-01-18-14-44.jpg','../static/img/2017-11-01-18-14-44.jpg'),(6,'Balaji Vignesh','2017-11-01-18-14-44_1.jpg','../static/img/2017-11-01-18-14-44_1.jpg'),(7,'Kermit','images_4.jpg','../static/img/images_4.jpg'),(10,'anirudh','kondu.jpg','../static/img/kondu.jpg'),(11,'vindhya2','doll.jpg','../static/img/doll.jpg'),(12,'varier','chutiya.jpg','../static/img/chutiya.jpg'),(13,'allbright','jesus.jpg','../static/img/jesus.jpg'),(14,'ashmita','bby.jpg','../static/img/bby.jpg');
/*!40000 ALTER TABLE `ImageGallery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Messages`
--

DROP TABLE IF EXISTS `Messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Messages` (
  `msgid` int(11) NOT NULL AUTO_INCREMENT,
  `sender_username` varchar(150) NOT NULL,
  `receiver_username` varchar(150) NOT NULL,
  `subject` varchar(50) DEFAULT NULL,
  `body` text NOT NULL,
  `timestamp` varchar(50) NOT NULL,
  PRIMARY KEY (`msgid`),
  KEY `sender_username` (`sender_username`),
  CONSTRAINT `Messages_ibfk_1` FOREIGN KEY (`sender_username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Messages`
--

LOCK TABLES `Messages` WRITE;
/*!40000 ALTER TABLE `Messages` DISABLE KEYS */;
INSERT INTO `Messages` VALUES (1,'ashmita','Shreyas_shreyas','Request Accepted','ashmita has accepted your request to view their profile.','2017-11-26 12:36'),(2,'Shreyas_shreyas','ashmita','BS is awesome','Hi ','2017-11-26 12:40'),(3,'ashmita','Shreyas_shreyas','no','','2017-11-26 12:42'),(4,'Kermit','ashmita','Looking to copulate ','Nice body ','2017-11-26 14:50'),(5,'Kermit','aravindbs','Looking to copulate ','Nice body ','2017-11-26 14:51'),(6,'ashmita','aravindbs','Request Accepted','ashmita has accepted your request to view their profile.','2017-11-26 17:17'),(7,'ashmita','Kermit','pls fo','','2017-11-26 17:18'),(8,'ashmita','aravindbs','Let\'s fill our success story.','Accept this request so that I can fill out our success story. <a href=\" /acceptProposal/ashmita\"  >Accept</a> <a href=\" /rejectProposal/ashmita\"  >Reject</a>','2017-11-26 17:31'),(9,'aravindbs','ashmita','Request Accepted','aravindbs has accepted your request to view their profile.','2017-11-26 18:41'),(10,'ashmita','aravindbs','tnx','','2017-11-26 18:49'),(11,'aravindbs','ashmita','Nin','Ajji','2017-11-26 18:49'),(12,'Rahul','Kermit','Lol','Waddup ','2017-11-27 01:58'),(13,'Madhulika ','ashmita','Request Accepted','Madhulika  has accepted your request to view their profile.','2017-11-27 14:32'),(14,'vindhya2','anirudh','Request Accepted','vindhya2 has accepted your request to view their profile.','2017-11-27 15:26'),(15,'vindhya2','anirudh','Let\'s fill our success story.','Accept this request so that I can fill out our success story. <a href=\" /acceptProposal/vindhya2\"  >Accept</a> <a href=\" /rejectProposal/vindhya2\"  >Reject</a>','2017-11-27 15:26'),(16,'anirudh','vindhya2','Request Accepted','anirudh has accepted your request to view their profile.','2017-11-27 15:26'),(17,'anirudh','vindhya2','Request to fill story Accepted','anirudh has accepted your request to fill stories. Please deactivate your profile so that it is not searchable and not viewable.   <a href=\" /createStory/anirudh\"  >Please add story.</a>','2017-11-27 15:26'),(18,'vindhya2','anirudh','Let\'s fill our success story.','Accept this request so that I can fill out our success story. <a href=\" /acceptProposal/vindhya2\"  >Accept</a> <a href=\" /rejectProposal/vindhya2\"  >Reject</a>','2017-11-27 15:26'),(19,'allbright','varier','Request Accepted','allbright has accepted your request to view their profile.','2017-11-27 15:45'),(20,'varier','allbright','Request Accepted','varier has accepted your request to view their profile.','2017-11-27 15:45'),(21,'varier','allbright','Let\'s fill our success story.','Accept this request so that I can fill out our success story. <a href=\" /acceptProposal/varier\"  >Accept</a> <a href=\" /rejectProposal/varier\"  >Reject</a>','2017-11-27 15:45'),(22,'allbright','varier','Request to fill story Accepted','allbright has accepted your request to fill stories. Please deactivate your profile so that it is not searchable and not viewable.   <a href=\" /createStory/allbright\"  >Please add story.</a>','2017-11-27 15:46'),(23,'ashmita','Srüjan ','Request Accepted','ashmita has accepted your request to view their profile.','2017-11-27 16:02');
/*!40000 ALTER TABLE `Messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Partner_Preferences`
--

DROP TABLE IF EXISTS `Partner_Preferences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Partner_Preferences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `height` varchar(50) DEFAULT NULL,
  `occupation` varchar(150) DEFAULT NULL,
  `salary` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `hometown` varchar(60) DEFAULT NULL,
  `mother_tongue` varchar(60) DEFAULT NULL,
  `current_location` varchar(20) DEFAULT NULL,
  `about` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `Partner_Preferences_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Partner_Preferences`
--

LOCK TABLES `Partner_Preferences` WRITE;
/*!40000 ALTER TABLE `Partner_Preferences` DISABLE KEYS */;
INSERT INTO `Partner_Preferences` VALUES (1,'Shreyas_shreyas',NULL,'','','female','','Kannada','Bangalore Urban',''),(2,'1RV15EC043','','','','male','','','',''),(3,'Shankrith','','','','male','','','',''),(4,'RS','150-160','Doctor','10000','male','Aizawl','Urdu','Aizawl','Vrhdbs'),(5,'Akarshita Shankar','','','','male','','','',''),(6,'sahr','190','Full time hogger','10000000000000000000000000','male','Bangalore Urban','Tamil','Bangalore Urban',''),(7,'Ashana','169','Doctor','10000000 p.a','male','North West Delhi','Bengali','Bangalore Urban',''),(8,'dubby','','','','male','','','',''),(9,'akhilprasad97','','','','male','','','',''),(10,'Dp','','','','male','','Tamil','',''),(11,'Rahul','169','Anything ','100000000 p.a','male','Bankura','Odia','Bharatpur','Bisexual '),(12,'anirudhkm','','','','male','','','',''),(13,'Balaji Vignesh','','','','female','','','Bangalore Urban',''),(14,'Kermit','2','House wife','0','female','Adilabad','Sanskrit','Adilabad','She better be desperate'),(15,'aravindbs','160','Student','0','female','Bangalore Urban','','Bangalore Urban',''),(16,'Deesiya','','','','male','','','',''),(17,'raviaravindravi','155','Housewife','0','male','Bangalore Urban','Kannada','Bangalore Urban','No specifics'),(18,'Amit','Any','Any','99999999999999999','female','Bangalore Urban','Kannada','Bangalore Urban',''),(19,'Vindhya','185','Not engineer','300000000000','male','','Malayalam','Bangalore Urban','Tall guy needed xD '),(20,'Srüjan ','0-150','Yes','0-1','female','Hooghly','Sanskrit','Bangalore Urban','Needs to tag in at least 3 posts a day'),(21,'anirudh','0-130','Engineer','0-10000','female','Kolar','Telugu','Bangalore Urban','Naive dancer'),(22,'vindhya2','170','Engineer','10000','male','Chittoor','Telugu','Bangalore Urban',' '),(23,'varier','175','God','0','male','Udupi','English','Bangalore Urban','Must not have committed any sins. '),(24,'Rajnee','','','','male','','','',''),(25,'allbright','170','Student','0','male','Thrissur','Malayalam','Bangalore Urban','Must be ready to convert. ');
/*!40000 ALTER TABLE `Partner_Preferences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Profiles`
--

DROP TABLE IF EXISTS `Profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `image_id` int(11) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `hometown` varchar(60) DEFAULT NULL,
  `dob` date NOT NULL,
  `mother_tongue` varchar(60) DEFAULT NULL,
  `about` text,
  `marital_status` varchar(20) DEFAULT NULL,
  `current_location` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `Profiles_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profiles`
--

LOCK TABLES `Profiles` WRITE;
/*!40000 ALTER TABLE `Profiles` DISABLE KEYS */;
INSERT INTO `Profiles` VALUES (1,'ashmita','Ashmita','Raju',14,'female','Bangalore Urban','1997-08-03','Tamil','','Single','Bangalore Urban'),(2,'Shreyas_shreyas','Shreyas ','S ',3,'male','Bangalore Urban','1997-11-03','Kannada','','single','Belgaum'),(4,'test','test5','',1,'male','','1998-09-09','','','single',''),(5,'deek28','Deekshit','BN',1,'male','Bangalore Urban','1997-06-28','Telugu','Lol','Single','Bangalore Urban'),(6,'Anomitro Datta','Anomitro','Datta',1,'male','Kolkata','1996-09-28','Bengali','','Single','Bangalore Urban'),(7,'Shankrith','Shankrith','Natarajan',1,'male','Chennai','1997-11-11','Tamil','','Single','Bangalore Urban'),(8,'1RV15EC043','Divya','Giridhar',1,'female','Bangalore Urban','1997-02-20','Tamil','','Single','Bangalore Urban'),(9,'King Khan','King','Khan',1,'male','Hassan','1982-11-26','Urdu','I\'m cool and hot','Single','Bangalore Urban'),(10,'RS','R','S',1,'male','Bangalore Urban','1997-04-11','Kannada','','Single','Bangalore Urban'),(11,'Ashana','Ashana','Shetty ',1,'female','Bangalore Urban','1989-12-13','Kannada','','Single','Bangalore Urban'),(12,'aravindbs','Aravind','B S',4,'male','Bangalore Urban','1997-03-04','Kannada','Single and Ready to Mingle ','Single','Bangalore Urban'),(13,'Akarshita Shankar','Akarshita','Shankar',1,'female','Bangalore Urban','1997-01-02','Tamil','','Single','Bangalore Urban'),(14,'sahr','Sahana','R',1,'female','Bangalore Urban','1997-03-23','Tamil','I swing both ways. If you can\'t handle that level of epicness, walk away.','Single','Bangalore Urban'),(15,'dubby','Abhishek','Krishna',1,'male','Bangalore Urban','1997-04-17','Tamil','I\'m Dubby','Single','Bangalore Urban'),(16,'Dp','Dhinesh','Pounmuthu',1,'male','Bangalore Urban','1998-01-26','Tamil','I\'m gay','Single','Mysore'),(17,'anirudhkm','Anirudh','Konduru',1,'male','Bangalore Urban','1997-09-10','Telugu','','Single','Bangalore Urban'),(18,'Rahul','Rahul','Menon',1,'male','Bilaspur','1991-10-11','Gujarati','Bisexual ','Poly','Bharatpur'),(19,'Balaji Vignesh','Balaji Vignesh','K',6,'male','Bangalore Urban','1998-01-11','Tamil','Looks like a nerd. Isn\'t one.','Single','Bangalore Urban'),(20,'Tequila','Tequila ','Beer',1,'female','Badgam','1890-06-01','Urdu','I\'m a vampire ','Poly','Bangalore Urban'),(21,'Kermit','Kermit','The frog',7,'male','Adilabad','2017-11-26','Sanskrit','An Amphibious seducer, I be wetter than your wettest dreams. So lets make this rainbow connection, the lovers and dreamers and me','Poly','Adilabad'),(22,'Madhulika ','Madhulika','Prasad',1,'female','Bangalore Urban','1997-07-08','Kannada','','Single','Bangalore Urban'),(23,'Mandara','Mandara','R',1,'female','Bangalore Urban','1997-08-06','Kannada','','Single','Bangalore Urban'),(24,'Deesiya','Dish','M',1,'female','South Delhi','1990-08-26','Hindi','','Single','Bangalore Urban'),(25,'raviaravindravi','RAVI ','B.V.',1,'male','Bangalore Urban','1995-01-21','Kannada','No specifics','Single','Bangalore Urban'),(26,'Amit','Amit','Subrahmanya',1,'male','Bangalore Urban','1996-11-26','Kannada','Hi','Single','Bangalore Urban'),(27,'studboi','BS','K',1,'male','Surendranagar','2017-11-15','Gujarati','Bleh','Single','Aizawl'),(28,'Vindhya','Vindhya','N',1,'female','Bangalore Urban','1997-07-29','','','Single','Bangalore Urban'),(29,'Srüjan ','Srüjan','Rangayyan',1,'male','Bangalore Urban','1997-01-31','Kannada','Fifa and Facebook tagging','Single','Bangalore Urban'),(30,'anirudh','Anirudh','Konduru',10,'male','Bangalore Urban','1997-09-09','Telugu','Attention beku ','Single','Bangalore Rural'),(31,'vindhya2','Kylie ','Jenner',11,'female','Bangalore Rural','1997-07-29','Telugu','Dancer','Single','Bangalore Rural'),(32,'varier','Aravind','Varier',12,'male','Thrissur','1997-10-14','Malayalam','I don\'t have a beard. ','Poly','Bangalore Urban'),(33,'Rajnee','Rajni','Kanth',1,'male','Chennai','0001-12-29','Tamil','Do I even need to? ','Poly','Chennai'),(34,'allbright','Allbright ','D\'Souza',13,'male','Udupi','1997-08-21','English','I am Jesus. Pray to me or die. ','Single','Bangalore Urban');
/*!40000 ALTER TABLE `Profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Requests`
--

DROP TABLE IF EXISTS `Requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Requests` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `to_username` varchar(150) NOT NULL,
  `from_username` varchar(150) NOT NULL,
  `status` varchar(10) NOT NULL,
  PRIMARY KEY (`request_id`),
  KEY `to_username` (`to_username`),
  CONSTRAINT `Requests_ibfk_1` FOREIGN KEY (`to_username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Requests`
--

LOCK TABLES `Requests` WRITE;
/*!40000 ALTER TABLE `Requests` DISABLE KEYS */;
INSERT INTO `Requests` VALUES (1,'ashmita','Shreyas_shreyas','accepted'),(2,'sahr','aravindbs','requested'),(3,'ashmita','aravindbs','accepted'),(4,'sahr','ashmita','requested'),(5,'aravindbs','ashmita','accepted'),(6,'Shreyas_shreyas','ashmita','requested'),(7,'Vindhya','aravindbs','requested'),(8,'Vindhya','ashmita','requested'),(9,'Madhulika','ashmita','accepted'),(10,'ashmita','Srüjan ','accepted'),(11,'vindhya2','anirudh','accepted'),(12,'anirudh','vindhya2','accepted'),(13,'allbright','varier','accepted'),(14,'varier','allbright','accepted');
/*!40000 ALTER TABLE `Requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Search`
--

DROP TABLE IF EXISTS `Search`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Search` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `searchable` tinyint(1) DEFAULT NULL,
  `username` varchar(60) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL,
  `occupation` varchar(150) DEFAULT NULL,
  `salary` bigint(20) DEFAULT NULL,
  `under_grad` varchar(150) DEFAULT NULL,
  `post_grad` varchar(150) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `hometown` varchar(60) DEFAULT NULL,
  `mother_tongue` varchar(60) DEFAULT NULL,
  `current_location` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `Search_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Search`
--

LOCK TABLES `Search` WRITE;
/*!40000 ALTER TABLE `Search` DISABLE KEYS */;
INSERT INTO `Search` VALUES (1,1,'ashmita',20,160,'',NULL,'RVCE','','female','Bangalore Urban','Tamil','Bangalore Urban'),(2,1,'Shreyas_shreyas',20,160,NULL,NULL,NULL,NULL,'male','Bangalore Urban','Kannada','Belgaum'),(4,1,'test',19,NULL,NULL,NULL,NULL,NULL,'male','','',''),(5,1,'deek28',20,NULL,NULL,NULL,NULL,NULL,'male','Bangalore Urban','Telugu','Bangalore Urban'),(6,1,'Anomitro Datta',21,NULL,NULL,NULL,NULL,NULL,'male','Kolkata','Bengali','Bangalore Urban'),(7,1,'Shankrith',20,170,'',NULL,'RVCE','','male','Chennai','Tamil','Bangalore Urban'),(8,1,'1RV15EC043',20,NULL,NULL,NULL,'RVCE','','female','Bangalore Urban','Tamil','Bangalore Urban'),(9,1,'King Khan',35,NULL,NULL,NULL,NULL,NULL,'male','Hassan','Urdu','Bangalore Urban'),(10,1,'RS',20,160,'A',10000,'','','male','Bangalore Urban','Kannada','Bangalore Urban'),(11,1,'Ashana',27,159,NULL,NULL,'Mount Carmel','At Josephs','female','Bangalore Urban','Kannada','Bangalore Urban'),(12,1,'aravindbs',20,178,'Student ',NULL,'RVCE','','male','Bangalore Urban','Kannada','Bangalore Urban'),(13,1,'Akarshita Shankar',20,NULL,'',NULL,'B.E','','female','Bangalore Urban','Tamil','Bangalore Urban'),(14,1,'sahr',20,176,'Full time hogger',9223372036854775807,'CMRIT','Hopefully Stanford ','female','Bangalore Urban','Tamil','Bangalore Urban'),(15,1,'dubby',20,NULL,'student',NULL,'RVCE','','male','Bangalore Urban','Tamil','Bangalore Urban'),(16,1,'Dp',19,165,'',NULL,'NITK','','male','Bangalore Urban','Tamil','Mysore'),(17,1,'anirudhkm',20,173,'',NULL,'RVCE','','male','Bangalore Urban','Telugu','Bangalore Urban'),(18,1,'Rahul',26,189,NULL,NULL,'St Xaviers','St Xaviers','male','Bilaspur','Gujarati','Bharatpur'),(19,1,'Balaji Vignesh',19,178,'',NULL,'RV College of Engineering','','male','Bangalore Urban','Tamil','Bangalore Urban'),(20,1,'Tequila',127,NULL,NULL,NULL,'SanskritH College','Sanskritham College','female','Badgam','Urdu','Bangalore Urban'),(21,1,'Kermit',0,30,'Seducer',0,'Bellandur lake','','male','Adilabad','Sanskrit','Adilabad'),(22,1,'Madhulika ',20,NULL,'',NULL,'R. V. College of Engineering ','University of Michigan ','female','Bangalore Urban','Kannada','Bangalore Urban'),(23,1,'Mandara',20,NULL,NULL,NULL,'','','female','Bangalore Urban','Kannada','Bangalore Urban'),(24,1,'Deesiya',27,NULL,'',NULL,'','','female','South Delhi','Hindi','Bangalore Urban'),(25,1,'raviaravindravi',22,167,NULL,NULL,NULL,NULL,'male','Bangalore Urban','Kannada','Bangalore Urban'),(26,1,'Amit',21,162,'Engineer',99999999999999999,'','','male','Bangalore Urban','Kannada','Bangalore Urban'),(27,1,'studboi',0,NULL,'',NULL,'','','male','Surendranagar','Gujarati','Aizawl'),(28,1,'Vindhya',20,152,'',NULL,'Jjsjssj','Dhjsjsks','female','Bangalore Urban','','Bangalore Urban'),(29,1,'Srüjan ',20,180,'Student',404,'RVCE','yell seat sigatho alli','male','Bangalore Urban','Kannada','Bangalore Urban'),(30,1,'anirudh',20,175,'Engineer',100000,'RVCE','','male','Bangalore Urban','Telugu','Bangalore Rural'),(31,1,'vindhya2',20,10,'dancer',NULL,'RVCE','','female','Bangalore Rural','Telugu','Bangalore Rural'),(32,1,'varier',20,177,'Student',20000,'RVCE','','male','Thrissur','Malayalam','Bangalore Urban'),(33,1,'Rajnee',2015,NULL,'',NULL,'Before I was born ','Lol','male','Chennai','Tamil','Chennai'),(34,1,'allbright',20,174,'God',0,'RVCE','','male','Udupi','English','Bangalore Urban');
/*!40000 ALTER TABLE `Search` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Social_Media`
--

DROP TABLE IF EXISTS `Social_Media`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Social_Media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `facebook` varchar(150) NOT NULL,
  `instagram` varchar(150) NOT NULL,
  `linkedin` varchar(150) NOT NULL,
  `twitter` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `Social_Media_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Social_Media`
--

LOCK TABLES `Social_Media` WRITE;
/*!40000 ALTER TABLE `Social_Media` DISABLE KEYS */;
INSERT INTO `Social_Media` VALUES (1,'Shankrith','https://www.facebook.com/shankrith','https://www.instagram.com/','https://www.linkedin.com/','https://www.twitter.com/'),(2,'1RV15EC043','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/','https://www.twitter.com/'),(3,'RS','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/','https://www.twitter.com/'),(4,'sahr','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/','https://www.twitter.com/'),(5,'dubby','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/','https://www.twitter.com/'),(6,'Dp','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/','https://www.twitter.com/'),(7,'Balaji Vignesh','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/','https://www.twitter.com/'),(8,'anirudhkm','https://www.facebook.com/anirudhkm97','https://www.instagram.com/','https://www.linkedin.com/anirudhkonduru','https://www.twitter.com/'),(9,'Kermit','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(10,'Madhulika ','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(11,'aravindbs','https://www.facebook.com/aravindbs','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(12,'Deesiya','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(13,'Amit','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(14,'Vindhya','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(15,'Srüjan ','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(16,'anirudh','https://www.facebook.com/anirudhkm97','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(17,'vindhya2','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(18,'varier','https://www.facebook.com/arvind.varier.5','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(19,'Rajnee','https://www.facebook.com/','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/'),(20,'allbright','https://www.facebook.com/allbright.dsouza','https://www.instagram.com/','https://www.linkedin.com/in/','https://www.twitter.com/');
/*!40000 ALTER TABLE `Social_Media` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('e859f2081465');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `success_stories`
--

DROP TABLE IF EXISTS `success_stories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `success_stories` (
  `succ_id` int(11) NOT NULL AUTO_INCREMENT,
  `username1` varchar(150) NOT NULL,
  `username2` varchar(150) NOT NULL,
  `story` text NOT NULL,
  `timestamp` varchar(50) NOT NULL,
  PRIMARY KEY (`succ_id`),
  KEY `username1` (`username1`),
  CONSTRAINT `success_stories_ibfk_1` FOREIGN KEY (`username1`) REFERENCES `users` (`username`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `success_stories`
--

LOCK TABLES `success_stories` WRITE;
/*!40000 ALTER TABLE `success_stories` DISABLE KEYS */;
INSERT INTO `success_stories` VALUES (1,'vindhya2','anirudh','Our love blossomed when we met each other on WEDx. Thank you WEDx for bringing us together. ','2017-11-27 15:28'),(3,'varier','allbright','Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis cursus sapien mattis massa gravida porttitor. Etiam euismod sem quis sollicitudin auctor. Donec lacinia rutrum mi non suscipit. Vivamus in quam ullamcorper, suscipit diam non, scelerisque augue. Vestibulum gravida orci ac dui aliquam, vitae consequat purus consectetur. In facilisis consectetur nisi. Nunc quis tristique turpis. Donec porttitor convallis felis mattis auctor. Fusce rhoncus felis et varius rhoncus. Nam blandit nibh ac','2017-11-27 15:48');
/*!40000 ALTER TABLE `success_stories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(60) DEFAULT NULL,
  `username` varchar(60) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'ashmita.raju@gmail.com','ashmita','pbkdf2:sha256:50000$6qz8mzS6$367d4c41f889e64afce8cbda1d61b8096d9c40f8b42d71f3c34e5c1c2a0036ca'),(2,'ksshreyas97@gmail.com','Shreyas_shreyas','pbkdf2:sha256:50000$JVgGwi4s$97d603f2da62fdc4c23717fdabf257745dd2bde956905e932969a4ca482a4fcc'),(4,'test@wedx.com','test','pbkdf2:sha256:50000$DgWooi8t$31e5eae22596dcf4b9db0520742040aed9b891b24608967484a398a85bc18c09'),(5,'dkshtbn@gmail.com','deek28','pbkdf2:sha256:50000$qslLhPUj$9076ee68518da02b812e6ef1e1e759c2ac939a9adee6a62ad3a4bd68b2c65f34'),(6,'anomitrodatta@gmail.com','Anomitro Datta','pbkdf2:sha256:50000$0xqncvlF$1a073f3200dd7c9e248b9ee6af2a45c46d7a75aab2a085dc998ab0121041f22b'),(7,'sushantopraharaj@gmail.com','spap','pbkdf2:sha256:50000$2LVdNdY2$b443323ab825794db1385c7641880208c5646a496c9ecb188406a79e131d1faf'),(8,'sahana.ram.2397@gmail.com','sahr','pbkdf2:sha256:50000$UtYM2byF$a19dcf5a63a8e2bd525c28fac311408c7569de1dff7c05ddb5aa9269e68ca4fc'),(9,'shankrith@gmail.com','Shankrith','pbkdf2:sha256:50000$gxlXPpUz$337dc3ba38c3dbba0965e5976199fb0e36468985acfb7e892b178460e346244e'),(10,'divyagiridhar123@gmail.com','1RV15EC043','pbkdf2:sha256:50000$DZc4DFIS$df4acbd2cf2a422cc36ea6801075ef1e3aafa7540753b4cd14b01a4aa71b5e27'),(11,'aswiftie11@gmail.com','Ashana','pbkdf2:sha256:50000$cW4XdxQ6$a4b652f60559e24fc45d3ec4bbf50c0532f4deb75c7dab55462e8af5de1f3ef7'),(12,'mynameiskhan@gmail.com','King Khan','pbkdf2:sha256:50000$CdfgVI51$43cf30f41ec305dc22f2561bef6fecee20e8b8d762e7e033fcf4c0be21e6f8db'),(13,'askarthikkumar@gmail.com','askarthikkumar','pbkdf2:sha256:50000$Q4ETUL5r$35b038d515df9d451075ad908f778f95aaad174cdc84712457b5c40a85975255'),(14,'aakanksha.ash13@gmail.com','Aakanksha','pbkdf2:sha256:50000$ZCTh82Xd$f6096f2676491909e92c22a8ef0f4c4b1ed1aac637ef5f35bea7bc2c335b75fe'),(15,'aditya.giridharan@gmail.com','Giri','pbkdf2:sha256:50000$NIgmsmzn$871f078bc61e992482d4b04bb7b9917ff3da9985e55a264fdde92f0903f62c5a'),(16,'rohansimha11@gmail.com','RS','pbkdf2:sha256:50000$DKcSuF3R$8e8515a6de560644007ddfd021df063068113dc875fe7c9aee845412b59146eb'),(17,'sarthakshetty97@gmail.com','sartek','pbkdf2:sha256:50000$D2EKejAr$2213d7966d5c464f606e2c2a58df26a3e9b14024483417243e70e927380a29f1'),(18,'Duniyakabaap@hotmail.com','Qwerty','pbkdf2:sha256:50000$tUG0NAtu$5bc918a91898f54cfbff0fd72752373f9093165720ced8b8aa802473f28a3b79'),(19,'bs.aravind.97@gmail.com','aravindbs','pbkdf2:sha256:50000$7z3qqt5H$f0e51761ed01163c3f500f0ae307ea7d3f95db69b70a1c37396acad460908115'),(20,'aku1997@hotmail.com','Akarshita Shankar','pbkdf2:sha256:50000$HZIpPPUL$6b48d820b82856af63e9041706cdb3cbac4931e4e73109d707ba308a8b6bd58b'),(21,'abhishekkrishna123@outlook.com','dubby','pbkdf2:sha256:50000$vaH91uFE$8ec7ce521baa9fc900bd8348a2f7801846b8992d187053802adf4701006edd91'),(22,'akhilprasad97@gmail.com','akhilprasad97','pbkdf2:sha256:50000$9IGQx98T$96ebdec806f6a52634bd4a17503e610d8047bf1efddbb29ab3910e9c343bb416'),(23,'dhrp98@gmail.com','Dp','pbkdf2:sha256:50000$j0WqdW0E$f5300439a514eaf7240b182ceffd8c25118fe65888cc3954fdc39946d7f0ed08'),(24,'anirudhkm.cs15@rvce.edu.in','anirudhkm','pbkdf2:sha256:50000$yoQh7pj7$ca1081d1e70ee2525d59b627105aa9c271dbfe8f0d106a2f77edeae88ce14421'),(25,'tmskrupnik@gmail.com','Rahul','pbkdf2:sha256:50000$a5jnxcfB$50c3236aee2707cea47f15ed92a398e74d6a3b8cfb6cbbbe497fe45fd95af5a1'),(26,'balvig.ca@gmail.com','Balaji Vignesh','pbkdf2:sha256:50000$BwvrzcF4$3de70793432897ce3de3048f4c627ad4744c08f5dcc4aa2013bb2c0abe272880'),(27,'Doremiojamajo@gmail.com','Doremi','pbkdf2:sha256:50000$aJeBnA9L$44eb16f55c7bc9d8d02f2aa58f8b964d443e3a7525b59abe722dd7fa5d6fb721'),(28,'Supriyaarun@rocketmail.con','Fluffyx','pbkdf2:sha256:50000$XJ839iY4$956c86a48b064cb49bb459e76cc71c67b090c442514778a58877d3dc5f757ce9'),(29,'Waddupbitches@gmail.com','Tequila','pbkdf2:sha256:50000$LfpZTL8t$ce85167039246f3320300980328cd2ebaa4c521bdf2c1881220108a6d7491e2e'),(30,'gmail@gmail.com','Kermit','pbkdf2:sha256:50000$hyMinBl2$97bfa01ab94bd8dbb7038ad492753ef070001fe07cfdf3bdd3e2fb9187390a78'),(31,'raagini.jm@gmail.com','Raagini','pbkdf2:sha256:50000$WSUcZVMu$8201266da5005ecca5002bd100b640ac0e0f951ebddea9749dfabae7f5677f26'),(32,'Sushanto@gmail.com','Sushanto','pbkdf2:sha256:50000$Ribu7uaj$946d340e995233c8861f1957e0fb75a2b2347c8b9a4633f62c149fc0ec0c1422'),(33,'sruthi31Srinivasan@gmail.com','Sruthi Srinivasan','pbkdf2:sha256:50000$arq3YLar$dd642b7bad22af57a0884681ce9c6c1e7ac6bdfc820cdca7aec0d7ef0f549730'),(34,'test1@wedx.com','test1','pbkdf2:sha256:50000$KqeICLdO$3e5e10c883e2a86bf5d77a3c70f87a45d303ff425cc1d32cd52978beb596c3b3'),(35,'nakaralo4@gmail.com','Nakara','pbkdf2:sha256:50000$iA7fVKrG$62eb98b375b547ba2ad649355990999afbf6aeb31f1b40b38cf5fabc80ea7423'),(36,'unknown@gmail.com','Anamica','pbkdf2:sha256:50000$5nz2SzF6$7a2a7095780987e4063d3f422daca8dcc0a9bb4ea4500cba5b3589d5f64c49f7'),(37,'madhulikashivaprasad08@gmail.com','Madhulika ','pbkdf2:sha256:50000$79AZdSAC$41bb7dbdab299a81a9a48ec3daa7eb5b0e626aa8bdefca492beccbec512203b2'),(38,'mandaramadhu@gmail.com','Mandara','pbkdf2:sha256:50000$CWy626lD$d87d624c78aef2b77d62865b719e8828e514786278275e59f7b30b61db5f837f'),(39,'dishasiya2623@gmail.com','Deesiya','pbkdf2:sha256:50000$EaH7DpgP$ec86c2aedbe7f2a4e5fc1f21f8497a84d83070c535b30561884a1d7ad997fbd2'),(40,'raviaravindravi@gmail.com','raviaravindravi','pbkdf2:sha256:50000$q1WrDRZ6$58cc4ba239ec2a3fdfd03a318fb007a06548d22755f5772061cb064dc15ebb45'),(41,'saiyaman122@gmail.com','Amit','pbkdf2:sha256:50000$cGdfvWkg$385b078c62d7fe1a2283072682ccb193d4cd9f323bc28ec118fd7947c7511f5e'),(42,'emailid@gmail.com','studboi','pbkdf2:sha256:50000$JWrbhmEm$12e65481e74c239849cd54ac6ddeed3ef4488fc998c749d622aaccba7719701c'),(43,'Vin@gmail.com','Vindhya','pbkdf2:sha256:50000$mzxEYsVS$859714e067d25688be8406299521a7a5fdf62614b8b7a3ccaf2b9078df8f5483'),(44,'fabregas.srujan@gmail.com','Srüjan ','pbkdf2:sha256:50000$Cm898eFr$976bde699cf87a4f2ac120d9d59a7371910e080b2f1a1256ac1e831bb649c5ac'),(45,'gagangowda26@gmail.com','Deep26','pbkdf2:sha256:50000$PM0W1RDz$b2686dfa8259848960326a659fdb667c32302653adac86acedecf8af381aba74'),(46,'anirudh@wedx.com','anirudh','pbkdf2:sha256:50000$at03lLaO$c8d724088b81f847575937e80bec32096ad2c93d2c27f012e0eacb57648d9c74'),(47,'kumarthenextcricketer@gmail.com','sai srivatsa kumar','pbkdf2:sha256:50000$eh5VgTEx$a7e4fe04ac99ca453042c60b9b9a004abb24c84e8a891304fe294c49262ff544'),(48,'vin@yahoo.com','vindhya2','pbkdf2:sha256:50000$TXvx7wZN$2a9ede3e78d2f2170ba8f03c3b4bcf8bd2b747a35b28810acc47a56f782e29af'),(49,'varier@wedx.com','varier','pbkdf2:sha256:50000$PIihiBiW$2d7d0fe72952b9de58c6da6b10a44e9d9521ae385229e53466d9f4d939290971'),(50,'Gmail@Rajnikanth.com','Rajnee','pbkdf2:sha256:50000$DkW46bFt$a00e7370a9c8e8bd5b0b4ee48bc6f629816ce8747a7dbae7f486e59aa646bb94'),(51,'jesus@wedx.com','allbright','pbkdf2:sha256:50000$jF3dFmIN$b230100c9a17a064c75494c7238e8dd20192ff3a2655dc85b02ce486da5f9451');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-27 16:43:48

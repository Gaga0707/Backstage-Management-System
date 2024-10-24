-- MySQL dump 10.13  Distrib 8.2.0, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: proj
-- ------------------------------------------------------
-- Server version	8.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'Primary Key',
  `ck_name` varchar(255) DEFAULT NULL,
  `kh_name` varchar(255) DEFAULT NULL,
  `region` int DEFAULT NULL,
  `gg` varchar(255) DEFAULT NULL,
  `ck_column` varchar(255) DEFAULT NULL,
  `ck_row` int DEFAULT NULL,
  `layer` int DEFAULT NULL,
  `box_num` varchar(255) DEFAULT NULL,
  `records_series` enum('civil','economy') DEFAULT NULL,
  `records_date` enum('temporory','lasting') DEFAULT NULL,
  `box2_num` int DEFAULT NULL,
  `goods_num` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'1','1',1,'1','1ax',1,1,'1','civil','temporory',1,1),(2,'qwe','qwe',2,'2','qwe',3,2,'sdf','economy','temporory',2,2),(3,'zxc','cvbcvz',3,'3','szxc',4,4,'asd','civil','temporory',3,3),(4,'asd','zxc',4,'4','ad',5,5,'asd','economy','temporory',4,4),(5,'as','asc',5,'5','asd',6,6,'asd','economy','temporory',5,5),(6,'ad','asd',6,'6','asd',7,7,'asd','economy','temporory',6,6),(7,'sd','c',7,'7','xcz',8,8,'asdad','civil','temporory',7,7),(8,'asd','sd',8,'8','xcv',9,23,'fdxvc','economy','temporory',34,23),(9,'sadf','zc',9,'9','asd',34,34,'sdfxc','economy','temporory',123,73),(10,'x ','xcvx',10,'10','zcxz',12,45,'sdfsdf','economy','temporory',11,52),(11,'sd','fvs',11,'11','cvxbfdb',23,56,'xcvsd','civil','temporory',34,65),(12,'cxvb','dfa',12,'12','xc',56,32,'xcvvs','economy','temporory',123,54),(13,'xcv','zx',13,'13','hdfg',43,12,'f','civil','temporory',45,21),(14,'dfs','xcv',14,'14','sdfq',87,87,'df','economy','temporory',53,42),(15,'v cb','ngh',15,'15','fg',46,67,'s','civil','temporory',23,31),(16,'asdf','sd',16,'16','hy',45,46,'sdf','economy','temporory',46,97),(17,'asdzx','az',985,'4','asdqw',74,74,'fgh','economy','temporory',45,86),(18,'asdasd','zxc',211,'24','dasd',75,57,'grt','civil','temporory',42,53),(19,'hg','dasd',8,'78','xc',67,12,'yrt','economy','temporory',24,75),(20,'zxc','asd',84,'86','as',7,12,'fgh','civil','temporory',12,24),(21,'asd','asd',433,'85','asd',41,68,'yr','economy','temporory',17,86);
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-11 23:58:24

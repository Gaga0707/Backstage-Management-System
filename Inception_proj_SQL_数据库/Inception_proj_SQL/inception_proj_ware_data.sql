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
-- Table structure for table `ware`
--

DROP TABLE IF EXISTS `ware`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ware` (
  `name` varchar(100) DEFAULT NULL,
  `master` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `commit` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ware`
--

/*!40000 ALTER TABLE `ware` DISABLE KEYS */;
INSERT INTO `ware` VALUES ('x','x','x','x'),('hsy','lxr','y102','zxy'),('xyq','zzy','103','hzy'),('kemailuo','huya','2862','great'),('bad','sun','gun','pond'),('adas','fghfgh','h','bnv'),('zxc','yf','n','vvb'),('dfg','hnghn','f','nv'),('wererg','ggh','vbnvb','vnb'),('df','v','vbn','n'),('htyh','ghg','vbnvb','f'),('fg','bn','v','nvbghfg'),('rttr','f','bn','fgh'),('asdas','fgh','hfg','asd'),('ads','hfg','fg','asd'),('asd','fg','fghfg','asd'),('dasd','fgh','t','sdasd'),('zxc','fgh','hfhgr','sd'),('asdasd','fghvb','hfgh','asd'),('asd','fgh','asd','a'),('xc','vadasz','zxc','asd');
/*!40000 ALTER TABLE `ware` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-11 23:59:35

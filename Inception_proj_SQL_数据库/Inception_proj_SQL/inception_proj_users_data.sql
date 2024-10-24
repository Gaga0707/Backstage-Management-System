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
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `logname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `realname` varchar(100) DEFAULT NULL,
  `user_type` enum('普通用户','管理员','客户') DEFAULT NULL,
  `gender` enum('男','女') DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cellphone` varchar(100) DEFAULT NULL,
  `workphone` varchar(100) DEFAULT NULL,
  `user_state` enum('正常','禁用') DEFAULT NULL,
  `del_state` enum('正常','已删除') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('hbc','123456','黄必成','普通用户','男','xxx','xxx','xxx','正常','正常'),('lxr','123456','刘骁然','管理员','男','xxx','xxx','xxx','正常','正常'),('cyw','123456','程翊玮','客户','男','xxx','xxx','xxx','正常','正常'),('lbw','123456','罗博文','管理员','男','xxx','xxx','xxx','正常','正常'),('zxy','123456','郑茜予','管理员','女','xxx','xxx','xxx','正常','正常'),('ysz','123456','杨舜喆','管理员','女','xxx','xxx','xxx','正常','正常'),('zzy','123','小曾','普通用户','男','xxx','xxx','xxx','正常','正常'),('hzy','123456','小黄','普通用户','男','xxx','xxx','xxx','正常','正常'),('x1','123','小红','客户','女','xxx','xxx','xxx','正常','正常'),('x2','123','小军','普通用户','男','xxx','xxx','xxx','正常','正常'),('x3','1123','raze','客户','女','xxx','xxx','xxx','正常','正常'),('x4','123','iso','普通用户','男','xxx','xxx','xxx','正常','正常'),('x5','123','MIkey','管理员','男','xxx','xxx','xxx','正常','正常'),('x6','123','Daniel','普通用户','男','xxx','xxx','xxx','正常','正常'),('x7','123','Anne','普通用户','女','xxx','xxx','xxx','正常','正常'),('x8','123','Helen','管理员','女','xxx','xxx','xxx','正常','正常'),('x9','123','John','客户','男','xxx','xxx','xxx','正常','正常'),('x10','123','Tony','普通用户','男','xxx','xxx','xxx','正常','正常'),('x111','123','Saber','管理员','女','xxx','xxx','xxx','正常','正常'),('Panda','123','熊猫','普通用户','男','xxx','xxx','xxx','正常','正常'),('hsy','123','何松谕','管理员','男','1121719482@qq.com','+8619841623725','wwww','正常','正常');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-11 23:59:06

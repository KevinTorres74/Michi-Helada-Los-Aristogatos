-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: ing_soft
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `administrador`
--

DROP TABLE IF EXISTS `administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `administrador` (
  `id_administrador` int auto_increment NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `telefono` int NOT NULL,
  `fna` date NOT NULL,
  `contraseña` varchar(45) NOT NULL,
  PRIMARY KEY (`id_administrador`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrador`
--

LOCK TABLES `administrador` WRITE;
/*!40000 ALTER TABLE `administrador` DISABLE KEYS */;
/*!40000 ALTER TABLE `administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `atender`
--

DROP TABLE IF EXISTS `atender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `atender` (
  `id_vendedor` int NOT NULL,
  `id_pedido` int NOT NULL,
  `id_cliente` int NOT NULL,
  KEY `fk_vendedors_idx` (`id_vendedor`),
  KEY `fk_pedido_idx` (`id_pedido`),
  KEY `fk_clientesAt_idx` (`id_cliente`),
  CONSTRAINT `fk_clientesAt` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_pedidos` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id_pedido`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_vendedors` FOREIGN KEY (`id_vendedor`) REFERENCES `vendedor` (`id_vendedor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atender`
--

LOCK TABLES `atender` WRITE;
/*!40000 ALTER TABLE `atender` DISABLE KEYS */;
/*!40000 ALTER TABLE `atender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `id_cliente` int auto_increment NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `telefono` int NOT NULL,
  `fna` date DEFAULT NULL,
  `contraseña` varchar(45) NOT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;


--
-- Table structure for table `contener`
--

DROP TABLE IF EXISTS `contener`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contener` (
  `id_producto` int NOT NULL,
  `id_cliente` int NOT NULL,
  `id_pedido` int NOT NULL,
  KEY `fk_product_1_idx` (`id_producto`),
  KEY `fk_client_1_idx` (`id_cliente`),
  KEY `fk_pedido_1_idx` (`id_pedido`),
  CONSTRAINT `fk_client_1` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_pedido_1` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id_pedido`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_product_1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contener`
--

LOCK TABLES `contener` WRITE;
/*!40000 ALTER TABLE `contener` DISABLE KEYS */;
/*!40000 ALTER TABLE `contener` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hacer`
--

DROP TABLE IF EXISTS `hacer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hacer` (
  `id_vendedor` int NOT NULL,
  `id_cliente` int NOT NULL,
  `id_reporteDeVenta` int NOT NULL,
  `id_pedido` int NOT NULL,
  KEY `fk_hacer_vendedor_idx` (`id_vendedor`),
  KEY `fk_hacer_cliente_idx` (`id_cliente`),
  KEY `fk_hacer_reporte_idx` (`id_reporteDeVenta`),
  KEY `fk_hacer_pedido_idx` (`id_pedido`),
  CONSTRAINT `fk_hacer_cliente` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_hacer_pedido` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id_pedido`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_hacer_reporte` FOREIGN KEY (`id_reporteDeVenta`) REFERENCES `reporteDeVenta` (`id_reporteDeVenta`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_hacer_vendedor` FOREIGN KEY (`id_vendedor`) REFERENCES `vendedor` (`id_vendedor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hacer`
--

LOCK TABLES `hacer` WRITE;
/*!40000 ALTER TABLE `hacer` DISABLE KEYS */;
/*!40000 ALTER TABLE `hacer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incluir`
--

DROP TABLE IF EXISTS `incluir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `incluir` (
  `id_insumo` int NOT NULL,
  `id_vendedor` int NOT NULL,
  `id_inventario` int NOT NULL,
  `diaDeCompra` date NOT NULL,
  `caducidad` date NOT NULL,
  `cantidad` int NOT NULL,
  KEY `fk_insumo_idx` (`id_insumo`),
  KEY `fk_vendedor_idx` (`id_vendedor`),
  KEY `fk_inventario_idx` (`id_inventario`),
  CONSTRAINT `fk_insumo` FOREIGN KEY (`id_insumo`) REFERENCES `insumo` (`id_insumo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_inventario` FOREIGN KEY (`id_inventario`) REFERENCES `inventario` (`id_inventario`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_vendedor` FOREIGN KEY (`id_vendedor`) REFERENCES `vendedor` (`id_vendedor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incluir`
--

LOCK TABLES `incluir` WRITE;
/*!40000 ALTER TABLE `incluir` DISABLE KEYS */;
/*!40000 ALTER TABLE `incluir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insumo`
--

DROP TABLE IF EXISTS `insumo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insumo` (
  `id_insumo` int auto_increment NOT NULL,
  `nombre` varchar(45) NOT NULL,
  PRIMARY KEY (`id_insumo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insumo`
--

LOCK TABLES `insumo` WRITE;
/*!40000 ALTER TABLE `insumo` DISABLE KEYS */;
/*!40000 ALTER TABLE `insumo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventario`
--

DROP TABLE IF EXISTS `inventario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventario` (
  `id_inventario` int auto_increment NOT NULL,
  `id_vendedor` int NOT NULL,
  `fechaDeinventario` date NOT NULL,
  PRIMARY KEY (`id_inventario`),
  UNIQUE KEY `id_vendedor_UNIQUE` (`id_vendedor`),
  CONSTRAINT `vendedor` FOREIGN KEY (`id_vendedor`) REFERENCES `vendedor` (`id_vendedor`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventario`
--

LOCK TABLES `inventario` WRITE;
/*!40000 ALTER TABLE `inventario` DISABLE KEYS */;
/*!40000 ALTER TABLE `inventario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ocupar`
--

DROP TABLE IF EXISTS `ocupar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ocupar` (
  `id_insumo` int NOT NULL,
  `id_producto` int NOT NULL,
  `cantidad` int NOT NULL,
  KEY `insumo_idx` (`id_insumo`),
  KEY `producto_idx` (`id_producto`),
  CONSTRAINT `insumo` FOREIGN KEY (`id_insumo`) REFERENCES `insumo` (`id_insumo`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `producto` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ocupar`
--

LOCK TABLES `ocupar` WRITE;
/*!40000 ALTER TABLE `ocupar` DISABLE KEYS */;
/*!40000 ALTER TABLE `ocupar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pedido`
--

DROP TABLE IF EXISTS `pedido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pedido` (
  `id_pedido` int auto_increment NOT NULL,
  `id_cliente` int NOT NULL,
  `fecha_pedido` date NOT NULL,
  PRIMARY KEY (`id_pedido`),
  KEY `fk_clientes_idx` (`id_cliente`),
  CONSTRAINT `fk_clientes` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pedido`
--

LOCK TABLES `pedido` WRITE;
/*!40000 ALTER TABLE `pedido` DISABLE KEYS */;
/*!40000 ALTER TABLE `pedido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_producto` int auto_increment NOT NULL,
  `id_administrador` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `precio` double NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `imagen` varchar(200) NOT NULL,
  `disponibilidad` tinyint NOT NULL,
  PRIMARY KEY (`id_producto`,`id_administrador`),
  KEY `fk_producto_1_idx` (`id_administrador`),
  CONSTRAINT `fk_producto_1` FOREIGN KEY (`id_administrador`) REFERENCES `administrador` (`id_administrador`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reporteDeVenta`
--

DROP TABLE IF EXISTS `reporteDeVenta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reporteDeVenta` (
  `id_reporteDeVenta` int auto_increment NOT NULL,
  `id_cliente` int NOT NULL,
  `id_pedido` int NOT NULL,
  PRIMARY KEY (`id_reporteDeVenta`),
  UNIQUE KEY `idreporteDeVenta_UNIQUE` (`id_reporteDeVenta`),
  UNIQUE KEY `id_pedido_UNIQUE` (`id_pedido`),
  KEY `fk_clienteReporte_idx` (`id_cliente`),
  CONSTRAINT `fk_clienteReporte` FOREIGN KEY (`id_cliente`) REFERENCES `cliente` (`id_cliente`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_pedidosR` FOREIGN KEY (`id_pedido`) REFERENCES `pedido` (`id_pedido`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reporteDeVenta`
--

LOCK TABLES `reporteDeVenta` WRITE;
/*!40000 ALTER TABLE `reporteDeVenta` DISABLE KEYS */;
/*!40000 ALTER TABLE `reporteDeVenta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendedor`
--

DROP TABLE IF EXISTS `vendedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendedor` (
  `id_vendedor` int auto_increment NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `telefono` int NOT NULL,
  `fna` date NOT NULL,
  `contraseña` varchar(45) NOT NULL,
  PRIMARY KEY (`id_vendedor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendedor`
--

LOCK TABLES `vendedor` WRITE;
/*!40000 ALTER TABLE `vendedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `vendedor` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-11 20:54:38

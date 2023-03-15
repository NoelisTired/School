SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `toolshed`
--
DROP DATABASE IF EXISTS `toolshed`;
CREATE DATABASE IF NOT EXISTS `toolshed` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `toolshed`;

--
-- Tabel: `tools`
--

DROP TABLE IF EXISTS `tools`;
CREATE TABLE IF NOT EXISTS `tools` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `weight` int(11) NOT NULL,
  `location` varchar(255) NOT NULL,
  `since` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


INSERT INTO `tools` (`title`, `weight`, `location`, `since`) VALUES ('Hamer', 1, 'Rek 5B', '2020-08-01');
INSERT INTO `tools` (`title`, `weight`, `location`, `since`) VALUES ('Zaag', 2, 'Kast 31', '1995-08-01');
INSERT INTO `tools` (`title`, `weight`, `location`, `since`) VALUES ('Sloophamer', 5, 'Rek 2D', NULL);
INSERT INTO `tools` (`title`, `weight`, `location`, `since`) VALUES ('Graafmachine', 5000, 'Garage 3', '2005-03-26');
INSERT INTO `tools` (`title`, `weight`, `location`, `since`) VALUES ('Nijptang', 1, 'Kast 9', NULL);
INSERT INTO `tools` (`title`, `weight`, `location`, `since`) VALUES ('Hark', 3, 'Rek 5A', '2018-12-09');

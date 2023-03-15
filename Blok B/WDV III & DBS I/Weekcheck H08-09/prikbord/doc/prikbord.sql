SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `prikbord`
--
DROP DATABASE IF EXISTS `prikbord`;
CREATE DATABASE IF NOT EXISTS `prikbord` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `prikbord`;

--
-- Tabel: `berichten`
--

DROP TABLE IF EXISTS `berichten`;
CREATE TABLE IF NOT EXISTS `berichten` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `author` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


INSERT INTO `berichten` (`title`, `content`, `author`) VALUES ('Lorem ipsum', 'Dolor sit amet, consectetur adipiscing elit. Proin ac euismod orci, sit amet congue lacus.', NULL);
INSERT INTO `berichten` (`title`, `content`, `author`) VALUES ('Mauris vel malesuada nunc', 'Aliquam pharetra elit magna, at porttitor mauris pretium dictum.', 'A. uteur');
INSERT INTO `berichten` (`title`, `content`, `author`) VALUES ('Nulla fringilla', 'Mi leo, eget cursus neque maximus eu. Aenean nec enim tincidunt.', NULL);
INSERT INTO `berichten` (`title`, `content`, `author`) VALUES ('Cras vitae', 'Integer pulvinar purus vitae vestibulum interdum. Integer ut placerat nisl, vitae euismod orci. Cras interdum vel leo ut dictum. Vestibulum congue vel diam non dignissim. Cras et finibus massa.', 'S. Vestdijk');
INSERT INTO `berichten` (`title`, `content`, `author`) VALUES ('Suspendisse et', 'Aliquam viverra fermentum eros non viverra.', 'G. Orwell');
INSERT INTO `berichten` (`title`, `content`, `author`) VALUES ('Pellentesque mattis', 'Quam ac pharetra facilisis, lacus sapien molestie tellus, non ornare leo nisl et velit. Morbi gravida et nunc sed finibus.', NULL);

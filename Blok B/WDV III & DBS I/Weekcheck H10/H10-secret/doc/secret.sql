SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `secret`
--
DROP DATABASE IF EXISTS `secret`;
CREATE DATABASE IF NOT EXISTS `secret` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `secret`;

--
-- Tabel: `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` text NOT NULL,
  `password` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


INSERT INTO `users` (`username`, `password`) VALUES ('user', '$2y$10$VzmyNAYE11zPscL2nd/OyuAaGVQNFM38OBQ4ea9ClVyJTrycbH24G');

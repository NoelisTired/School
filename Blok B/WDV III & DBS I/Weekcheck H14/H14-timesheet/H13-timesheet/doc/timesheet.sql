SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `timesheet`
--
DROP DATABASE IF EXISTS `timesheet`;
CREATE DATABASE IF NOT EXISTS `timesheet` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `timesheet`;

--
-- Tabel: `logs`
--

DROP TABLE IF EXISTS `logs`;
CREATE TABLE IF NOT EXISTS `logs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` int(11) NOT NULL,
  `date` date NOT NULL,
  `duration` int(11) NOT NULL,
  `department` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


INSERT INTO `logs` (`user`, `date`, `duration`, `department`) VALUES ('1', '2021-03-26', 9, 'horeca');
INSERT INTO `logs` (`user`, `date`, `duration`, `department`) VALUES ('1', '2021-03-27', 8, 'horeca');
INSERT INTO `logs` (`user`, `date`, `duration`, `department`) VALUES ('2', '2021-03-28', 7, 'attracties');
INSERT INTO `logs` (`user`, `date`, `duration`, `department`) VALUES ('2', '2021-03-29', 6, 'attracties');
INSERT INTO `logs` (`user`, `date`, `duration`, `department`) VALUES ('3', '2021-03-30', 5, 'techniek');
INSERT INTO `logs` (`user`, `date`, `duration`, `department`) VALUES ('3', '2021-03-31', 4, 'groen');

--
-- Tabel: `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `manager` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

INSERT INTO `users` (`name`, `username`, `password`) VALUES ('O. ber',      'user1', '$2y$10$K3/tOrxhzoSqS19Slgw6AeH6NCeSGTGMvakfObfvYEkFN9osquEpG');
INSERT INTO `users` (`name`, `username`, `password`) VALUES ('G. astvrouw', 'user2', '$2y$10$K3/tOrxhzoSqS19Slgw6AeH6NCeSGTGMvakfObfvYEkFN9osquEpG');
INSERT INTO `users` (`name`, `username`, `password`) VALUES ('T. echnicus', 'user3', '$2y$10$K3/tOrxhzoSqS19Slgw6AeH6NCeSGTGMvakfObfvYEkFN9osquEpG');

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 16, 2023 at 09:17 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance_s_1`
--

DROP TABLE IF EXISTS `attendance_s_1`;
CREATE TABLE IF NOT EXISTS `attendance_s_1` (
  `Course_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Teacher_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Credits` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Semester` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Lectures` int NOT NULL,
  `Presents` int NOT NULL,
  `Absents` int NOT NULL,
  UNIQUE KEY `Course_Name` (`Course_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `attendance_s_1`
--

INSERT INTO `attendance_s_1` (`Course_Name`, `Teacher_Name`, `Credits`, `Semester`, `Lectures`, `Presents`, `Absents`) VALUES
('Advance Computer Programming', 'Mam Ammarah Khalid', '3(2-1)', '5', 26, 23, 3),
('Compiler Construction', 'Mam Sahar Gull', '3(3-0)', '5', 26, 26, 0),
('Introduction to Software Engineering', 'Sir Rizwan Anwar', '3(3-0)', '5', 31, 27, 4),
('Operating Systems', 'Sir Arslan Rauf', '4(3-1)', '5', 44, 39, 5),
('Psychology', 'Mam Asia Atif', '3(3-0)', '5', 15, 14, 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance_s_1`
--
ALTER TABLE `attendance_s_1`
  ADD CONSTRAINT `Attendance_S_1_ibfk_1` FOREIGN KEY (`Course_Name`) REFERENCES `enrollments_s_1` (`Course_Name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

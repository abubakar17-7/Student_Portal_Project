-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 16, 2023 at 09:16 AM
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
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
CREATE TABLE IF NOT EXISTS `courses` (
  `Course_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Credits` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Semester` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`Course_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` (`Course_Name`, `Credits`, `Semester`) VALUES
('Advance Computer Programming', '3(2-1)', '5'),
('Applied Physics', '3(3-0)', '1'),
('Calculus & Analytical Geometry', '3(3-0)', '2'),
('Communication and Presentation Skills', '3(3-0)', '2'),
('Compiler Construction', '3(3-0)', '5'),
('Computer Organization and Assembly Language', '4(3-1)', '3'),
('Data Communication', '3(3-0)', '4'),
('Data Structures and Algorithms', '4(3-1)', '3'),
('Database Systems', '4(3-1)', '4'),
('Design and Analysis of Algorithms', '3(3-0)', '4'),
('Digital Logic and Design', '4(3-1)', '2'),
('Discrete Structures', '3(3-0)', '1'),
('English Composition and Comprehension', '3(3-0)', '1'),
('Introduction to Information and Communication Technology', '3(2-1)', '1'),
('Introduction to Software Engineering', '3(3-0)', '5'),
('Life & Living Vl (Introduction to Hadees & Seerah-ll)', '1(1-0)', '4'),
('Life & Living-I (Islamic Studies)', '2(2-0)', '1'),
('Life & Living-IV (Revealed Sciences-II)', '1(1-0)', '3'),
('Life & Living-V (Introduction to Hadees & Seerah-l)', '1(1-0)', '4'),
('Life and Living -II (Pakistan Studies)', '2(2-0)', '2'),
('Life and Living -III (Revealed Sciences-I)', '1(1-0)', '2'),
('Linear Algebra', '3(3-0)', '3'),
('Object Oriented Programming', '4(3-1)', '2'),
('Operating Systems', '4(3-1)', '5'),
('Probability and Statistics', '3(3-0)', '4'),
('Programming Fundamentals', '4(3-1)', '1'),
('Psychology', '3(3-0)', '5'),
('Sociology', '3(3-0)', '3'),
('Theory of Automata', '3(3-0)', '4'),
('Web Design Application', '3(2-1)', '3');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 16, 2023 at 09:18 AM
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
-- Table structure for table `result_s_3`
--

DROP TABLE IF EXISTS `result_s_3`;
CREATE TABLE IF NOT EXISTS `result_s_3` (
  `Course_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Teacher_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Credits` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Semester` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Mid` int NOT NULL,
  `Sessional` int NOT NULL,
  `Final` int NOT NULL,
  UNIQUE KEY `Course_Name` (`Course_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `result_s_3`
--

INSERT INTO `result_s_3` (`Course_Name`, `Teacher_Name`, `Credits`, `Semester`, `Mid`, `Sessional`, `Final`) VALUES
('Applied Physics', 'Sir Danish Abid', '3(3-0)', '1', 18, 49, 16),
('Calculus & Analytical Geometry', 'Sir Umar Riaz', '3(3-0)', '2', 20, 50, 18),
('Communication and Presentation Skills', 'Sir Akhtar Ali', '3(3-0)', '2', 15, 51, 18),
('Computer Organization and Assembly Language', 'Sir Abdul Ghaffar', '4(3-1)', '3', 18, 36, 36),
('Data Communication', 'Sir Tanveer Younis', '3(3-0)', '4', 24, 18, 30),
('Data Structures and Algorithms', 'Sir Mudassar Alam', '4(3-1)', '3', 18, 38, 34),
('Database Systems', 'Sir Usman Zamir', '4(3-1)', '4', 16, 32, 32),
('Design and Analysis of Algorithms', 'Mam Farah Naz', '3(3-0)', '4', 30, 23, 28),
('Digital Logic and Design', 'Sir Qasim Ashfaq', '4(3-1)', '2', 14, 43, 17),
('Discrete Structures', 'Sir Nadeem Abbas', '3(3-0)', '1', 18, 59, 13),
('English Composition and Comprehension', 'Mam Zahra Rubab', '3(3-0)', '1', 15, 46, 15),
('Introduction to Information and Communication Technology', 'Mam Qurat ul Ain', '3(2-1)', '1', 16, 49, 16),
('Life & Living Vl (Introduction to Hadees & Seerah-ll)', 'Sir Usama Ashraf', '1(1-0)', '4', 15, 30, 38),
('Life & Living-I (Islamic Studies)', 'Sir Umer Raheel', '2(2-0)', '1', 15, 45, 11),
('Life & Living-IV (Revealed Sciences-II)', 'Sir Ishfaq Nawaz', '1(1-0)', '3', 21, 24, 31),
('Life & Living-V (Introduction to Hadees & Seerah-l)', 'Sir Usama Ashraf', '1(1-0)', '4', 24, 27, 25),
('Life and Living -II (Pakistan Studies)', 'Sir Imran Ahmed', '2(2-0)', '2', 28, 45, 19),
('Life and Living -III (Revealed Sciences-I)', 'Sir Shams ul Arifeen', '1(1-0)', '2', 15, 42, 17),
('Linear Algebra', 'Mam Nosheen Zafar', '3(3-0)', '3', 26, 27, 32),
('Object Oriented Programming', 'Mam Qurat ul Ain', '4(3-1)', '2', 9, 51, 15),
('Probability and Statistics', 'Sir Ashraf Malik', '3(3-0)', '4', 19, 27, 30),
('Programming Fundamentals', 'Mam Farwah Sahar', '4(3-1)', '1', 18, 59, 13),
('Sociology', 'Sir Junaid Rasool', '3(3-0)', '3', 14, 26, 30),
('Theory of Automata', 'Sir Pervez Akhtar', '3(3-0)', '4', 25, 26, 40),
('Web Design Application', 'Sir Shahzeb Javed', '3(2-1)', '3', 11, 37, 32);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `result_s_3`
--
ALTER TABLE `result_s_3`
  ADD CONSTRAINT `Result_S_3_ibfk_3` FOREIGN KEY (`Course_Name`) REFERENCES `enrollments_s_3` (`Course_Name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

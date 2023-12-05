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
-- Table structure for table `enrollments_s_2`
--

DROP TABLE IF EXISTS `enrollments_s_2`;
CREATE TABLE IF NOT EXISTS `enrollments_s_2` (
  `Course_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Teacher_Name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Credits` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Semester` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  UNIQUE KEY `Course_Name` (`Course_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `enrollments_s_2`
--

INSERT INTO `enrollments_s_2` (`Course_Name`, `Teacher_Name`, `Credits`, `Semester`) VALUES
('Advance Computer Programming', 'Mam Ammarah Khalid', '3(2-1)', '5'),
('Applied Physics', 'Sir Danish Abid', '3(3-0)', '1'),
('Calculus & Analytical Geometry', 'Sir Umar Riaz', '3(3-0)', '2'),
('Communication and Presentation Skills', 'Sir Akhtar Ali', '3(3-0)', '2'),
('Compiler Construction', 'Mam Sahar Gull', '3(3-0)', '5'),
('Computer Organization and Assembly Language', 'Sir Abdul Ghaffar', '4(3-1)', '3'),
('Data Communication', 'Sir Tanveer Younis', '3(3-0)', '4'),
('Data Structures and Algorithms', 'Sir Mudassar Alam', '4(3-1)', '3'),
('Database Systems', 'Sir Usman Zamir', '4(3-1)', '4'),
('Design and Analysis of Algorithms', 'Mam Farah Naz', '3(3-0)', '4'),
('Digital Logic and Design', 'Sir Qasim Ashfaq', '4(3-1)', '2'),
('Discrete Structures', 'Sir Nadeem Abbas', '3(3-0)', '1'),
('English Composition and Comprehension', 'Mam Zahra Rubab', '3(3-0)', '1'),
('Introduction to Information and Communication Technology', 'Mam Qurat ul Ain', '3(2-1)', '1'),
('Introduction to Software Engineering', 'Sir Rizwan Anwar', '3(3-0)', '5'),
('Life & Living Vl (Introduction to Hadees & Seerah-ll)', 'Sir Usama Ashraf', '1(1-0)', '4'),
('Life & Living-I (Islamic Studies)', 'Sir Umer Raheel', '2(2-0)', '1'),
('Life & Living-IV (Revealed Sciences-II)', 'Sir Ishfaq Nawaz', '1(1-0)', '3'),
('Life & Living-V (Introduction to Hadees & Seerah-l)', 'Sir Usama Ashraf', '1(1-0)', '4'),
('Life and Living -II (Pakistan Studies)', 'Sir Imran Ahmed', '2(2-0)', '2'),
('Life and Living -III (Revealed Sciences-I)', 'Sir Shams ul Arifeen', '1(1-0)', '2'),
('Linear Algebra', 'Mam Nosheen Zafar', '3(3-0)', '3'),
('Object Oriented Programming', 'Mam Qurat ul Ain', '4(3-1)', '2'),
('Operating Systems', 'Sir Arslan Rauf', '4(3-1)', '5'),
('Probability and Statistics', 'Sir Ashraf Malik', '3(3-0)', '4'),
('Programming Fundamentals', 'Mam Farwah Saher', '4(3-1)', '1'),
('Psychology', 'Mam Asia Atif', '3(3-0)', '5'),
('Sociology', 'Sir Junaid Rasool', '3(3-0)', '3'),
('Theory of Automata', 'Sir Pervez Akhtar', '3(3-0)', '4'),
('Web Design Application', 'Sir Shahzeb Javed', '3(2-1)', '3');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `enrollments_s_2`
--
ALTER TABLE `enrollments_s_2`
  ADD CONSTRAINT `Enrollments_S_2_ibfk_2` FOREIGN KEY (`Course_Name`) REFERENCES `courses` (`Course_Name`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

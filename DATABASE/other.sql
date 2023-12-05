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
-- Table structure for table `other`
--

DROP TABLE IF EXISTS `other`;
CREATE TABLE IF NOT EXISTS `other` (
  `Roll_No` int NOT NULL,
  `CNIC` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `DOB` date NOT NULL,
  `Gender` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `M_Status` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Nationality` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Province` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `District` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Tehsile` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Zip_Code` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Mother_Tongue` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `E_mail` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Phone_No` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Blood` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Religion` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Hafiz` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `Disable` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `G_Name` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `G_CNIC` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `G_Phone_No` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `G_E_mail` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`Roll_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `other`
--

INSERT INTO `other` (`Roll_No`, `CNIC`, `DOB`, `Gender`, `M_Status`, `Nationality`, `Province`, `District`, `Tehsile`, `Zip_Code`, `Mother_Tongue`, `E_mail`, `Phone_No`, `Blood`, `Religion`, `Hafiz`, `Disable`, `G_Name`, `G_CNIC`, `G_Phone_No`, `G_E_mail`) VALUES
(1, '33104-8977464-7', '2002-10-02', 'Male', 'Single', 'Pakistani', 'Punjab', 'Faisalabad', 'Jaranwala', '38000', 'Punjabi', 'abubakar10jutt@gmail.com', '+92 320 7539684', 'O+', 'Islam', 'No', 'No', 'Muhammad Afzal', '33104-2233151-1', '+92 333 8682259', 'afzalsanghera04@gmail.com'),
(2, '33100-9259532-7', '2001-09-21', 'Male', 'Single', 'Pakistani', 'Punjab', 'Faisalabad', 'Faisalabad City', '38000', 'Punjabi', 'ranafani001@gmail.com', '+92 300 6659416', 'B+', 'Islam', 'No', 'No', 'Sajid Mehmood', '33100-52523234-7', '+92 300 8669416', 'ranasajid06@gmail.com'),
(3, '33102-1323913-1', '2003-04-09', 'Male', 'Single', 'Pakistani', 'Punjab', 'Faisalabad', 'Faisalabad City', '38000', 'Punjabi', 'mujeebu817@gmail.com', '+92 314 6694417', 'A-', 'Islam', 'No', 'No', 'Mujeeb Ullah', '33102-1323913-1', '+92 314 6694417', 'mujeebu817@gmail.com'),
(4, '', '0000-00-00', 'Male', 'Single', 'Pakistani', 'Punjab', 'Faisalabad', 'Faisalabad City', '38000', 'Punjabi', '', '', '', 'Islam', 'No', 'No', '', '', '', '');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `other`
--
ALTER TABLE `other`
  ADD CONSTRAINT `Other_ibfk_1` FOREIGN KEY (`Roll_No`) REFERENCES `login` (`Roll_No`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

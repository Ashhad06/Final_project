-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 15, 2023 at 12:32 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online_order`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('Ashhad', 'Ashhad');

-- --------------------------------------------------------

--
-- Table structure for table `bovichic`
--

CREATE TABLE `bovichic` (
  `Name` varchar(200) NOT NULL,
  `Price` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `bovichic`
--

INSERT INTO `bovichic` (`Name`, `Price`) VALUES
('Krispo Origin', 280),
('Krispo Ace', 300),
('Krispo Primo', 300),
('Bovino Vegg Buzz', 340),
('Bovino Gustare', 340),
('Frequent Pick Jyro', 340),
('Mexican Charm Jyro', 370),
('Italian Amore Jyro', 390);

-- --------------------------------------------------------

--
-- Table structure for table `broadway`
--

CREATE TABLE `broadway` (
  `Name` varchar(200) NOT NULL,
  `Price` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `broadway`
--

INSERT INTO `broadway` (`Name`, `Price`) VALUES
('Appetizers', 379),
('Wings', 379),
('Salads', 399),
('Phantom Pizza large', 2100),
('Mughlai Beast Pizza large', 2100),
('Tarzan Tikka Pizza large', 2100),
('West Side Garlic Pizza large', 2100);

-- --------------------------------------------------------

--
-- Table structure for table `customer_login`
--

CREATE TABLE `customer_login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `kfc`
--

CREATE TABLE `kfc` (
  `Name` varchar(200) NOT NULL,
  `Price` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kfc`
--

INSERT INTO `kfc` (`Name`, `Price`) VALUES
('Krunch Burger', 270),
('Zingeratha', 350),
('Rice & Spice', 350),
('Twister', 400),
('3 Pcs Chicken', 620),
('Zinger Burger', 550),
('Zinger Stacker', 590),
('Kentucky Burger', 590),
('Mighty Zinger', 700),
('Value Bucket', 1890),
('Pepsi Regular', 140),
('Mirinda Regular', 140),
('Mountain Dew Regular', 140),
('7UP Regular', 140),
('Fries', 270),
('Nuggets', 480);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `Name` varchar(255) NOT NULL,
  `Restaurant` varchar(255) NOT NULL,
  `Bill` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

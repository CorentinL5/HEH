-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 22 nov. 2022 à 20:32
-- Version du serveur :  5.7.31
-- Version de PHP : 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `ex2`
--

-- --------------------------------------------------------

--
-- Structure de la table `installer`
--

DROP TABLE IF EXISTS `installer`;
CREATE TABLE IF NOT EXISTS `installer` (
  `nPoste` varchar(7) DEFAULT NULL,
  `nLog` varchar(5) DEFAULT NULL,
  `numIns` int(5) NOT NULL AUTO_INCREMENT,
  `dateIns` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `delai` decimal(8,2) DEFAULT NULL,
  PRIMARY KEY (`numIns`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `installer`
--

INSERT INTO `installer` (`nPoste`, `nLog`, `numIns`, `dateIns`, `delai`) VALUES
('p2', 'log1', 1, '2003-05-14 22:00:00', NULL),
('p2', 'log2', 2, '2003-09-16 22:00:00', NULL),
('p4', 'log5', 3, NULL, NULL),
('p6', 'log6', 4, '2003-05-19 22:00:00', NULL),
('p6', 'log1', 5, '2003-05-19 22:00:00', NULL),
('p8', 'log2', 6, '2003-05-18 22:00:00', NULL),
('p8', 'log6', 7, '2003-05-19 22:00:00', NULL),
('p11', 'log3', 8, '2003-04-19 22:00:00', NULL),
('p12', 'log4', 9, '2003-04-19 22:00:00', NULL),
('p11', 'log7', 10, '2003-04-19 22:00:00', NULL),
('p7', 'log7', 11, '2002-03-31 22:00:00', NULL);

-- --------------------------------------------------------

--
-- Structure de la table `logiciel`
--

DROP TABLE IF EXISTS `logiciel`;
CREATE TABLE IF NOT EXISTS `logiciel` (
  `nLog` varchar(5) NOT NULL,
  `nomLog` varchar(20) NOT NULL,
  `dateAch` datetime DEFAULT NULL,
  `version` varchar(7) DEFAULT NULL,
  `typeLog` varchar(9) DEFAULT NULL,
  `prix` decimal(6,2) DEFAULT NULL,
  `nbInstall` tinyint(2) DEFAULT '0',
  PRIMARY KEY (`nLog`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `logiciel`
--

INSERT INTO `logiciel` (`nLog`, `nomLog`, `dateAch`, `version`, `typeLog`, `prix`, `nbInstall`) VALUES
('log1', 'Oracle 6', '1995-05-13 00:00:00', '6.2', 'UNIX', '3000.00', 0),
('log2', 'Oracle 8', '1999-09-15 00:00:00', '8i', 'UNIX', '5600.00', 0),
('log3', 'SQL Server', '1998-04-12 00:00:00', '7', 'PCNT', '2700.00', 0),
('log4', 'Front Page', '1997-06-03 00:00:00', '5', 'PCWS', '500.00', 0),
('log5', 'WinDev', '1997-05-12 00:00:00', '5', 'PCWS', '750.00', 0),
('log6', 'SQL*Net', NULL, '2.0', 'UNIX', '500.00', 0),
('log7', 'I. I. S.', '2002-04-12 00:00:00', '2', 'PCNT', '810.00', 0),
('log8', 'DreamWeaver', '2003-09-21 00:00:00', '2.0', 'BeOS', '1400.00', 0);

-- --------------------------------------------------------

--
-- Structure de la table `poste`
--

DROP TABLE IF EXISTS `poste`;
CREATE TABLE IF NOT EXISTS `poste` (
  `nPoste` varchar(7) NOT NULL,
  `nomPoste` varchar(20) NOT NULL,
  `indIP` varchar(11) DEFAULT NULL,
  `ad` varchar(3) DEFAULT NULL,
  `typePoste` varchar(9) DEFAULT NULL,
  `nSalle` varchar(7) DEFAULT NULL,
  PRIMARY KEY (`nPoste`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `poste`
--

INSERT INTO `poste` (`nPoste`, `nomPoste`, `indIP`, `ad`, `typePoste`, `nSalle`) VALUES
('p1', 'Poste 1', '130.120.80', '01', 'TX', 's01'),
('p2', 'Poste 2', '130.120.80', '02', 'UNIX', 's01'),
('p3', 'Poste 3', '130.120.80', '03', 'TX', 's01'),
('p4', 'Poste 4', '130.120.80', '04', 'PCWS', 's02'),
('p5', 'Poste 5', '130.120.80', '05', 'PCWS', 's02'),
('p6', 'Poste 6', '130.120.80', '06', 'UNIX', 's03'),
('p7', 'Poste 7', '130.120.80', '07', 'TX', 's03'),
('p8', 'Poste 8', '130.120.81', '01', 'UNIX', 's11'),
('p9', 'Poste 9', '130.120.81', '02', 'TX', 's11'),
('p10', 'Poste 10', '130.120.81', '03', 'UNIX', 's12'),
('p11', 'Poste 11', '130.120.82', '01', 'PCNT', 's21'),
('p12', 'Poste 12', '130.120.82', '02', 'PCWS', 's21');

-- --------------------------------------------------------

--
-- Structure de la table `salle`
--

DROP TABLE IF EXISTS `salle`;
CREATE TABLE IF NOT EXISTS `salle` (
  `nSalle` varchar(7) NOT NULL,
  `nomSalle` varchar(20) NOT NULL,
  `nbPoste` tinyint(2) DEFAULT NULL,
  `indIP` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`nSalle`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `salle`
--

INSERT INTO `salle` (`nSalle`, `nomSalle`, `nbPoste`, `indIP`) VALUES
('s01', 'Salle 1', 3, '130.120.80'),
('s02', 'Salle 2', 2, '130.120.80'),
('s03', 'Salle 3', 2, '130.120.80'),
('s11', 'Salle 11', 2, '130.120.81'),
('s12', 'Salle 12', 1, '130.120.81'),
('s21', 'Salle 21', 2, '130.120.82'),
('s22', 'Salle 22', 0, '130.120.83'),
('s23', 'Salle 23', 0, '130.120.83');

-- --------------------------------------------------------

--
-- Structure de la table `segment`
--

DROP TABLE IF EXISTS `segment`;
CREATE TABLE IF NOT EXISTS `segment` (
  `indIP` varchar(11) NOT NULL,
  `nomSegment` varchar(20) NOT NULL,
  `etage` tinyint(1) DEFAULT NULL,
  `nbSalle` tinyint(2) DEFAULT '0',
  `nbPoste` tinyint(2) DEFAULT '0',
  PRIMARY KEY (`indIP`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `segment`
--

INSERT INTO `segment` (`indIP`, `nomSegment`, `etage`, `nbSalle`, `nbPoste`) VALUES
('130.120.80', 'Brin RDC', 0, 0, 0),
('130.120.81', 'Brin 1er  étage', 1, 0, 0),
('130.120.82', 'Brin 2ème étage', 2, 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `types`
--

DROP TABLE IF EXISTS `types`;
CREATE TABLE IF NOT EXISTS `types` (
  `typeLP` varchar(9) NOT NULL,
  `nomType` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`typeLP`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `types`
--

INSERT INTO `types` (`typeLP`, `nomType`) VALUES
('TX', 'Terminal X-Window'),
('UNIX', 'Système Unix'),
('PCNT', 'PC Windows  NT'),
('PCWS', 'PC Windows'),
('NC', 'Network Computer');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

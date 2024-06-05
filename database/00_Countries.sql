SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `countries` ;
CREATE SCHEMA IF NOT EXISTS `countries` DEFAULT CHARACTER SET latin1 ;
USE `countries` ;

CREATE TABLE IF NOT EXISTS `countries`.`customers` (
   -- date,sentiment,text,source_country,queried_country,url,Safety Index
   'id' INT NOT NULL AUTO_INCREMENT,
   'date' date NOT NULL,
   'sentiment' FLOAT NOT NULL,
   'text' VARCHAR(100) NOT NULL,
   'source_country' VARCHAR(50) NOT NULL,
   'queried_country' VARCHAR(50) NOT NULL,
   'url' VARCHAR(50) NOT NULL,
   'Safety Index' FLOAT NOT NULL,
    PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
   


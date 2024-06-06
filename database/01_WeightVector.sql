SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

DROP SCHEMA IF EXISTS `country_data` ;
CREATE SCHEMA IF NOT EXISTS `country_data` DEFAULT CHARACTER SET latin1;
USE country_data;

CREATE TABLE IF NOT EXISTS `weight_vector`.`customers` (
    'intercept' FLOAT  
    'weight' FLOAT NOT NULL)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

INSERT INTO weight_vector (intercept, weight)
VALUES (NULL, 0),
(0, 0.0),
(1, -0.21913580557953766);

DROP DATABASE IF EXISTS Diplomatic_Data;
CREATE DATABASE IF NOT EXISTS Diplomatic_Data;
USE Diplomatic_Data;

-- Create country table first
DROP TABLE IF EXISTS country;
CREATE TABLE IF NOT EXISTS country
(
    country_id   INT PRIMARY KEY AUTO_INCREMENT,
    country_name VARCHAR(50) UNIQUE NOT NULL,
    safety_index FLOAT,
    country_code VARCHAR(2) UNIQUE NOT NULL
);


-- Create users table
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users
(
    user_id    INT PRIMARY KEY,
    created_at DATE,
    gender     VARCHAR(1),
    email      VARCHAR(255),
    birthdate  DATE,
    first_name VARCHAR(40),
    username   VARCHAR(25),
    country    VARCHAR(50)
);


DROP TABLE IF EXISTS article;
CREATE TABLE IF NOT EXISTS article
(
    article_id            INT AUTO_INCREMENT PRIMARY KEY,
    content               MEDIUMTEXT,
    publication_date      DATETIME,
    article_link          VARCHAR(1000),
    country_written_from  VARCHAR(100),
    sentiment             FLOAT,
    country_written_about VARCHAR(100),
    FOREIGN KEY (country_written_from) REFERENCES country (country_code)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (country_written_about) REFERENCES country (country_name)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


DROP TABLE IF EXISTS views;
CREATE TABLE IF NOT EXISTS views
(
    view_id    INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT,
    article_id INT,
    view_date  DATETIME,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (article_id) REFERENCES article (article_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- Create likes table
DROP TABLE IF EXISTS likes;
CREATE TABLE IF NOT EXISTS likes
(
    like_id    INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT,
    article_id INT UNIQUE NOT NULL,
    like_date  DATETIME,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (article_id) REFERENCES article (article_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- Create saves table
DROP TABLE IF EXISTS saves;
CREATE TABLE IF NOT EXISTS saves
(
    save_id    INT AUTO_INCREMENT PRIMARY KEY,
    user_id    INT,
    article_id INT UNIQUE NOT NULL,
    save_date  DATETIME,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (article_id) REFERENCES article (article_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Create filter table
DROP TABLE IF EXISTS filter;
CREATE TABLE IF NOT EXISTS filter
(
    filter_id             INT PRIMARY KEY AUTO_INCREMENT,
    user_id               INT,
    start_date            DATE,
    end_date              DATE,
    country_written_about VARCHAR(50),
    country_written_from  VARCHAR(50),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (country_written_about) REFERENCES country (country_name)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    FOREIGN KEY (country_written_from) REFERENCES country (country_name)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- Creates the news source table
-- felt cute, might delete later....
DROP TABLE IF EXISTS news_source;
CREATE TABLE IF NOT EXISTS news_source
(
    id                INT PRIMARY KEY,
    name              VARCHAR(255),
    political_leaning VARCHAR(255),
    article_id        INT,
    FOREIGN KEY (article_id) REFERENCES article (article_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Create trending_articles table
DROP TABLE IF EXISTS trending_articles;
CREATE TABLE IF NOT EXISTS trending_articles
(
    trending_id         INT PRIMARY KEY AUTO_INCREMENT,
    article_id          INT,
    views_last_24_hours INT,
    FOREIGN KEY (article_id) REFERENCES article (article_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

DROP TABLE IF EXISTS weight_vector;
CREATE TABLE IF NOT EXISTS weight_vector
(
    sequence_number INT PRIMARY KEY AUTO_INCREMENT,
    beta_vals       VARCHAR(1000)
);

DROP TABLE IF EXISTS forest_vector;
CREATE TABLE IF NOT EXISTS forest_vector
(
    sequence_number INT PRIMARY KEY AUTO_INCREMENT,
    text            MEDIUMTEXT,
    word_count      FLOAT,
    sentiment_score FLOAT,
    queried_country VARCHAR(50),
    source_country  VARCHAR(50)
);


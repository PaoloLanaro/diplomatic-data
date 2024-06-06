CREATE DATABASE IF NOT EXISTS Diplomatic_Data;
USE Diplomatic_Data;

-- Create country table first
DROP TABLE IF EXISTS country;
CREATE TABLE IF NOT EXISTS country (
  country_id INT PRIMARY KEY,
  country_name VARCHAR(50),
  country_tag VARCHAR(2),
  region VARCHAR(255)
);

-- Create users table
DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
  user_id INT PRIMARY KEY,
  created_at DATETIME, 
  gender VARCHAR(1),
  email VARCHAR(255),
  birthdate DATETIME,
  first_name VARCHAR(40),
  username VARCHAR(15),
  country VARCHAR(20)
);

-- Create user_interests table
DROP TABLE IF EXISTS user_interests;
CREATE TABLE IF NOT EXISTS user_interests (
  interests_id INT PRIMARY KEY,
  user_id INT,
  country_id INT,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (country_id) REFERENCES country (country_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Create article table
DROP TABLE IF EXISTS article;
CREATE TABLE IF NOT EXISTS article (
  article_id INT AUTO_INCREMENT PRIMARY KEY,
  content VARCHAR(15000),
  country_id INT,
  publication_date DATETIME,
  article_link VARCHAR(100),
  FOREIGN KEY (country_id) REFERENCES country (country_id)
);

-- Create filter table
DROP TABLE IF EXISTS filter;
CREATE TABLE IF NOT EXISTS filter (
  id INT PRIMARY KEY,
  user_id INT,
  region VARCHAR(255),
  subjects VARCHAR(255),
  start_date DATETIME,
  end_date DATETIME,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Create sentiment_analysis table
DROP TABLE IF EXISTS sentiment_analysis;
CREATE TABLE IF NOT EXISTS sentiment_analysis (
  id INT PRIMARY KEY,
  article_id INT,
  sentiment_score FLOAT,
  analysis_date DATETIME,
  FOREIGN KEY (article_id) REFERENCES article (article_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Creates the news source table 
-- DROP TABLE IF NOT EXISTS news_source;
CREATE TABLE IF NOT EXISTS news_source (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  political_leaning VARCHAR(255),
  article_id INT,
  FOREIGN KEY (article_id) REFERENCES article (article_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

-- Create likes table
DROP TABLE IF EXISTS likes;
CREATE TABLE IF NOT EXISTS likes (
  like_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  article_id INT,
  like_date DATETIME,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (article_id) REFERENCES article (article_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);


-- Create saves table
DROP TABLE IF EXISTS saves;
CREATE TABLE IF NOT EXISTS saves (
  save_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  article_id INT,
  save_date DATETIME,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (article_id) REFERENCES article (article_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);


-- Create shares table
DROP TABLE IF EXISTS shares;
CREATE TABLE IF NOT EXISTS shares (
  share_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  article_id INT,
  share_date DATETIME,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (article_id) REFERENCES article (article_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);



-- Create weight_vector table
DROP TABLE IF EXISTS weight_vector;
CREATE TABLE IF NOT EXISTS weight_vector (
  sequence_number INTEGER AUTO_INCREMENT PRIMARY KEY,
  beta_vals VARCHAR(100)
);


--INSERT INTO weight_vector (beta_vals) VALUES ("[0.0, -0.21913580557953766]");

-- Create recently_viewed table
-- NOT SHOWING 
DROP TABLE IF EXISTS recently_viewed;
CREATE TABLE IF NOT EXISTS recently_viewed (
  view_id INT PRIMARY KEY,
  user_id INT,
  article_id INT,
  date_viewed DATETIME,
  FOREIGN KEY (user_id) REFERENCES users (user_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (article_id) REFERENCES article (article_id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);


-- Create trending_articles table
-- NOT SHOWING 
DROP TABLE IF EXISTS trending_articles;
CREATE TABLE IF NOT EXISTS trending_articles (
  article_id INT PRIMARY KEY,
  relevance INT
);


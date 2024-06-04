DROP DATABASE IF EXISTS Diplomatic_Data;
CREATE DATABASE IF NOT EXISTS Diplomatic_Data;

USE Diplomatic_Data;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users
(
  id INT PRIMARY KEY,
  created_at DATETIME,
  home_country_id INT, 
  gender VARCHAR(255),
  email VARCHAR(255),
  travelling_country_id INT
);

DROP TABLE IF EXISTS user_interests;
CREATE TABLE IF NOT EXISTS user_interests
(
  interests_id INT PRIMARY KEY,
  user_id INT,
  country_id INT,
  FOREIGN KEY (user_id) REFERENCES users (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,
  FOREIGN KEY (country_id) REFERENCES country (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

DROP TABLE IF EXISTS country;
CREATE TABLE IF NOT EXISTS country
(
  id INT PRIMARY KEY,
  country_name VARCHAR(255),
  region VARCHAR(255)
);

DROP TABLE IF EXISTS article;
CREATE TABLE IF NOT EXISTS article
(
  id INT PRIMARY KEY,
  content VARCHAR(15000),
  country_id INT,
  title VARCHAR(255),
  publication_date DATETIME,
  FOREIGN KEY (country_id) REFERENCES country (id)
);

DROP TABLE IF EXISTS filter;
CREATE TABLE IF NOT EXISTS filter
(
  id INT PRIMARY KEY,
  user_id INT,
  region VARCHAR(255),   # unsure how to make this a multi-value
  subjects VARCHAR(255), # unsure how to make this a multi-value
  # time frame attribute,  unsure if this should be two DATETIME values?
  FOREIGN KEY (user_id) REFERENCES users (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

DROP TABLE IF EXISTS sentiment_analysis;
CREATE TABLE IF NOT EXISTS sentiment_analysis
(
  id INT PRIMARY KEY,
  article_id INT,
  sentiment_score FLOAT,
  analysis_date DATETIME,
  FOREIGN KEY (article_id) REFERENCES article (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

DROP TABLE IF EXISTS news_source;
CREATE TABLE IF NOT EXISTS news_source
(
  id INT PRIMARY KEY,
  name VARCHAR(255), 
  political_leaning VARCHAR(255),
  article_id INT,
  FOREIGN KEY (article_id) REFERENCES article (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

DROP TABLE IF EXISTS likes;
CREATE TABLE IF NOT EXISTS likes
(
  id INT PRIMARY KEY,
  user_id INT,
  like_date DATETIME,
  article_id INT,
  FOREIGN KEY (user_id) REFERENCES users (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

DROP TABLE IF EXISTS saves;
CREATE TABLE IF NOT EXISTS saved
(
  id INT PRIMARY KEY,
  article_id INT,
  user_id INT,
  save_date DATETIME,
  FOREIGN KEY (user_id) REFERENCES users (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

DROP TABLE IF EXISTS shares;
CREATE TABLE IF NOT EXISTS shares
(
  id INT PRIMARY KEY,
  user_id INT,
  share_date DATETIME,
  article_id INT,
  FOREIGN KEY (user_id) REFERENCES users (id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);


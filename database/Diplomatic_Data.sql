DROP DATABASE IF EXISTS Diplomatic_Data;
CREATE DATABASE IF NOT EXISTS Diplomatic_Data;

USE Diplomatic_Data;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users
(
  user_id INT PRIMARY KEY,
  created_at DATETIME, 
  gender VARCHAR(1),
  email VARCHAR(255),
  birthdate DATETIME,
  first_name VARCHAR(40),
  username VARCHAR(15),
  country VARCHAR(20)
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
  country_id INT PRIMARY KEY,
  country_name VARCHAR(50),
  country_tag VARCHAR(2),
  region VARCHAR(255)
);

DROP TABLE IF EXISTS article;
CREATE TABLE IF NOT EXISTS article
(
  article_id INT PRIMARY KEY AUTO INCREMENT,
  content VARCHAR(15000),
  country_id INT,
  publication_date DATETIME,
  article_link VARCHAR(100),
  PRIMARY KEY (article_id)
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

-- GET
DROP TABLE IF EXISTS weight_vector;
CREATE TABLE IF NOT EXISTS weight_vector
(
    sequence_number INTEGER AUTO_INCREMENT PRIMARY KEY,
    beta_vals varchar(100)
);

INSERT INTO weight_vector (beta_vals) VALUES ("[0.0, -0.21913580557953766]");

-- POST/DELETE
DROP TABLE IF EXISTS likes;
CREATE TABLE IF NOT EXISTS lakes
(
  likes_id INT PRIMARY KEY AUTO_INCREMENT,
  article_id INT,
  user_id INT,
  date_liked datetime
);

-- POST/DELETE
DROP TABLE IF EXISTS saves;
CREATE TABLE IF NOT EXISTS saves
(
  saves_id INT PRIMARY KEY AUTO_INCREMENT,
  article_id INT,
  user_id INT,
  date_saved datetime
);

-- POST/DELETE
DROP TABLE IF EXISTS shares;
CREATE TABLE IF NOT EXISTS shares
(
  shares_id INT PRIMARY KEY AUTO_INCREMENT,
  article_id INT,
  user_id INT,
  date_shared datetime
);


-- PUT 
DROP TABLE IF EXISTS filters;
CREATE TABLE IF NOT EXISTS filters
(
  filter_id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  start_date date,
  end_date date,
  country_about VARCHAR(50),
  country_from VARCHAR(50)
);


-- GET
DROP TABLE IF EXISTS recently_viewed;
CREATE TABLE IF NOT EXISTS recently_viewed
(
  view_id INT PRIMARY KEY,
  user_id INT,
  article_id INT,
  date_viewed datetime
);


-- 





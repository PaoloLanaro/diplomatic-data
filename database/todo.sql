drop database if exists todoApp;
create database if not exists todoApp;

use todoApp;

CREATE TABLE if not exists users (
    userId INTEGER AUTO_INCREMENT PRIMARY KEY,
    firstName VARCHAR(40),
    lastName VARCHAR(40),
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE if not exists tasks (
    taskId Integer AUTO_INCREMENT,
    userID Integer,
    description varchar(255),
    dueDate DATE,
    completed boolean,
    Constraint PK01 PRIMARY KEY (taskID),
    Constraint FK01 FOREIGN KEY (userID) REFERENCES users(userID)
                   on update cascade on delete restrict
);

INSERT INTO users(firstName, lastName, email) 
VALUES ('Mark', 'Fontenot', 'm.fontenot@northeastern.edu'),
       ('John', 'Doe', 'j.doe@anyurl.com');


INSERT INTO tasks(userID, description, dueDate, completed) 
VALUES (1, 'Buy milk', '2024-04-06', false),
       (1, 'Make vet appt for Winston', '2024-04-05', false),
       (2, 'Study for quiz', '2024-04-07', false),
       (2, 'Buy pencils', '2024-04-08', false);

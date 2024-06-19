-- Create the database "hbtn_0d_usa"
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database "hbtn_0d_usa"
USE hbtn_0d_usa;

-- Create the "states" table
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Create the table called "cities"
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

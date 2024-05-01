CREATE DATABASE IF NOT EXISTS challenge_db;
USE challenge_db;

CREATE TABLE IF NOT EXISTS challenge_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_db VARCHAR(255),
    owner_email VARCHAR(255),
    manager_email VARCHAR(255),
    db_classification VARCHAR(255),
    db_severity VARCHAR(255)
);
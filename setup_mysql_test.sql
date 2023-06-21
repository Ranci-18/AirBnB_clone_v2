-- Creates hbnb_test_db database if it does not exists
-- Creates user hbnb_test@localhost if it does not exist
-- Grants all priviledges to the user on the hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON perfomance_schema.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
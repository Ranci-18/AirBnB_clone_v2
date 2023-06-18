-- script prepares a MYSQL server for the project
-- it first creates database hbnb_dev_db without fail
-- then creates user hbnb_dev@localhost without fail
-- grants all permissions on hbnb_dev_db
-- grants select permissions on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `perfomance_schema`.* TO 'hbnb_test'@'localhost';

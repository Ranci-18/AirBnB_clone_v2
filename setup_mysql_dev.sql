-- script prepares a MYSQL server for the project
-- it first creates database hbnb_dev_db without fail
-- then creates user hbnb_dev@localhost without fail
-- grants all permissions on hbnb_dev_db
-- grants select permissions on performance_schema
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
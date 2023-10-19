-- Create the database
CREATE DATABASE IF NOT EXISTS html2md;

-- Create the user
CREATE USER IF NOT EXISTS 'ugosamsue'@'%' IDENTIFIED BY 'html2md_devs';

-- Grant all privileges on the database to created user
GRANT ALL ON html2md.* TO 'ugosamsue'@'%';

-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;

-- Show available database
SHOW DATABASES;


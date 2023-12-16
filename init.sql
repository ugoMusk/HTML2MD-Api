-- Create the database
CREATE DATABASE IF NOT EXISTS html2md;

-- Create the user
CREATE USER IF NOT EXISTS 'html2md_devs'@'%' IDENTIFIED BY 'html2md_pwd';

-- Grant all privileges on the database to created user
GRANT ALL ON html2md.* TO 'html2md_devs'@'%';

-- Flush the privileges to apply the changes
FLUSH PRIVILEGES;



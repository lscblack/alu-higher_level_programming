-- list privileges
-- Initial attempt to show privileges, expecting an error
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Creating user user_0d_1 if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';

-- Granting all privileges to user_0d_1 on all databases
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Show privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Attempting to show privileges for user_0d_2, expecting an error
SHOW GRANTS FOR 'user_0d_2'@'localhost';

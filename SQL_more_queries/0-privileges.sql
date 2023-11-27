-- Check if user_0d_1 exists and display its grants
SELECT COUNT(*) AS user_0d_1_exists FROM mysql.user WHERE User = 'user_0d_1' AND Host = 'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check if user_0d_2 exists and display its grants
SELECT COUNT(*) AS user_0d_2_exists FROM mysql.user WHERE User = 'user_0d_2' AND Host = 'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

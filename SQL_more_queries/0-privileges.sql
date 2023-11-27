-- Check if user_0d_1 exists
SELECT 
    GROUP_CONCAT(privilege_type) AS privileges
FROM 
    information_schema.USER_PRIVILEGES 
WHERE 
    GRANTEE = "'user_0d_1'@'localhost'";


-- Check if user_0d_2 exists
SHOW GRANTS FOR 'user_0d_2'@'localhost';

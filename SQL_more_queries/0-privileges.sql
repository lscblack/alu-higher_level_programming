-- select
SELECT
    CASE
        WHEN EXISTS (
            SELECT 1 FROM mysql.user WHERE User = 'user_0d_1' AND Host = 'localhost'
        ) THEN
            CONCAT(
                'GRANT ',
                GROUP_CONCAT(privilege_type SEPARATOR ', '),
                ' ON *.* TO ',
                QUOTE(GRANTEE),
                ';'
            )
        ELSE
            CONCAT(
                'Grants for ', 
                GRANTEE, 
                '\n', 
                GROUP_CONCAT(privilege_type SEPARATOR ', ')
            )
    END AS privilege_statement
FROM
    information_schema.USER_PRIVILEGES
WHERE
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'")
GROUP BY
    GRANTEE;

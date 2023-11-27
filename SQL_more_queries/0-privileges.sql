-- select
SELECT
    CONCAT(
        'GRANT ',
        GROUP_CONCAT(privilege_type SEPARATOR ', '),
        ' ON *.* TO ',
        QUOTE(GRANTEE),
        ';'
    ) AS privilege_statement
FROM
    information_schema.USER_PRIVILEGES
WHERE
    GRANTEE IN ("'user_0d_1'@'localhost'", "'user_0d_2'@'localhost'")
GROUP BY
    GRANTEE;

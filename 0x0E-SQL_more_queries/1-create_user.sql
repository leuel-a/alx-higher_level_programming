-- Creates a new user in MySQL server
-- Username: `user_0d_1` Password: `user_0d_1_pwd`
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

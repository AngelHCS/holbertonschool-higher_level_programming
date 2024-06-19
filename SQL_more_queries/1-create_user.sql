-- Create the user "user_0d_1"
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user "user_0d_1"
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the changes
FLUSH PRIVILEGES;

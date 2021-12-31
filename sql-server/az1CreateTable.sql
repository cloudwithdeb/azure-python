--CREATE SQL TABLES--
-- Create a new table called 'TableName' in schema 'SchemaName'
-- Drop the table if it already exists
IF OBJECT_ID('users', 'U') IS NOT NULL
DROP TABLE SchemaName.TableName
GO
-- Create the table in the specified schema
CREATE TABLE users
(
    user_id INT NOT NULL PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    age INTEGER NOT NULL
);
GO
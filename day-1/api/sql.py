SELECT_ONE = "SELECT 1"
SELECT_USER = "SELECT TOP(1) USERNAME FROM [current_user] ORDER BY date DESC"
CREATE_USER_TABLE = """
CREATE TABLE [current_user]
(
    USERNAME varchar(50),
    DATE DATETIME
);
"""
INSERT_USER = "INSERT INTO [current_user](USERNAME, DATE) VALUES ('{user}', GETDATE())"
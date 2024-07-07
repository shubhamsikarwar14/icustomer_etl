-- Create the schema for storing user interaction data
CREATE TABLE IF NOT EXISTS user_interactions (
    interaction_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255) NOT NULL,
    product_id VARCHAR(255) NOT NULL,
    action VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    interaction_count INT
);

-- Insert data into the user_interactions table
INSERT INTO user_interactions (interaction_id, user_id, product_id, action, timestamp, interaction_count) VALUES
('1', '1001', 'P100', 'click', '2023-01-01 12:00:00', 2),
('2', '1002', 'P101', 'view', '2023-01-01 12:05:00', 3),
('3', '1001', 'P102', 'click', '2023-01-01 12:10:00', 1),
('4', '1003', 'P103', 'view', '2023-01-01 12:15:00', 1),
('5', '1002', 'P101', 'click', '2023-01-01 12:20:00', 3),
('6', '1003', 'P102', 'view', '2023-01-01 12:25:00', 1),
('7', '1001', 'P100', 'click', '2023-01-01 12:30:00', 2),
('8', '1004', 'P104', 'view', '2023-01-01 12:35:00', 2),
('9', '1002', 'P101', 'click', '2023-01-01 12:40:00', 3),
('10', '1004', 'P104', 'view', '2023-01-01 12:45:00', 2);

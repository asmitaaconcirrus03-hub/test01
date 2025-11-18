-- Database schema for storing pilot flying hours
CREATE TABLE pilot_hours (
    pilot_id INT PRIMARY KEY,
    last_12_months_hours DECIMAL(10, 2)
);
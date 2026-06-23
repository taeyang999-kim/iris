CREATE TABLE iris_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sl FLOAT,
    sw FLOAT,
    pl FLOAT,
    pw FLOAT,
    result VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
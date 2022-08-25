CREATE TABLE IF NOT EXISTS users (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(20) NOT NULL, 
    password VARCHAR(100) NOT NULL,
    aadhar INT NOT NULL PRIMARY KEY,
    DOB VARCHAR(20) NOT NULL,
    isApproved INT DEFAULT 0,
    phone INT NOT NULL, 
    email VARCHAR(30) NOT NULL UNIQUE,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    modified_by INT,
    FOREIGN KEY (modified_by) REFERENCES users(id)
    );

CREATE TABLE IF NOT EXISTS user_role (
    id INT PRIMARY KEY AUTO_INCREMENT,
    role_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (role_id) REFERENCES role(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS role (
    id INT PRIMARY KEY AUTO_INCREMENT,
    role_name VARCHAR(20) NOT NULL,
    created_at TIMESTAMP,
    modified_by INT,
    FOREIGN KEY (modified_by) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS approval_requests (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_aadhar INT NOT NULL,
    account_type INT NOT NULL,
    approved_by INT NOT NULL,
    created_at TIMESTAMP,
    approved_at TIMESTAMP,
    FOREIGN KEY (account_type) REFERENCES account_type(id),
    FOREIGN KEY (user_aadhar) REFERENCES users(aadhar),
    FOREIGN KEY (approved_by) REFERENCES users(id),
);
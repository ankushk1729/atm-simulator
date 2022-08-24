CREATE TABLE users (
    id INT UNIQUE NOT NULL,
    full_name VARCHAR(20) NOT NULL, 
    password VARCHAR(20) NOT NULL,
    aadhar INT NOT NULL PRIMARY KEY,
    isApproved INT,
    phone INT, 
    email VARCHAR(30),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (modified_by) REFERENCES users(id)
    );

CREATE TABLE role (
    id INT PRIMARY KEY,
    FOREIGN KEY (role_id) REFERENCES role(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    created_at TIMESTAMP,
);

CREATE TABLE users_role (
    id INT PRIMARY KEY,
    role_name VARCHAR(20),
    created_at TIMESTAMP,
    FOREIGN KEY (modified_by) REFERENCES users(id)
);

CREATE TABLE approval_requests (
    id INT PRIMARY KEY,
    FOREIGN KEY (user_aadhar) REFERENCES users(aadhar),
    FOREIGN KEY (account_type) REFERENCES account_type(id),
    created_at TIMESTAMP,
    approved_at TIMESTAMP,
    FOREIGN KEY (approved_by) REFERENCES users(id),
);
CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(70) UNIQUE NOT NULL,
    full_name VARCHAR(20) NOT NULL, 
    password VARCHAR(100) NOT NULL,
    aadhar INT NOT NULL PRIMARY KEY,
    DOB VARCHAR(20) NOT NULL,
    isApproved INT DEFAULT 0,
    phone INT NOT NULL, 
    email VARCHAR(30) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by VARCHAR(70),
    FOREIGN KEY (modified_by) REFERENCES users(id)
    );

CREATE TABLE IF NOT EXISTS user_role (
    id INT PRIMARY KEY AUTO_INCREMENT,
    role_id INT NOT NULL,
    user_id VARCHAR(70) NOT NULL,
    FOREIGN KEY (role_id) REFERENCES role(id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS role (
    id INT PRIMARY KEY AUTO_INCREMENT,
    role_name VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by VARCHAR(70),
    FOREIGN KEY (modified_by) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS approval_requests (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_aadhar INT NOT NULL,
    account_type INT NOT NULL,
    approved_by VARCHAR(70),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    approved_at TIMESTAMP DEFAULT NULL,
    FOREIGN KEY (account_type) REFERENCES account_type(id),
    FOREIGN KEY (user_aadhar) REFERENCES users(aadhar),
    FOREIGN KEY (approved_by) REFERENCES users(id),
    status INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS account (
    account_num INT PRIMARY KEY AUTO_INCREMENT,
    balance INT DEFAULT 0,
    account_type INT,
    user_aadhar INT,
    FOREIGN KEY (account_type) REFERENCES account_type(id),
    FOREIGN KEY (user_aadhar) REFERENCES users(aadhar),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by VARCHAR(70),
    FOREIGN KEY (modified_by) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS account_type (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(20) DEFAULT 'savings',
    max_withdrawal_amount INT DEFAULT 0,
    min_balance INT DEFAULT 5000,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by VARCHAR(70),
    FOREIGN KEY (modified_by) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS transaction(
    id INT PRIMARY KEY AUTO_INCREMENT,
    txn_type INT,
    amount  INT,
    account_num  INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(txn_type) REFERENCES  transaction_type(id),
    FOREIGN KEY(account_num) REFERENCES  account(account_num)
    );

CREATE TABLE IF NOT EXISTS transaction_type (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    modified_by  VARCHAR(70),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(modified_by) REFERENCES  users(id)
    );
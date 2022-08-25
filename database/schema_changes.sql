CREATE TABLE IF NOT EXISTS users (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(20) NOT NULL, 
    password VARCHAR(100) NOT NULL,
    aadhar INT NOT NULL PRIMARY KEY,
    DOB VARCHAR(20) NOT NULL,
    isApproved INT DEFAULT 0,
    phone INT NOT NULL, 
    email VARCHAR(30) NOT NULL,
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

CREATE TABLE IF NOT EXISTS transactions(
    ID INT ,
    TXN_TYPE INT,
    AMOUNT  INT,
    ACCOUNT_NUM  INT,
    CREATED_AT  Timestamp,
    PRIMARY KEY(ID);
    FOREIGN KEY(TXN_TYPE) REFERENCES  transaction_type(id)
    FOREIGN KEY(ACCOUNT_NUM REFERENCES  account_type(ACCOUNT_NUM))
    );

CREATE TABLE IF NOT EXISTS transaction_type (
    ID INT,
    full_name VARCHAR(30),
    MODIFIED_BY  INT,
    UPDATED_AT  Timestamp,
    CREATED_AT  Timestamp,
    FOREIGN KEY(MODIFIED_BY) REFERENCES  account(id)
    );
    


CREATE TABLE IF NOT EXISTS account_type ( 
    ID INT,
    full_name VARCHAR(30),
    MAX_WITHDRAW INT,
    MIN_BALANCE INT, 
    MODIFIED_BY  INT,
    UPDATED_AT  Timestamp,
    CREATED_AT  Timestamp,
    FOREIGN KEY(MODIFIED_BY) REFERENCES  user(id)
    );
    
    
CREATE TABLE IF NOT EXISTS account ( 
    ACCOUNT_NUM INT,
    ACC_TYPE INT,
    BALANCE INT,
    USER_ID INT, 
    MODIFIED_BY  INT,
    UPDATED_AT  Timestamp,
    CREATED_AT  Timestamp,
    PRIMARY KEY(ACCOUNT_NUM)
    FOREIGN KEY(ACC_TYPE) REFERENCES  account_type(id)
    FOREIGN KEY(USER_ID) REFERENCES  account_type(id)
    FOREIGN KEY(MODIFIED_BY) REFERENCES  user(id)
);

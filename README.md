# ATM Simulator to Deposit and withdrawal amount 

## Tasks completed 
- User signup and login
- Add to user_role mapping
- Create user
- Approve user by id and aadhar
- Search user by name
- Get single user data

## Pending remember
- Add queries.xml root tree import to util function
- Mask password

## User account information  

- Account number
- Account holder name  
- DOB - Contact  
- Phone  
- E-mail  
- Account type 
- Saving (min Balance - 5000) 
- Current (min Balance - 10000) 

## Account Opening by Admin  

- Admin can open account for user 
- Can define Type of account  
- Saving  
- Current  

 
## Account Opening by user  

- User can apply for account through screen 
- After Admin approve user account will active  

 
## ATM Menu  

- User login  
- After login user can view account information 
- User can view Balance amount 
- User can view Transaction  
- Withdrawal amount  
    - User cannot Withdrawal in minus  
    - If account type is "Saving" user cannot Withdrawal  amount more then 5000 
    - If Account type "Current" any amount 
    - If user Withdrawal amount is more than mini amount show warning 
- Deposit amount  
    - User can deposit amount 
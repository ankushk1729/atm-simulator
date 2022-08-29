# ATM Simulator to Deposit and withdrawal amount 

## Functions
- User signup and login
- Add to user_role mapping
- Approve user by id and aadhar
- Search user by name
- Get single user data
- Add to approval requests on signup
- Get all txns
- Get all users
- Get all accounts
- Get account info
- Check user approved
- Withdraw
- Deposit
- Get user transactions
- On approval and account creation minimum balance is added acc to account requested
- Get user transactions
- Delete user
- Show user age

## Admin ops
- search user
-approve user
- create new account



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
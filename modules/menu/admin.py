class AdminMenu():
    def handler(self):
        while True:
            print('Enter 1 to deposit')
            print('Enter 2 to withdraw')
            print('Enter 3 to get all transactions')
            print("enter 0 to end")

            try:
                choice = input()
                if not choice.isdigit() : raise TypeError('Invalid input, please enter a number')
                if not (int(choice) >= 0 and int(choice) <= 3) : raise ValueError('Please enter a number between 0 and 3')
                break
            except ValueError as error:
                print(str(error))
            except TypeError as error:
                print(str(error))


        choice = int(choice)
        match choice : 
            case 1: 
                self.deposit()
            case 2:
                self.withdrawal()
            case 3:
                self.viewTransaction()    
            case 0:
                return 0

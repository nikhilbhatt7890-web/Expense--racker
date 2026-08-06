from key import derive_data 
import get_positive_num as number
class python_banking:
    def __init__(self,name:str):
        self.name = name 
        self.data = derive_data(name)
        self.user_name = name
        
    
    
    def take_request(self,avl_operations): # --> completed
        
        menu = """
        Choose an option:
        1. Show bank balance  (type: show balance)
        2. Add money          (type: add)
        3. Add expense        (type: expense)
        4. Overall report     (type: report)
        5. Quit               (type: quit)
            """

        while True:
            # // todo // fix show balance key error 
            req = input(menu + "\nEnter your choice: ").strip().upper()
            

            if req in avl_operations:
                return req

            print("❌ Invalid option. Please try again.")

    def proceed(self):# --> completed
            while True:
                return_to_main = input("Type 'continue' to proceed: ").strip()
                if return_to_main == "continue":
                    return True
                print("❌ Invalid option. Please try again.\n")
              

    def current_bank_balance(self):# --> completed
        
        bank_bal = self.data["account_bal"]
        s = f'''
        ====================================
            Current Balance: {bank_bal}
        
        Your bank balance has been displayed.
        '''
        print(s) 

        return self.proceed()

    def expense(self):# --> completed

        expense_amount = number.get_positive("Enter the expense amount (₹): ")
        Type = self.expense_type()
        self.update_bank_balance(expense_amount)
        return self.proceed()
        
    def expense_type(self):
        pass 

    

    def add_money(self):
        ...

    def update_bank_balance(self,money:int):
             print("success",money)
            


    def generate_report(self):
        ...

    def update_data(new_data): 
        ...
 
def Start_interaction(name):
    
    print("\n","|","--"*20,"|")  
    print("gotcha user interaction","\n")

    Bank = python_banking(name) 
    avl_operations = {
            "SHOW BALANCE":Bank.current_bank_balance,
            "ADD":Bank.update_bank_balance,
            "EXPENSE":Bank.expense,
            "REPORT":Bank.expense_type,
            'QUIT':"return"
            }
    
    while True :

        user_req = Bank.take_request(avl_operations) # user input 
        if user_req == "QUIT":
            return "complete"  
                                      
        avl_operations[user_req]() #--> evaluate_user_req
    
    

# Start_interaction("nikhil")

from key import derive_data 

class python_banking:
    def __init__(self,name:str):
        self.name = name 
        self.data = derive_data(name)
        self.user_name = name
        self.avl_functions = {"Show balance":"","add":"","expense":"","report":""}

    def take_request(self):
        
        menu = """
        Choose an option:

        1. Show bank balance  (type: show balance)
        2. Add money          (type: add)
        3. Add expense        (type: expense)
        4. Overall report     (type: report)
            """

        while True:
            # // todo // fix show balance key error 
            req = input(menu + "\nEnter your choice: ").strip().lower()
            print(req)

            if req in self.avl_functions:
                return req

            print("❌ Invalid option. Please try again.")
        

    def current_bank_balance(self):
        bank_bal = self.data["account_bal"]
        print(bank_bal) 
        print("create a branch before starting")

    def update_bank_balance(self):
        pass 


    def expense(self):
        pass 


    def expense_type(self):
        pass 

    def generate_report(self):
        ...
    
def Start_interaction(name):

    print("\n","|","--"*20,"|")
    print("gotcha user interaction","\n")
    Bank = python_banking(name)
    user_request = Bank.take_request()
    print(user_request)
    Bank.current_bank_balance()



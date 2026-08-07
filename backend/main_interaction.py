from key import derive_data 
import get_positive_num as number
class python_banking:
    def __init__(self,name:str):
        self.name = name 
        self.data = derive_data(name)
        self.user_name = name
        
    
    def compare(self,to_be_com,to_com):
         if to_be_com == to_com:
              return True
         return False


    def take_request(self,avl_operations): # --> completed
        
        menu = """   Choose an option:
        1. Show bank balance  (type: show balance)
        2. Add money          (type: add)
        3. Add expense        (type: expense)
        4. Overall report     (type: report)
        5. Quit               (type: quit)
            """

        while True:
            
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
        self.expense_type(expense_amount)
        self.update_bank_balance(expense_amount,"EXPENSE")
        return self.proceed()


    def check_expense(expense_data:dict,expense_amount:int):  # --> no work defined 
         pass 


    def expense_type(self,total_amount):  # todo : upgrade  the quality of code 
 
        expense_categories = {
    "FOOD": 0,
    "GROCERIES": 0,
    "RENT": 0,
    "ELECTRICITY": 0,
    "WATER": 0,
    "INTERNET": 0,
    "MOBILE RECHARGE": 0,
    "TRANSPORTATION": 0
      }

        Categories = expense_categories.keys()

        prompt = "\n".join(Categories)
        while True:   
          expense_t = input(f"{prompt}\nENTER ONE OF THE OPTIONS ABOVE : ").upper().strip()

          if expense_t in Categories :   
               how_much = number.get_positive(f"How much for {expense_t}: ")
               expense_categories[expense_t] += how_much
               done = self.compare((input("\ndone adding all expense 'yes' to save : ").upper().strip()),"YES")
               
               if done  :
                   print('\nHAVE TO COMPLETE IT Tomorow ')
                   return
        
               continue
          print('\nWRONG CATEGORY\n')


    def add_money(self):

        prompt = "How much money do you want to add : "
        money = number.get_positive(prompt)
        self.update_bank_balance(money,"ADD")
        print("success")


    def update_bank_balance(self,money:int,transaction_type):
        with open(f"backend/{self.name}_data.txt","w") as f :  
            if transaction_type=="ADD":
                        self.data["account_bal"] += money
            elif transaction_type=="EXPENSE":
                        self.data["account_bal"] -= money
            else :
                 raise ValueError("NO DATA DETECTED")
            
            f.write(str(self.data))
            return "SUCCESS"
             



            

    # untouched files 
    def generate_report(self):
        ...

    def update_data(new_data): 
        ...
 
def Start_interaction(name):
    
    print("\n","|","--"*20,"|")  
    Bank = python_banking(name) 
    avl_operations = {
            "SHOW BALANCE":Bank.current_bank_balance,
            "ADD":Bank.add_money,
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

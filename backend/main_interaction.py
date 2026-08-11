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
        expense_data = self.user_expense_type(expense_amount)
        self.update_bank_balance(expense_amount,"EXPENSE")
        return self.proceed()




    def get_cat(self,prompt:str,categories:list):

        while True: 
            user_cat = input(f"{prompt}\nEnter your categories: ").upper().strip()
            if user_cat not in categories : 
                print("\nINVALID CATEGORY\n")
                continue
            return user_cat
        
    def get_amount(self,user_cat:str,total_amount:int,total_expense_added:int):
         while True:
            amount = number.get_positive(f"How much for {user_cat}: ")
            
            if amount > total_amount or amount + total_expense_added > total_amount :
                print('\n❌ Cannot be more than total expense')
                continue
            return amount
         
    def user_expense_type(self,total_amount): 
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
        prompt = ":\n".join(Categories)
        total_expense_added = 0  
        while True:

            user_cat = self.get_cat(prompt,Categories)
            amount = self.get_amount(user_cat,total_amount,total_expense_added)

            total_expense_added += amount

            expense_categories[user_cat] += amount
            if sum(expense_categories.values()) == total_amount :
                print('\nDone adding expenses')
                self.data["EXPENSE_HISTORY"] = expense_categories
                return expense_categories 
            
            
                         #    done = self.compare((input("\ndone adding all expense 'yes' to save : ").upper().strip()),"YES")
                            
           

    def add_money(self):

        prompt = "How much money do you want to add : "
        money = number.get_positive(prompt)
        self.update_bank_balance(money,"ADD")
        print("success")
        return self.proceed()


    def update_bank_balance(self,money:int,transaction_type):
        with open(f"backend/{self.name}_data.txt","w") as f :  
            if transaction_type=="ADD":
                        self.data["account_bal"] += money
                        print('SUCCESS fully added into your bank balance ')
            elif transaction_type=="EXPENSE":
                        self.data["account_bal"] -= money
            else :
                 raise ValueError("NO DATA DETECTED")
            
            f.write(str(self.data))
            return "SUCCESS"
             



            

    # untouched files 
    def generate_report(self):
        print('\nLast transaction report\n')
        default = 18 
        print("┌" + "─" * 20 + "┐")
        


        for i in range(12):
          if i == 1 :
               print("|"+" "*3+"PYTHON BANKING"+" "*3+"|")
          elif i == 3 :
               print("|"+" "*2+"Name - "+f"{self.name}"+" "*(default-len(self.name)-7)+"|")
          elif i == 4 :
               account = self.data['bank_acc_name']
               print("|"+" "*2+"Bank - "+f"{account}"+" "*(default-len(account)-7)+"|")
          elif i == 6 :
               print("|"+" "*2+"Transactions"+" "*6+"|")
          elif i == 8 :
               pass
          else :              
               print("|"+" "*(default+2)+"|")
            
        
        print("└" + "─" * 20 + "┘")
                    
       

    def update_data(new_data): 
        ...
 
def Start_interaction(name):
    
    print("\n","|","--"*20,"|")  
    Bank = python_banking(name) 
    avl_operations = {
            "SHOW BALANCE":Bank.current_bank_balance,
            "ADD":Bank.add_money,
            "EXPENSE":Bank.expense,
            "REPORT":Bank.generate_report,
            'QUIT':"return"
            }
    
    while True :

        user_req = Bank.take_request(avl_operations) # user input 
        if user_req == "QUIT":
            return "complete"  
                                      
        avl_operations[user_req]() #--> evaluate_user_req
    
    

# # Start_interaction("nikhil") 
# c = python_banking("nikhil")
# c.generate_report()
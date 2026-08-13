from key import derive_data 
import get_positive_num as number
class python_banking:
    def __init__(self,name:str):
        self.name:str = name 
        self.data:dict = derive_data(name)
        
    
    def compare(self,to_be_com,to_com):
         if to_be_com == to_com:
              return True
         return False

    def get_cat(self,prompt:str,categories:list):

        while True: 
            user_cat = input(f"{prompt}\nEnter your categories: ").upper().strip()
            if user_cat not in categories : 
                print("\nINVALID CATEGORY\n")
                continue
            return user_cat
        
    def get_amount(self,user_cat:str,total_amount:int,total_added:int):
         while True:
            amount = number.get_positive(f"How much for {user_cat}: ")
            
            if amount > total_amount or amount + total_added > total_amount :
                print('\n❌ Cannot be more than total expense')
                continue
            return amount
    
    def Transaction_type(self,trans_type:str,Categories:list,total_amount:int):
            
            
            prompt = ":\n".join(Categories)
            total_added = 0  
            while True:
             
                user_cat = self.get_cat(prompt,Categories)
                amount = self.get_amount(user_cat,total_amount,total_added)
             
                total_added += amount
             
                Categories[user_cat] += amount
                if sum(Categories.values()) == total_amount :
                    print('\nDone adding expenses')
                    self.data[f"{trans_type.upper()}_HISTORY"] = Categories
                    return Categories 
                
    def take_request(self,avl_operations:dict): # --> completed
        
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
    
        expense_data = self.Transaction_type("EXPENSE",self.data["EXPENSE"],expense_amount)
        self.update_bank_balance(expense_amount,"EXPENSE")
        return self.proceed()
      
    def add_money(self): # --> completed

        prompt = "How much money do you want to add : "
        money = number.get_positive(prompt)
        self.Transaction_type("ADD",self.ALL_categories["ADD"],money)
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
             

    def fetch_data(self,word:str,):
        
            Current_data : dict = self.data[f"{word.upper()}_HISTORY"] 
            transactions:list = [(point,value) for point,value in Current_data.items() if Current_data[point]!=0]
            return transactions

    def print_cat(self,word:str,less):   
          transactions:list = self.fetch_data(word)
          s = "  " + f"{word}-> {sum([val[1] for val in transactions])}"
          print("|"+"  "+"-"*len(s)+" "*less(s+"  ")+"|")
          print("|"+s+" "*less(s)+"|")
          print("|"+"  "+"-"*len(s)+" "*less(s+"  ")+"|")
                        
          for trans , value in transactions:
                s = f" {trans.lower()}-> {value}"
                print("|"+s+" "*less(s)+"|")
        
    
    def generate_report(self):   # completed
        print('\nLast transaction report\n')
        default = 30 # must be even
        print("┌" + "─" * (default) + "┐")
        less = lambda x : default-len(x)


        for i in range(10):
          
          if i == 1 :
               s = "PYTHON BANKING"
               half = int(less(s)//2)
               print("|"+"-"*(default)+"|")
               print("|"+" "*half+s+" "*half+"|")
               print("|"+"-"*(default)+"|")
          elif i == 2 :
               s = "  Name - "+f"{self.name}"
               print("|"+s+" "*(default-len(s))+"|")
               
          elif i == 3  :
               account = self.data['bank_acc_name']
               s = "  "+"Bank - "+f"{account}"
               print("|"+s+" "*less(s)+"|")
               print("|"+"-"*default+"|")

          elif i == 5 :
               s = "  Transactions"
               
               print("|"+s+" "*less(s)+"|")
               
               
          elif i == 6 :
            self.print_cat("ADD",less)
          elif i == 7 :
                self.print_cat("EXPENSE",less)
          elif i == 9 :
               print("|"+"_"*default+"|")
               s = " " + f"Current bank bal-> {self.data['account_bal']}"
               print("|"+s+" "*less(s)+"|")
          else :              
               print("|"+" "*(default)+"|")
            
        
        print("└" + "─" * default + "┘")
        print("REPORT DISPLAYED SUCCESSFULLY")
        return self.proceed()             
       


 
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
    


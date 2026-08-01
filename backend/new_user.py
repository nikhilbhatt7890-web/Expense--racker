
class work :
    def __init__(self,name:str):
        self.name = name
        self.file =f"backend/{self.name}_data.txt"
        # self.u_email = ""
        # self.bnk_name = ""
        # self.bal = ""
    
    def details(self):
            self.u_email = input("\nlet us start the process \ntell your EMAIL_ID : " )
            self.bnk_name = input("\nNoted the bank in which you have your account\n(bank name): ")
            while True:
                try : 
                    self.bal = int(input("\nyour bank balance : "))
                    break
                except Exception :
                    print("\nenter a vaild bank balance")
                    continue
            

    def create_account(self):
        with open(self.file,"w") as f :
            self.details()
            user_info = {
                "user_name":self.name,
                "user_email":self.u_email,
                "bank_acc_name":self.bnk_name,
                "account_bal":self.bal,
            }
            f.write(str(user_info))


    def authenticate(self):
        # self.name = self.name.lstrip
        try:
            with open(self.file,"r"):
               return True
            
        except FileNotFoundError:
            print("file not found ")
            return False
        
        except Exception as e :
            return None
    
       
    def assign_work(self,exists):
        case = {
        True:"ALR_EXISTS",
        False:self.create_account, ###### assign work
        None:"ERROR"
    }
        if not exists :
            case[exists]()
        else:
            return exists

    
   

def new(name):

    main_obj = work(name)
    exists = main_obj.authenticate()
    to_do = main_obj.assign_work(exists)
    # print(to_do)
    return to_do  

new(input("name = "))   #learn about the re moduel
 # find a way to solve the same name in diffrent format problem
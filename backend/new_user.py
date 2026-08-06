import get_positive_num as number 
class work :
    def __init__(self,name:str):
        self.name = name
        # self.u_email = ""
        # self.bnk_name = ""
        # self.bal = ""
    
    def details(self):
            self.u_email = input("\nlet us start the process \ntell your EMAIL_ID : " )
            self.bnk_name = input("\nNoted the bank in which you have your account\n(bank name): ")
            self.bal = number.get_positive("\nyour bank balance")
            print("-"*10)
            self.key = input("\nCreate a login key :   ").lower()


            

    def create_account(self):
        with open(f"backend/{self.name}_data.txt","w") as f :
            self.details()
            user_data = {
                "user_name":self.name,
                "user_email":self.u_email,
                "bank_acc_name":self.bnk_name,
                "account_bal":self.bal,
                "key":self.key
            }

            f.write(str(user_data))
        return "NEW_SUCCESS"

    
   

def new(name): 
    main_obj = work(name)
    status = main_obj.create_account()
    # print(to_do)
    return status  


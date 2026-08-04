from key import derive_data 

class python_banking:
    def __init__(self,name:str):
        self.data = derive_data(name)
        self.user_name = name

    def bank_balance(self):
        pass 

    def update_bank_balance(self):
        pass 

    
def Start_intraction(name):
    print("|","--"*20,"|")
    print("gotcha user interaction","\n")




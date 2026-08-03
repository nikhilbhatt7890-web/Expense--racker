from ast import literal_eval




class user_login :
    def __init__(self,name:str,user_data:dict):
        self.name = name 
        self.data = user_data
        self.key = user_data["key"]       

    def start_authentication(self):
        print(self.key)
       
        while True:
            entered_key = input("Enter your login key: ").strip().lower()

            if entered_key.lower() == "quit":
                print("Program terminated.")
                return "UNAPPROVED"

            if entered_key == self.key:
                print("Key matched successfully.")
                return "APPROVED"

            print("\nIncorrect key. Type 'quit' to exit.")


def derive_data(name):
    
    with open(f"backend/{name}_data.txt","r") as f :
        data = f.read()
        user_data = literal_eval(data)
    return user_data
    
    

def key(name):
    print("-"*50)
    data = derive_data(name)
    work = user_login(name,data)
    status = work.start_authentication()
    return status



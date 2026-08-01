from new_user import new
from key import key
from login import login

USER_NAME = input("hello their may i know your name ? : ").lower()


def authenticate():
        
        file = f"backend/{USER_NAME}_data.txt"
        try:
            with open(file,"r"):
               return True
            
        except FileNotFoundError:
            print("file not found ")
            return False
        
        except Exception as e :
            print(e)
            return None
    
def after_new_login(name):
     print("--"*10)
     print(f"Thank you {name}\n For choosing us\nYour registration is successfull\n")
     
def terminate(name):
     print(f"\nsorry {name} but something bad happen in our side ")
     
def errorhappend(name):
        print(f"\nWelcome back {USER_NAME}")
        return "ERROR_IN_TRACING_FILE"

def initialization(name):
    while True:   
        try :
                user_input = input(
                     "what do you wana do\n" \
                     "1) use a keyword (type 'key')\n" \
                     "2) login using mobile number (type 'login') \n" \
                     "plz enter a valid response -> : "
                ).upper()

                if user_input in AVL_OPTIONS :
                    print()
                    return user_input
                
        except KeyError: 
                print("\n INVALID INPUT : \n")
                continue

def start_working(task):
    work = AVL_OPTIONS[task]
    next_work = work(USER_NAME)
    start = AVL_OPTIONS[next_work]
    start(USER_NAME)
    

     
     

AVL_OPTIONS = {
    True : initialization,
    False:new,
    None:errorhappend,
    "KEY":key,
    "LOGIN" : login,
    "NEW_SUCCESS":after_new_login,
    "ERROR_IN_TRACING_FILE" : terminate

}
 
if __name__ == "__main__":
    assignee = authenticate()
    start_working(assignee)

    

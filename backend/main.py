from new_user import new
from key import key


USER_NAME = input("Hello their may i know your name ? : ").lower()


def authenticate():
        
        file = f"backend/{USER_NAME}_data.txt"
        try:
            with open(file,"r"):
               return True
            
        except FileNotFoundError:
            return False
        
        except Exception as e :
            print(e)
            return None
    
def after_new_login(name):
     print("--"*10)
     print(f"Thank you {name}\n For choosing us\nYour registration is successfull\n")
     next = initialization(name)
     key_r = AVL_OPTIONS[next](name)
     return key_r

     
def terminate(name):
     print(f"\nsorry {name} but something bad happen in our side ")
     
def errorhappend(name):
        
        return "ERROR_IN_TRACING_FILE"

def initialization(name):
    
    while True:   
        try :
                user_input = input(
                     "Want to login using a keyword\n" \
                     "(type 'key')\n" \
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
    key_done = start(USER_NAME)
    print(AVL_OPTIONS[key_done])
    

     
     

AVL_OPTIONS = {
    True : initialization,
    False:new,
    None:errorhappend,
    "KEY":key,
    "NEW_SUCCESS":after_new_login,
    "ERROR_IN_TRACING_FILE" : terminate,
    "APPROVED":"SUCCESS",
    "UNAPPROVED":"TERMINATE"

}
 
if __name__ == "__main__":
    assignee = authenticate()
    start_working(assignee)

    

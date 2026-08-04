from new_user import new
from key import key
from user_intraction import Start_intraction

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
    
# def after_new_login(name):
#      print("--"*10)
#      print(f"Thank you {name}\n For choosing us\nYour registration is successfull\n")
#      next = initialization(name)
#      key_r = AVL_OPTIONS[next](name)
#      return key_r

     
def terminate(name):
     print(f"\nsorry {name} but something bad happen in our side ")
     
# def errorhappend(name):
#         return "ERROR_IN_TRACING_FILE"

def initialization(name):
    print("--"*20,"\n")

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

def start_working(task:bool): # task values: true or false 
    if not(task) :
       initialize_work = AVL_OPTIONS[new(USER_NAME)](USER_NAME) # output --> key
    else :
       initialize_work = AVL_OPTIONS[task](USER_NAME)  # output --> key

    key_status = AVL_OPTIONS[initialize_work](USER_NAME)  # output --> approved , none 
    if key_status is None:
             return "END"                        
    intraction_start = AVL_OPTIONS[key_status](USER_NAME) # output --> yet to decide 
    print("success till interaction")

    
AVL_OPTIONS = {
    True : initialization,
    False:new,
    "KEY":key,
    "NEW_SUCCESS":initialization,
    "APPROVED":Start_intraction,
}
 
if __name__ == "__main__":
    exists_status = authenticate()
    if exists_status is None :
            terminate(USER_NAME)
    start_working(exists_status)

    
